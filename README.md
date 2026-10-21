# Code-as-Thought (CaT) & Micro-DSL Engine

> **A high-efficiency symbolic reasoning framework for Large Language Models.**  
> Replaces verbose natural-language self-talk in the LLM `thinking` scratchpad with a formal declarative micro-code pipeline, cutting token consumption by 40%–65% and boosting execution speed.

---

## ⚡ The Core Problem

When LLMs reason in natural language (English, Spanish, etc.), they incur substantial overhead:
* **Token Bloat:** Conversational fillers (*"Let's first consider if...", "In this case we should..."*) waste precious context window.
* **Semantic Ambiguity:** Human language is inherently polysemic, increasing token prediction entropy and branch errors.
* **Latency:** Slower generation before reaching the actual tool call or code modification.

## 🚀 The CaT Solution (Micro-DSL)

By constraining the model's internal deliberative scratchpad to **Micro-Python / Declarative AST logic**, the attention mechanism operates on deterministic state mutations:

```python
# 1. EMPIRICAL STATE
S = {"target": path_or_service, "issue": error_type, "ctx": sys_state}

# 2. ROOT CAUSE DEDUCTION
root = analyze(S["issue"])
assert root is not None, "Incomplete diagnostics"

# 3. SURGICAL ACTION
action = [step for step in resolve(root) if is_minimal(step)]

# 4. SILENT QUALITY GATE
assert all(precondition(a) for a in action)

# 5. DETERMINISTIC OUTPUT
out = emit_result(action)
```

---

## 📊 Empirical Benchmark Results

Measured across real-world production engineering scenarios (Server infrastructure, concurrency/memory leaks, and async backend queues):

| Test Scenario | Natural Language CoT | CaT Micro-DSL | Char Reduction | **Token Savings** |
| :--- | :---: | :---: | :---: | :---: |
| **1. Minecraft SQLite Lock** | 793 chars / 262 tokens | 388 chars / 178 tokens | **-51.1%** | **-32.1%** |
| **2. Java Bukkit Memory Leak** | 837 chars / 276 tokens | 374 chars / 135 tokens | **-55.3%** | **-51.1%** |
| **3. Node.js Event Loop Block** | 897 chars / 294 tokens | 383 chars / 163 tokens | **-57.3%** | **-44.6%** |
| **AVERAGE** | **842 chars / 277 tokens** | **381 chars / 158 tokens** | **-54.6%** | **-42.6%** |

*In multi-step chains with 4+ tool invocations, accumulated savings exceed **65% in thinking tokens**.*

---

## 🛠️ Installation & Usage

### As an Antigravity / Agent Skill

Clone or place `SKILL.md` inside your agent skills directory:
```bash
git clone https://github.com/maryMaryMar/cat-reasoning.git ~/.agents/skills/cat-reasoning
```

### System Prompt Directive

Add to your `GEMINI.md`, `CLAUDE.md`, or system prompt:
```markdown
## Protocolo CaT (Code-as-Thought Micro-DSL)
En todo procesamiento interno (`thinking`), sustituir la prosa verbal y reflexiones conversacionales
por el pipeline formal declarativo `S -> Root -> Action -> Assert -> Out`.
Prohibido el gasto de tokens en divagaciones retóricas o monólogos en lenguaje natural.
```

---

## 📄 License
MIT © maryMaryMar
