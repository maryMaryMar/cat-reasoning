---
name: cat-worker
description: >
  Fusión del Protocolo CaT (Code-as-Thought Micro-DSL) y el subagente obrero OpenCode Worker.
  Ahorra entre un 90% y 95% de tokens en modelos de alto consumo (como Argon/Pro) al forzar
  razonamiento interno en micro-código y delegar 100% de la masa de código a opencode-worker.
argument-hint: "[on|off|exec <tarea>]"
license: MIT
---

# CAT-WORKER: Motor Dual de Máxima Eficiencia de Tokens

Combina **Code-as-Thought (CaT)** en el espacio deliberativo interno con **OpenCode Worker (`opencode-worker`)** como ejecutor satélite de coste $0.00.

## 1. Topología del Flujo Dual

```
[Usuario / Tarea Técnica]
       │
       ▼
[Antigravity — Razonamiento CaT Micro-DSL]
       │  • Thinking 100% código declarativo: S -> Root -> Action -> Assert -> Out
       │  • Ahorro de thinking: -60% tokens. Cero prosa o relleno.
       │
       ▼ (CLI Prompt Técnico Quirúrgico)
[opencode-worker — Obrero Headless Gratuito]
       │  • Genera código masivo, parsers, scripts, refactorizaciones.
       │  • Coste en cuota principal: $0.00 / 0 tokens.
       │
       ▼ (Quality Gate Automático: --check python|bash|node)
[Validación Silenciosa & Aplicación en Disco / SFTP]
       │
       ▼
[Salida de Alta Calidad al Usuario (Estilo Fable en Español)]
```

## 2. Invocación y Parámetros

Cuando `cat-worker` está activo:
1. **Razonamiento Interno:** Prohibido el monólogo en lenguaje natural en el `<thought>`. Formular siempre el pipeline `S -> Root -> Action -> Assert -> Out`.
2. **Generación de Código:** Prohibido que Antigravity redacte directamente bloques extensos de código en su propio contexto si superan 15 líneas. Debe delegar a:
   ```bash
   opencode-worker -c --check <python|bash|node> -o <ruta_destino> "instrucción técnica"
   ```
3. **Quality Gate:** Antigravity verifica el archivo generado antes de presentar el resumen al usuario.

## 3. Comandos Rápidos

* `cat-worker on`: Activa el modo orquestador CaT + OpenWorker.
* `cat-worker off`: Desactiva la delegación forzada.
* `cat-worker status`: Muestra el estado del obrero y métricas de cuota.
