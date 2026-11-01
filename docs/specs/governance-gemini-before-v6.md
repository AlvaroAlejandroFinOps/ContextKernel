# Reglas de Gobernanza Antigravity / Gemini: Centro de Mando ContextControl (v5.0)

Este repositorio es el nodo de orquestación central de la federación **iContext v5.0** (diseñado por **Gravity HyperScale Thinking**). Establece las directivas de ejecución para asistentes basados en Gemini y Google Antigravity.

---

## ⚡ Directivas de Ejecución Rápida (`/icontext`)

Para cualquier operación sobre el ecosistema iContext, prioriza las herramientas maestras alojadas en este repositorio:

1. **Sincronización y Reconciliación Global:**
   ```powershell
   python icontext.py sync --all
   ```
2. **Diagnóstico Holístico del Ecosistema:**
   ```powershell
   python audit_federation.py --all
   ```
3. **Auto-Sanación de Inconsistencias:**
   ```powershell
   python audit_federation.py --fix
   ```
4. **Cápsula de Mínimo Contexto para Subagentes (<250 tokens):**
   ```powershell
   python icontext.py capsule --target <dir> --task "<tarea>"
   ```

---

## 🛡️ Reglas de Operación Estricta

1. **Prioridad del Bus Federado:** Antes de inspeccionar código en otros repositorios, consulta el bus `.context/icontext_bus.json` o ejecuta `python icontext.py status --all` para conocer el estado y mtimes de cada capa.
2. **Cero Rutas Absolutas:** Prohibido emitir enlaces con unidades `C:` o `D:` o esquemas URI locales (`file` scheme).
3. **Poda Atencional:** Nunca leas directorios podados (`data/`, `logs/`, `artifacts/plans/archive/`).
