---
name: cat-reasoning
description: >
  Motor de razonamiento simbólico Code-as-Thought (CaT) y Micro-DSL declarativo.
  Sustituye la prosa verbal reflexiva en el espacio interno de pensamiento (thinking)
  por un pipeline formal en micro-código (S -> Root -> Action -> Assert -> Out).
  Reduce el consumo de tokens entre un 40% y 65%, elimina ambigüedades lógicas,
  acelera la latencia de respuesta y mantiene salidas en lenguaje natural quirúrgico.
argument-hint: "[on|off|benchmark]"
license: MIT
---

# Code-as-Thought (CaT) & Micro-DSL Engine

Motor cognitivo determinista que reconfigura el espacio deliberativo interno de la IA (`thinking`)
para pensar exclusivamente mediante lógica formal, estructuras de datos y pipelines de ejecución.

## 1. Fundamentos Técnicos

1. **Eficiencia BPE / SentencePiece:** Operadores sintácticos (`->`, `:=`, `[]`, `assert`, `lambda`)
   consumen 1 solo token, eliminando conectores retóricos del lenguaje natural.
2. **Cero Ambigüedad:** El flujo de tipos y estados restringe el espacio de hipótesis a hechos reales.
3. **Validación Invariante:** Cada paso se valida con precondiciones y aserciones (`assert`) antes
   de la acción, previniendo alucinaciones y llamadas a herramientas erróneas.

## 2. Pipeline Canónico de Razonamiento (Micro-DSL)

Todo proceso deliberativo en `thinking` debe estructurarse obligatoriamente bajo este esquema:

```python
# 1. ESTADO ACTUAL (Facts & Grounding)
S = {
    "intent": user_request,
    "target": path_or_service,
    "observed": tool_output or error_trace
}

# 2. CAUSA RAÍZ & INVARIANTE (Deduction)
root = analyze(S["observed"])
assert root is not None, "Incomplete diagnostics"

# 3. ACCIÓN QUIRÚRGICA (Minimal Transform)
action = [
    plan_step for step in resolve(root)
    if is_minimal(step) and satisfies_ponytail(step)
]

# 4. ASERCIÓN / VALIDACIÓN SILENCIOSA (Quality Gate)
assert all(precondition(a) for a in action)

# 5. RESULTADO / SALIDA VISIBLE
out = emit_result(action, style="clean_fable_spanish")
```

## 3. Reglas de Inferencia

* **Prohibido el monólogo en lenguaje natural:** Nada de *"Veamos qué sucede si..."*, *"Primero analizaremos..."* o reflexiones conversacionales dentro del bloque de pensamiento.
* **Sesgo directo a herramientas:** Si falta un dato o estado empírico, invocar la herramienta inmediatamente en el paso 1 (`tool_first`).
* **Bimodalidad:** El pensamiento interno es 100% código/pseudocódigo compacto; la salida final al usuario es prosa en español estructurada, técnica y de alta claridad.
