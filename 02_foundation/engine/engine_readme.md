# CONTEXTCONTROL - iDirectory Architecture v5.0

Framework modular gobernado por **Gravity HyperScale Thinking** con Context Engineering nativo.

> **Protocolo de Ingesta para Agentes (Adaptive Bootloader v4.0):**
> 1. **Tier 1A (Atómico con ruta conocida):** `python FWengine.py context --pack <dir> --tier 1a` (< 220 tokens).
> 2. **Tier 1B (Multiarchivo / `/plan` acotado):** `python FWengine.py context --compact` + `map --slice <dir>` + `seed --section <id>`.
> 3. **Tier 2 (Arquitectura Global / Auditoría):** Lee `.context/tree.json` + `01_seed/seed-contextcontrol-master.md` solo en rediseño transversal o `/seedMaster`.
> 4. **Contrato de Cierre Unificado:** Tras crear carpetas o alterar la topología, ejecuta:
>    `python FWengine.py reconcile`

## Manifiesto de Directorios y Roles

- **`01_seed/`**: Semilla de proyecto y memoria técnica (ThinkingSeed Master). ADN arquitectónico del sistema. `[Priority: p0]`
- **`02_foundation/engine/`**: Núcleo del framework de automatización, lógica de ruteo, indexación y governance engine. `[Priority: p1]`
- **`03_research/notebooks/`**: Notebooks de desarrollo interactivo (Jupyter/Colab/Fabric/Databricks) para análisis exploratorio (EDA). `[Priority: p2]`
- **`03_research/prompts/`**: Estructuras de prompts para LLMs, system prompts, árboles de contexto y plantillas de inferencia. `[Priority: p1]`
- **`03_research/experiments/`**: Pruebas de concepto (PoCs), prototipos de modelos algorítmicos, benchmarks e I+D. `[Priority: p2]`
- **`src/cloud_jobs/`**: Scripts productivos, pipelines y orquestación multi-cloud (Fabric PySpark, AWS Glue, GCP Dataproc, Azure Synapse). `[Priority: p1]`
- **`src/data_generation/`**: Módulos de generación y simulación de datos sintéticos con rigor probabilístico y volumetría estadística. `[Priority: p2]`
- **`src/core/`**: Lógica de negocio transversal, utilitarios de backend, clientes de servicios y módulos comunes. `[Priority: p1]`
- **`src/dashboards/`**: Tableros de Business Intelligence y apps de visualización interactiva (Streamlit, Dash, PowerBI, Looker). `[Priority: p2]`
- **`artifacts/plans/active/`**: Planes de capacidad activos (F-SKUs), presupuestos cloud vigentes e hitos operativos en curso. `[Priority: p1]`
- **`artifacts/plans/metricsthinking/`**: Evaluación forense de métricas de avance del proyecto, scores de madurez y roadmap de remediación SDD (MetricsThinking™). `[Priority: p2]`
- **`artifacts/plans/backlog/`**: Cola formal de intenciones, backlog de tareas y planes candidatos de ejecución. `[Priority: p2]`
- **`artifacts/plans/archive/`**: Histórico de planes evaluados, arquitecturas descartadas y documentación obsoleta preservada por trazabilidad. `[Priority: p3]`
- **`docs/architecture/`**: Diagramas de arquitectura multi-cloud, topologías C4 y flujos de datos de las capas Medallion. `[Priority: p1]`
- **`docs/specs/`**: Especificaciones técnicas detalladas, linaje de datos, contratos de esquemas y requerimientos no funcionales. `[Priority: p1]`
- **`docs/notes/`**: Bitácoras de ingeniería, registro de deuda técnica, decisiones rápidas (ADRs) y análisis de causa raíz (RCA). `[Priority: p2]`
- **`config/`**: Parámetros de entorno (dev, staging, prod), políticas de contexto y variables desacopladas. `[Priority: p1]`
- **`data/raw/`**: Zona de aterrizaje local (Bronze) para fuentes puras e inmutables. Ignorado en Git y AI. `[Priority: p3]`
- **`data/processed/`**: Datos transformados localmente (Silver/Gold) en formatos estructurados (Parquet/Delta). `[Priority: p3]`
- **`data/sandbox/`**: Entorno aislado para experimentación de científicos de datos y arquitectos. `[Priority: p3]`
- **`schemas/`**: Definiciones estrictas de esquemas (Avro, JSON Schema, DDL de SQL) para control de deriva de datos. `[Priority: p1]`
- **`scripts/`**: Scripts operativos del sistema operativo (bash, powershell, make) para tareas de mantenimiento. `[Priority: p2]`
- **`tests/`**: Suites de pruebas unitarias, integración y calidad de datos (Great Expectations / pytest). `[Priority: p1]`
- **`tools/`**: Scripts utilitarios internos, herramientas de automatización local y linters. `[Priority: p2]`
- **`logs/`**: Trazas locales de ejecución, auditorías y dumps de errores. `[Priority: p3]`
- **`.context/`**: Directorio de telemetría, checkpoints y mapas satelitales de Context Engineering de iDirectory. `[Priority: p0]`
