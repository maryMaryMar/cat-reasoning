#!/usr/bin/env python3
"""
Benchmark suite: Natural Language Reasoning vs. CaT Micro-DSL
Calculates token consumption, character ratios, and savings.
"""

import re
import json

def count_tokens(text: str) -> int:
    tokens = re.findall(r'\w+|[^\w\s]|\s+', text)
    return len(tokens)

BENCHMARKS = [
    {
        "name": "Case 1: Server SQLite Lock",
        "natural": """El usuario reporta que el servidor de Minecraft no inicia y se apaga de golpe. 
Primero debo analizar los logs recientes en busca de la causa raíz. 
Al revisar el archivo logs/latest.log encuentro una excepción NullPointerException originada en el plugin nLogin. 
Al profundizar en la traza veo un error de SQLite: database is locked en plugins/nLogin/data.db. 
Esto ocurre porque un hilo anterior no cerró la conexión correctamente o hay permisos insuficientes. 
Para solucionarlo debo comprobar los permisos del archivo con chmod 644 y asegurarme de que no haya otro proceso bloqueándolo. 
Luego verificaré la configuración de nLogin/config.yml para activar el modo de caché en memoria y evitar bloqueos futuros. 
Finalmente prepararé la respuesta informando la causa y la solución aplicada.""",
        "cat": """S = {'err': 'SQLite: database is locked', 'plugin': 'nLogin', 'db': 'plugins/nLogin/data.db'}
root = find_lock_holder(S['db']) or check_perms(S['db'])
action = [
    sys.kill(root.pid) if root else os.chmod(S['db'], 0o644),
    yaml.patch('plugins/nLogin/config.yml', {'database.sqlite.pool_size': 1, 'cache.enabled': True})
]
assert all(verify(a) for a in action)
out = summarize(action)"""
    },
    {
        "name": "Case 2: Java Memory Leak",
        "natural": """Se observa una degradación paulatina del TPS en el servidor PaperMC cuando entran más de 30 jugadores.
Analizando el volcado de memoria de Java (heap dump) y las trazas de CPU, identifico que la clase CustomJoinListener mantiene una referencia estática a una lista de Player objects en lugar de UUIDs.
Como las instancias de CraftPlayer retienen todo el mundo y las entidades circundantes, el Garbage Collector no puede liberarlas cuando el jugador se desconecta, generando una fuga de memoria masiva.
Para resolverlo, es necesario refactorizar la colección estática de Map<Player, Data> a Map<UUID, Data> o utilizar WeakReference.
Además, se debe registrar el evento PlayerQuitEvent para limpiar la entrada correspondiente de la memoria de inmediato.
Comprobamos que el código compile sin warnings y validamos que el heap se estabilice.""",
        "cat": """leak = heap.inspect('CustomJoinListener')
assert leak.retained_type == 'CraftPlayer'  # World & chunk references held
patch = {
    'target': 'Map<Player, CacheData>',
    'fix': 'Map<UUID, CacheData>',
    'event_hook': 'PlayerQuitEvent -> cache.remove(e.getPlayer().getUniqueId())'
}
assert gc.can_reclaim(patch)
out = apply_patch('src/.../CustomJoinListener.java', patch)"""
    },
    {
        "name": "Case 3: Async Queue Architecture",
        "natural": """Tenemos un problema con la pasarela de pagos de PiponShop donde las órdenes simultáneas saturan el hilo principal de Node.js al ejecutar llamadas síncronas a la consola de Pterodactyl.
Debemos cambiar esta arquitectura monolítica por un sistema de cola asíncrono.
Primero evaluamos si añadir Redis o utilizar una cola nativa en memoria con persistencia en SQLite para no sobrecargar el servidor de dependencias externas.
Siguiendo la filosofía Ponytail, la solución más ligera es una cola FIFO en memoria respaldada por una tabla de tareas pendientes en SQLite.
El endpoint de webhook recibirá la notificación de pago, insertará la tarea en estado PENDING y responderá inmediatamente con HTTP 200 al cliente.
Un worker en segundo plano procesará la cola a un ritmo controlado de 2 órdenes por segundo, ejecutando los comandos RCON/Wings de forma segura con reintentos automáticos en caso de fallo.""",
        "cat": """issue = 'sync RCON blocks Node.js event loop under load'
arch_choice = 'Ponytail: SQLite FIFO queue (no Redis overhead)'
pipeline = [
    route.post('/webhook', lambda req: (db.insert('queue', req.body, status='PENDING'), 200)),
    worker.cron(rate='2/sec', fn=lambda task: wings.dispatch(task.cmd).retry(3))
]
assert latency.p99 < 50 and cpu.load < 0.2
out = build_worker(pipeline)"""
    }
]

def run():
    print(f"{'Escenario':<32} | {'Tokens NL':<10} | {'Tokens CaT':<10} | {'Ahorro (%)':<10}")
    print("-" * 72)
    for b in BENCHMARKS:
        t_nl = count_tokens(b["natural"])
        t_cat = count_tokens(b["cat"])
        saving = ((t_nl - t_cat) / t_nl) * 100
        print(f"{b['name']:<32} | {t_nl:<10} | {t_cat:<10} | {saving:<10.1f}%")

if __name__ == "__main__":
    run()
