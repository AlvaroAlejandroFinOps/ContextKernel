# AGENTS.md: iContext Federation Protocol v5.0 Master Command Center

Este repositorio (**ContextControl**) es el **Centro de Mando Maestro y Nodo de Gobernanza Universal** del protocolo **iContext Federation Protocol v5.0** (diseñado por **Gravity HyperScale Thinking**). Coordina de forma determinista y transaccional las cuatro capas del ecosistema:

- **L0: iDirectory v5.0** — Plano de Control Topológico, Beacons Semánticos y Ruteo Canónico.
- **L1: ThinkingSeed v5.0** — Vector de ADN Arquitectónico Simbólico y Certificación de 6 Gates.
- **L2: MetricsThinking v5.0** — Auditoría Forense por Ground Truth, Eficiencia Espectral FPIA y Gobernanza de Planes.
- **L3: iReadme v5.0** — Síntesis de Documentación Dual Enterprise Paper-Grade v5.0.

---

## 🚀 Puntos de Entrada Maestros y CLI Global

Todo agente que opere en ContextControl o que necesite sincronizar la federación debe utilizar los motores centralizados de este directorio:

### 1. Orquestador Maestro de la Federación: `icontext.py` (`/icontext`)
- **Sincronización Transaccional Global (5 fases en los 4 repositorios):**
  ```powershell
  python icontext.py sync --all
  ```
- **Inspección de Salud y Trazabilidad en Tiempo Real:**
  ```powershell
  python icontext.py status --all
  ```
- **Cápsula Quirúrgica para Subagentes (<250 tokens):**
  ```powershell
  python icontext.py capsule --target <directorio> --task "<descripcion_tarea>"
  ```
- **Auto-Sanación de la Federación:**
  ```powershell
  python icontext.py doctor
  ```

### 2. Auditor Forense Global y Auto-Sanador: `audit_federation.py`
- **Auditoría Forense Integral de los 4 Proyectos:**
  ```powershell
  python audit_federation.py --all
  ```
- **Auto-Sanación Automática de Drift Satelital o Inconsistencias Topológicas:**
  ```powershell
  python audit_federation.py --fix
  ```

---

## 🛡️ Invariantes Críticas de Gobernanza

1. **[INV-01] Resiliencia NTFS I/O:** Toda escritura al bus `.context/icontext_bus.json` o mapas satelitales se realiza de manera atómica (`.tmp_{pid}_{tid}_{uuid}` + `os.replace`) con 10 reintentos exponenciales deterministas.
2. **[INV-02] Prohibición de Escaneo Ciego Recursivo:** Prohibido ejecutar búsquedas masivas sin filtro (`Get-ChildItem -Recurse`, `find .`, `ls -R`). Toda exploración debe conducirse mediante `icontext capsule`, `icontext pack` o el mapa satelital `.context/tree.json`.
3. **[INV-08] Cero Fuga de Rutas Absolutas (Zero Path Leakage):** Queda estrictamente prohibido incluir rutas con letras de unidad locales (`C:\`, `D:\`), esquemas URI locales (`file` scheme) o rutas de usuario (`/home/`). Toda ruta debe ser relativa a la raíz del repositorio (`./`).

---

## 📂 Estructura Canónica de ContextControl

- `icontext.py`: CLI maestro universal del protocolo v5.0.
- `audit_federation.py`: Auditor holístico multi-proyecto y motor de auto-reparación.
- `FWengine.py`: Motor de gobernanza y satélite topológico local.
- `ICONTEXT_FEDERATION_PROTOCOL_V5.md`: Especificación formal y matemática del protocolo federado v5.0.
- `01_seed/seed-contextcontrol-master.md`: ADN y vector arquitectónico de ContextControl.
- `.agents/skills/icontext/SKILL.md`: Especificación de la habilidad agéntica `/icontext`.
- `README.md` & `README_ES.md`: Documentación global de uso del ecosistema.
