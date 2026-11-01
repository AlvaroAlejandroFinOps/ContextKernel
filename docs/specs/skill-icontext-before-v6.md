---
name: icontext
description: >-
  Orquestador maestro universal del protocolo iContext Federation Protocol v5.0.
  Coordina de forma determinista y en un solo comando las 4 capas del ecosistema:
  L0 iDirectory (topología y satélite), L1 ThinkingSeed (ADN y 6 gates),
  L2 MetricsThinking (auditoría forense y FPIA espectral) y L3 iReadme (documentación dual Enterprise Paper-Grade).
  Permite reconciliación unificada (icontext reconcile), emisión de cápsulas quirúrgicas para subagentes
  (icontext capsule <450 tokens), paquetes de contexto (icontext pack), telemetría del bus (icontext status)
  y auto-sanación del ecosistema (icontext doctor). Se activa con /icontext.
---

# Workflow Maestro: iContext Federation Protocol v5.0 (`/icontext`)

> **Protocolo Universal de Control y Gobernanza de Context Engineering para Agentes Autónomos y Modelos de Lenguaje (LLMs)**  
> Creado por **Gravity HyperScale Thinking**.  
> **Centro de Mando:** `D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py`

---

## 🚀 Puntos de Entrada Principales

### 1. Reconciliación Unificada 1-Click (`icontext sync` / `icontext reconcile`)
Sincroniza, normaliza mayúsculas/minúsculas, verifica balizas, valida los 6 gates de ADN, ensambla documentación dual y sella satélites en el orden de precedencia estricto del protocolo:
```powershell
# En el repositorio actual (CWD):
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" sync

# En todo el ecosistema federado:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" sync --all
```

### 2. Inspección de Salud y Trazabilidad Temporal (`icontext status`)
Lectura ultrarrápida (< 500 ms) del estado vivo de las 4 capas en `.context/icontext_bus.json`, con timestamps de última reconciliación, frescura de satélite y enriquecimiento de beacons:
```powershell
# En el repositorio actual (CWD):
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" status

# En toda la federación:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" status --all
```

### 3. Cápsula Quirúrgica para Subagentes (`icontext capsule`)
Genera un payload JSON de ultra-alta densidad contextual (< 250 tokens) para delegar tareas a subagentes o workers sin fuga de ventana atencional ni escaneos ciegos:
```powershell
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" capsule --target <directorio> --task "<descripcion_tarea>"
```
*Contenido de la Cápsula:*
- Beacon del módulo resuelto por herencia (`role`, `prio`, `crawl`, `instructions`).
- Firmas AST públicas (`contracts_ast`) exclusivamente del módulo objetivo.
- Estado del checkpoint activo (`plan_id`, `phase`, `next_action`).
- Invariantes críticas de gobernanza (`[INV-01]`, `[INV-02]`, `[INV-08]`).

### 4. Paquete de Contexto Adaptativo (`icontext pack`)
Compila el subgrafo focalizado, archivos clave y telemetría según el perfil del bootloader:
```powershell
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" pack --target <directorio> --tier 1a
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" pack --target <directorio> --tier 1b
```

### 5. Auditoría Forense y Auto-Sanación (`audit_federation.py` / `icontext doctor`)
```powershell
# Auditoría forense del repositorio actual:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\audit_federation.py"

# Auditoría de los 4 repositorios del ecosistema:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\audit_federation.py" --all

# Auto-reparación de anomalías topológicas o satelitales:
python "D:\0001 HyperScale Thinking\PROYECTOS CLOUD\iContext\ContextControl\icontext.py" doctor
```

---

## 🛡️ Invariantes Fundamentales de la Federación v5.0

1. **[INV-01] Resiliencia NTFS I/O:** Toda mutación del bus `.context/icontext_bus.json` o satélites se realiza de forma atómica (`.tmp_{pid}_{tid}_{uuid}` + `os.replace`) con 10 reintentos exponenciales deterministas.
2. **[INV-02] Prohibición de Escaneo Ciego Recursivo:** Ningún agente ejecutará comandos masivos recursivos (`find .`, `Get-ChildItem -Recurse`, `ls -R`). Toda inspección debe guiarse por `icontext capsule`, `icontext pack` o `.context/tree.json`.
3. **[INV-08] Cero Fuga de Rutas Absolutas (Zero Path Leakage):** Prohibido emitir rutas con letras de unidad (`C:\`, `D:\`), esquemas locales (`file:///`) o directorios de usuario (`/home/`). Toda referencia debe ser estrictamente relativa a la raíz del repositorio (`./`).
