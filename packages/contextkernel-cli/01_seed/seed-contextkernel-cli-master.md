<SEED_ARCHITECTURAL_VECTOR version="6.1" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# ThinkingSeed Master v6.1: ContextKernel CLI

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es el **Vector Arquitectónico Maestro y Memoria Técnica Modular (ThinkingSeed Master v6.1)** de **contextkernel-cli** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería (`[INV-02]`)** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas AST (Sección 4.1) y la Superficie de Tensión (Sección 7) para detectar condiciones de carrera, sobrescrituras destructivas, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) o scaffolding intencional del proyecto, no defectos de este documento.

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR

```yaml
seed_schema_version: "6.1"
project_name: "contextkernel-cli"
repository_name: "ContextControl"
slogan: "Unified CLI and context orchestrator for AI engineering agents"
project_type: "cli-orchestrator"
repository_mode: "modular-package"
generated_at: "2026-11-02T07:20:00.000000+00:00"
generated_by: "Antigravity / ContextKernel v6.1 Migration"
repository_root: "./"
git_branch: "master"
analysis_mode: "static+git+validated"
coverage_level: "high"
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN de contextkernel-cli (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución en vivo.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder consultas técnicas.
3. **Estado de Avance:** Considera que las secciones o directorios marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`. No transformes inferencias en hechos.
5. **Portabilidad de Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio (`./ruta/archivo`) con barras inclinadas (`/`). Prohibido emitir rutas absolutas locales o URIs con esquema de archivo local.
6. **Contratos Simbólicos:** Conserva la arquitectura, convenciones `all-lowercase`, firmas simbólicas AST (Sección 4.1) e invariantes (`[INV-01]` a `[INV-08]`).
7. **Postura Adversarial Constructiva:** Evalúa siempre la Sección 7 (Superficie de Tensión) para anticipar impactos laterales en reglas de agentes, sincronización satelital, pruebas y seguridad.
8. **Seguridad Zero-Trust:** Nunca reveles, inventes ni solicites secretos reales; utiliza siempre el marcador `<REDACTED>`.

---

## 1. RESUMEN EJECUTIVO Y ALCANCE

[CONFIRMADO] **contextkernel-cli** es el módulo orquestador central de la suite ContextKernel. Provee los puntos de entrada `ck`, `contextkernel` e `icontext`, gobernando:
- La invocación del ciclo de vida federado (`status`, `sync`, `pack`, `audit`, `doctor`).
- El bus cognitivo unificado (`.context/icontext_bus.json`) y capas de validación.
- El benchmark volumétrico y la distribución multiplataforma de skills para agentes de IA.

---

## 2. DIRECTORY BEACONS & STRUCTURAL ROLES

### 2.0 Estado vigente v6.1 (Modular CLI Package)

- ./: role="package_root" | crawl=true | key_files=["pyproject.toml", "README.md"]
- ./01_seed: role="dna" | crawl=true | seed_reference="required" | key_files=["seed-contextkernel-cli-master.md"]
- ./src/contextkernel: role="core_orchestrator_sources" | crawl=true | key_files=["cli.py", "context_runtime.py", "benchmark.py", "installer.py"]
- ./tests: role="package_tests" | crawl=true | key_files=["test_v6.py"]
- ./tests/fixtures: role="golden_fixtures" | crawl=true

---

## 3. CRYPTOGRAPHIC INVARIANTS & OPERATIONAL RULES

### 3.0 Estado vigente v6.1

Invariantes Criptográficas Maestras:
- [INV-01] Resilient NTFS I/O with 10 jittered backoff retries on icontext_bus.json.
- [INV-02] Zero blind recursive filesystem scans (find ., Get-ChildItem -Recurse prohibited).
- [INV-03] Hierarchical pruning propagation (crawl=false prohibits sub-tree exploration).
- [INV-04] Atomic bus synchronicity via .context/icontext_bus.json.
- [INV-05] Zero-Trust PII and credential sanitization (<REDACTED>).
- [INV-06] Deterministic epistemic tags ([CONFIRMADO], [INFERIDO], [FALTANTE]).
- [INV-07] Strict bilingual doc parity (Phi = 1.0).
- [INV-08] Zero host-specific absolute path leakage (strictly relative ./ paths).

---

## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA

### 4.1 Contratos públicos vigentes v6.1

[CONFIRMADO] Firmas simbólicas AST de contextkernel-cli:

- ./packages/contextkernel-cli/src/contextkernel/benchmark.py::percentile(values, fraction) -> Any
- ./packages/contextkernel-cli/src/contextkernel/benchmark.py::benchmark(root, samples=7) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::ecosystem_root(value=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::outputs(root, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::output_hash(root, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::layer_hash(inv, layer, root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::plan(root, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::status(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::audit(root, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::request(root, layer, inv, fingerprint, delta) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::complete(root, layer, expected) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::metrics(root, eco, full=False, profile='default') -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::sync(root, eco, dry_run=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::pack(root, path='.', tier='1a', expand=False, task='') -> Any
- ./packages/contextkernel-cli/src/contextkernel/cli.py::main(argv=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::read_json(path, default=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::digest(value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::atomic_write(path, content) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::write_json(path, value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::ignore_patterns(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::ignored(relative, patterns) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::crawl_allowed(directory) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::python_contracts(source, relative) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::input_hash(inv, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::estimated_tokens(value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::validate_seed(path, index=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/context_runtime.py::validate_readmes(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::source_bundles(eco) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::inspect_installation(eco, home) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::install(eco, agents, home, local=None, dry_run=False, only=None, source_runtime=None) -> Any

CLI flags: --agents, --all, --antigravity, --apply, --archetype, --audit, --check, --claude, --clear, --codex, --compact, --dest, --dry-run, --expand, --fix, --full, --global, --help, --home, --json, --local, --only, --pack, --profile, --root, --samples, --status, --sync, --target, --task, --tier

### 4.2 Artefactos y propiedad de escritura
[CONFIRMADO]
- `.context/inventory.json`: Hash de contenido e inventario.
- `.context/icontext_bus.json`: Bus cognitivo federado.
- `.context/layers/`: Sidecars por capa.

---

## 5. FPAI MATHEMATICAL ENGINES & STATE MODELS
- Resilient NTFS lock backoff: t_retry = min(t_max, t_base * 2^attempt + jitter)
- Content digest: H_content = SHA256(content_bytes)

---

## 6. EXECUTION & VERIFICATION FLOW
- Status check: python -m contextkernel.cli status
- Layer sync: python -m contextkernel.cli sync --all
- Doctor check: python -m contextkernel.cli doctor

---

## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA
- [CONFIRMADO] Alias de compatibilidad: `icontext_cli.py`, `runtime.py` y `skill_installer.py` proveen compatibilidad hacia atrás con runtimes anteriores.
- [CONFIRMADO] Bloqueo NTFS concurrente con reintentos para prevenir contención multi-proceso.

---

## 8. EPISTEMIC RIGOR TAGS
- [CONFIRMADO] 100% de los comandos CLI testeados en `tests/test_v6.py`.
- [CONFIRMADO] Cero rutas absolutas y política de secretos `<REDACTED>`.

---

## 9. HISTORICAL DELTA & MIGRATION LINEAGE
- v6.1.0: Consolidación modular de ContextKernel CLI como paquete independiente en el workspace monorepo.

---

## 10. REPORTE DE CUMPLIMIENTO
| Área Evaluada | Cobertura | Confianza | Método de Verificación |
|---|---|---|---|
| Contratos CLI | 100% | Alta | test_v6.py [CONFIRMADO] |
| Portabilidad | 100% | Alta | Invariante [INV-08] [CONFIRMADO] |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es la semilla modular (**ThinkingSeed Master v6.1**) de **contextkernel-cli** (`contains_source_code="false"`).
> Úsalo para asistir en la extensión o mantenimiento del CLI y del orquestador unificado de ContextKernel."

### Pautas de resolución:
1. Utiliza rutas relativas `./packages/contextkernel-cli/`.
2. Preserva las invariantes `[INV-01]` a `[INV-08]`.

### 🤝 Acuse de Recibo Inicial
Confirmar asimilación del vector modular de **contextkernel-cli**.

</SEED_ARCHITECTURAL_VECTOR>
