<SEED_ARCHITECTURAL_VECTOR version="6.1" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# ThinkingSeed Master v6.1: ContextKernel

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es el **Vector Arquitectónico Maestro y Memoria Técnica (ThinkingSeed Master v6.1)** de **ContextKernel** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería (`[INV-02]`)** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas AST (Sección 4.1) y la Superficie de Tensión (Sección 7) para detectar condiciones de carrera, sobrescrituras destructivas, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) o scaffolding intencional del proyecto, no defectos de este documento.

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR

```yaml
seed_schema_version: "6.1"
project_name: "ContextKernel"
repository_name: "ContextControl"
slogan: "ContextKernel is a context and attention control plane for AI engineering agents"
project_type: "monorepo-context-control-plane"
repository_mode: "modular-monorepo-workspace"
generated_at: "2026-11-01T20:40:00.000000+00:00"
generated_by: "Antigravity / ContextKernel v6.1 Migration"
repository_root: "./"
git_branch: "master"
analysis_mode: "static+git+validated"
coverage_level: "high"
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN de ContextKernel (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución en vivo.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder consultas técnicas.
3. **Estado de Avance:** Considera que las secciones o directorios marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`. No transformes inferencias en hechos.
5. **Portabilidad de Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio (`./ruta/archivo`) con barras inclinadas (`/`). Prohibido emitir rutas absolutas locales o URIs con esquema de archivo local.
6. **Contratos Simbólicos:** Conserva la arquitectura, convenciones `all-lowercase`, firmas simbólicas AST (Sección 4.1) e invariantes (`[INV-01]` a `[INV-08]`).
7. **Postura Adversarial Constructiva:** Evalúa siempre la Sección 7 (Superficie de Tensión) para anticipar impactos laterales en reglas de agentes, sincronización satelital, pruebas y seguridad.
8. **Seguridad Zero-Trust:** Nunca reveles, inventes ni solicites secretos reales; utiliza siempre el marcador `<REDACTED>`.

---

## 1. RESUMEN EJECUTIVO Y ALCANCE

[CONFIRMADO] **ContextKernel** es el plano de control de contexto y atención para agentes de ingeniería de Inteligencia Artificial ("ContextKernel is a context and attention control plane for AI engineering agents"). Opera como un monorepo modular de alta ingeniería que consolida cuatro capas federadas y un núcleo CLI orquestador:
- `packages/idirectory/` (Capa L0: Topología, Beacons y AST Contracts)
- `packages/thinkingseed/` (Capa L1: ADN Arquitectónico Simbólico y Validador de 6 Gates)
- `packages/metricsthinking/` (Capa L2: Auditoría Forense y FPIA Espectral con Backend Rust)
- `packages/ireadme/` (Capa L3: Sintetizador Documental Paper-Grade y Paridad Bilingüe)
- `packages/contextkernel-cli/` (CLI unificado, Runtime, Installer y Benchmark)

[CONFIRMADO] El Protocolo de Control de Contexto Federado (FCCP v6.1) coordina el flujo de evidencia y redacción asistida entre capas a través del bus cognitivo `.context/icontext_bus.json` bajo transacciones atómicas con bloqueo NTFS resiliente (`repository_lock`).

---

## 2. DIRECTORY BEACONS & STRUCTURAL ROLES

### 2.0 Estado vigente v6.1 (Monorepo Workspace)

[CONFIRMADO] En v6.1, la raíz gobierna el workspace unificado mientras que cada módulo conserva su propio SeedMaster en `01_seed/` para aislamiento cognitivo y correcciones quirúrgicas con ahorro de más del 95% de tokens.

Nodos Canónicos del Árbol Satelital (.context/tree.json):
- ./.context: role="context_engineering" | prio="p0" | crawl=true | key_files=["tree.json", "icontext_bus.json", "contracts_ast.json"]
- ./01_seed: role="dna" | prio="p0" | crawl=true | seed_ref="required" | key_files=["seed-contextkernel-master.md", "seed-contextkernel-hybrid.md"]
- ./02_foundation/engine: role="core_engine" | prio="p1" | crawl=true | key_files=["engine_readme.md"]
- ./03_research/notebooks: role="eda" | prio="p2" | crawl=false
- ./03_research/prompts: role="prompt_engineering" | prio="p1" | crawl=true
- ./03_research/experiments: role="pocs_benchmarks" | prio="p2" | crawl=false
- ./src/cloud_jobs: role="production_pipelines" | prio="p1" | crawl=true
- ./src/data_generation: role="synthetic_data" | prio="p2" | crawl=true
- ./src/core: role="shared_backend" | prio="p1" | crawl=true
- ./src/dashboards: role="bi_viz" | prio="p2" | crawl=true
- ./artifacts/plans/active: role="active_plans" | prio="p1" | crawl=true
- ./artifacts/plans/metricsthinking: role="metrics_evaluation" | prio="p2" | crawl=true | key_files=["MetricsThinking.md", "MetricsThinking.json"]
- ./artifacts/plans/backlog: role="intent_backlog" | prio="p2" | crawl=false
- ./artifacts/plans/archive: role="archived_plans" | prio="p3" | crawl=false
- ./docs/architecture: role="architecture_diagrams" | prio="p1" | crawl=true
- ./docs/specs: role="technical_specs" | prio="p1" | crawl=true
- ./docs/notes: role="engineers_notes" | prio="p2" | crawl=true
- ./config: role="configuration" | prio="p1" | crawl=true | key_files=["context_policy.json"]
- ./data/raw: role="bronze_storage" | prio="p3" | crawl=false
- ./data/processed: role="silver_gold_storage" | prio="p3" | crawl=false
- ./data/sandbox: role="sandbox" | prio="p3" | crawl=false
- ./schemas: role="data_contracts" | prio="p1" | crawl=true
- ./scripts: role="ops_automation" | prio="p2" | crawl=true
- ./tests: role="test_suites" | prio="p1" | crawl=true
- ./tools: role="tooling" | prio="p2" | crawl=true
- ./logs: role="logs" | prio="p3" | crawl=false
- ./packages: role="namespace" | prio="p1" | crawl=true
- ./skills: role="domain_extension" | prio="p1" | crawl=true

Ecosistema Modular Federado (packages/):
- ./packages/idirectory: role="l0_topological_governor" | seed="seed-idirectory-master.md"
- ./packages/thinkingseed: role="l1_architectural_dna" | seed="seed-thinkingseed-master.md"
- ./packages/metricsthinking: role="l2_forensic_auditor" | seed="seed-metricsthinking-master.md"
- ./packages/ireadme: role="l3_paper_grade_synthesizer" | seed="seed-ireadme-master.md"
- ./packages/contextkernel-cli: role="core_orchestrator" | seed="seed-contextkernel-cli-master.md" 

---

## 3. CRYPTOGRAPHIC INVARIANTS & OPERATIONAL RULES

### 3.0 Estado vigente v6.1

[CONFIRMADO] El flujo FCCP v6.1 coordina 5 fases deterministas:
1. L0 (iDirectory): Invariante de topología física, beacons y cálculo de AST contracts.
2. L1 (ThinkingSeed): Evaluación de los 6 gates deterministas de memoria arquitectónica.
3. L2 (MetricsThinking): Auditoría forense M01-M10, FPIA espectral y escaneo Zero-Trust PII.
4. L3 (iReadme): Inyección de telemetría forense en documentación dual con paridad Phi = 1.0.
5. Sincronización del Bus: Persistencia transaccional de sidecars en `.context/layers/`.

Invariantes Criptográficas Maestras:
- [INV-01] Resilient NTFS I/O with 10 jittered backoff retries on icontext_bus.json.
- [INV-02] Zero blind recursive filesystem scans (find ., Get-ChildItem -Recurse prohibited).
- [INV-03] Hierarchical pruning propagation (crawl=false prohibits sub-tree exploration).
- [INV-04] Atomic cognitive bus synchronization via .context/icontext_bus.json and repository_lock.
- [INV-05] Zero-Trust PII and credential sanitization (mandatory <REDACTED> tags).
- [INV-06] Deterministic epistemic tags ([CONFIRMADO], [INFERIDO], [DECLARADO], [FALTANTE]).
- [INV-07] Strict bilingual documentation parity (Phi = 1.0) and Golden invariant.
- [INV-08] Zero host-specific absolute path leakage (strictly relative ./ paths).

---

## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA

### 4.1 Contratos públicos vigentes v6.1

[CONFIRMADO] Firmas simbólicas extraídas de módulos activos del monorepo ContextKernel:

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
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::ecosystem_root(value=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::outputs(root, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::output_hash(root, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::layer_hash(inv, layer, root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::plan(root, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::status(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::audit(root, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::request(root, layer, inv, fingerprint, delta) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::complete(root, layer, expected) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::metrics(root, eco, full=False, profile='default') -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::sync(root, eco, dry_run=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::pack(root, path='.', tier='1a', expand=False, task='') -> Any
- ./packages/contextkernel-cli/src/contextkernel/icontext_cli.py::main(argv=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::source_bundles(eco) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::inspect_installation(eco, home) -> Any
- ./packages/contextkernel-cli/src/contextkernel/installer.py::install(eco, agents, home, local=None, dry_run=False, only=None, source_runtime=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::read_json(path, default=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::digest(value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::atomic_write(path, content) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::write_json(path, value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::ignore_patterns(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::ignored(relative, patterns) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::crawl_allowed(directory) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::python_contracts(source, relative) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::input_hash(inv, layer) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::estimated_tokens(value) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::validate_seed(path, index=None) -> Any
- ./packages/contextkernel-cli/src/contextkernel/runtime.py::validate_readmes(root) -> Any
- ./packages/contextkernel-cli/src/contextkernel/skill_installer.py::source_bundles(eco) -> Any
- ./packages/contextkernel-cli/src/contextkernel/skill_installer.py::inspect_installation(eco, home) -> Any
- ./packages/contextkernel-cli/src/contextkernel/skill_installer.py::install(eco, agents, home, local=None, dry_run=False, only=None, source_runtime=None) -> Any
- ./packages/idirectory/skills/v6/idir/scripts/run.py::matches_version(path) -> Any
- ./packages/idirectory/src/core/context_runtime.py::read_json(path, default=None) -> Any
- ./packages/idirectory/src/core/context_runtime.py::digest(value) -> Any
- ./packages/idirectory/src/core/context_runtime.py::atomic_write(path, content) -> Any
- ./packages/idirectory/src/core/context_runtime.py::write_json(path, value) -> Any
- ./packages/idirectory/src/core/context_runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/idirectory/src/core/context_runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/idirectory/src/core/context_runtime.py::ignore_patterns(root) -> Any
- ./packages/idirectory/src/core/context_runtime.py::ignored(relative, patterns) -> Any
- ./packages/idirectory/src/core/context_runtime.py::crawl_allowed(directory) -> Any
- ./packages/idirectory/src/core/context_runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/idirectory/src/core/context_runtime.py::python_contracts(source, relative) -> Any
- ./packages/idirectory/src/core/context_runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/idirectory/src/core/context_runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/idirectory/src/core/context_runtime.py::input_hash(inv, layer) -> Any
- ./packages/idirectory/src/core/context_runtime.py::estimated_tokens(value) -> Any
- ./packages/idirectory/src/core/context_runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/idirectory/src/core/context_runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/idirectory/src/core/context_runtime.py::validate_seed(path, index=None) -> Any
- ./packages/idirectory/src/core/context_runtime.py::validate_readmes(root) -> Any
- ./packages/idirectory/src/core/fwengine.py::MiniYAML(class)
- ./packages/idirectory/src/core/fwengine.py::safe_io_retry(operation: Callable[[], Any], max_attempts: int=4, initial_delay_ms: float=25.0) -> Any
- ./packages/idirectory/src/core/fwengine.py::safe_rename_casing(src: Path, dest: Path) -> Path
- ./packages/idirectory/src/core/fwengine.py::estimate_tokens_v4(text_or_path: Any, fast_stat_only: bool=False) -> int
- ./packages/idirectory/src/core/fwengine.py::resolve_seed_key_files(root_path: Path) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::generate_beacon_content(folder: str, meta: Dict[str, Any], root_path: Optional[Path]=None) -> str
- ./packages/idirectory/src/core/fwengine.py::resolve_beacon(dir_path: Path, root_path: Path) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::extract_preserved_comments(beacon_file: Path) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::validate_beacon_data(data: Dict[str, Any]) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::validate_tree_data(data: Dict[str, Any]) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::validate_backlog_data(data: Dict[str, Any]) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::validate_backlog_queue(root_path: Path, check_only: bool=False) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::load_ignore_patterns(root_path: Path) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::is_ignored_path(dir_path: Path, root_path: Path, patterns: Optional[List[str]]=None) -> bool
- ./packages/idirectory/src/core/fwengine.py::discover_unbeaconed_directories(root_path: Path) -> List[Path]
- ./packages/idirectory/src/core/fwengine.py::infer_beacon_meta(dir_path: Path, root_path: Path) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::scaffold_beacon_for_dir(dir_path: Path, root_path: Path, overwrite: bool=False) -> Optional[Path]
- ./packages/idirectory/src/core/fwengine.py::ensure_beacon_chain(target_dir: Path, root_path: Path) -> List[Path]
- ./packages/idirectory/src/core/fwengine.py::iter_beacon_files(root_path: Path) -> List[Path]
- ./packages/idirectory/src/core/fwengine.py::sync_beacons(root_path: Path, auto_discover: bool=True, force_defaults: bool=False) -> int
- ./packages/idirectory/src/core/fwengine.py::compute_topology_hash(root_path: Path) -> str
- ./packages/idirectory/src/core/fwengine.py::compute_node_fingerprint(dir_path: Path) -> str
- ./packages/idirectory/src/core/fwengine.py::generate_tree_json(root_path: Path) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::check_satellite_freshness(root_path: Path) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::format_compact_tree_json(data: Dict[str, Any]) -> str
- ./packages/idirectory/src/core/fwengine.py::sync_tree(root_path: Path) -> Path
- ./packages/idirectory/src/core/fwengine.py::generate_sliced_tree(root_path: Path, target_path: str, radius: int=1, max_children: int=6) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::format_sliced_tree(data: Dict[str, Any]) -> str
- ./packages/idirectory/src/core/fwengine.py::build_context_pack(root_path: Path, target_path: str, tier: str='1a', expand: bool=False) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::build_context_capsule(root_path: Path, target_path: str, task_description: str='') -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::get_seed_sections(root_path: Path) -> List[Dict[str, Any]]
- ./packages/idirectory/src/core/fwengine.py::extract_seed_section(root_path: Path, query: str) -> str
- ./packages/idirectory/src/core/fwengine.py::manage_checkpoint(root_path: Path, action='show', plan_id=None, status=None, phase=None, next_action=None, completed_step=None, session_id=None, objective=None, constraints=None, decisions=None, evidence_hash=None, expires_at=None) -> Any
- ./packages/idirectory/src/core/fwengine.py::build_ast_contracts_index(root_path: Path, write_to_disk: bool=True) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::sync_icontext_bus(root_path: Path, tree_data=None, ast_index=None, write_to_disk=True) -> Any
- ./packages/idirectory/src/core/fwengine.py::build_ecosystem_pack(root_path: Path, expand: bool=False) -> Dict[str, Any]
- ./packages/idirectory/src/core/fwengine.py::upsert_segmented_block(file_path: Path, tool_key: str, block_content: str) -> bool
- ./packages/idirectory/src/core/fwengine.py::compute_context_budget(root_path: Path, include_pruned_stats: bool=False) -> List[Dict[str, Any]]
- ./packages/idirectory/src/core/fwengine.py::init_project(base_path: str) -> Any
- ./packages/idirectory/src/core/fwengine.py::inspect_python_header(file_path: Path, max_chars: int=4096) -> str
- ./packages/idirectory/src/core/fwengine.py::route_file(file_path: str, base_path: str='.', move: bool=False, overwrite: bool=False) -> Optional[Path]
- ./packages/idirectory/src/core/fwengine.py::reconcile_plans_lifecycle(root_path: Path, check_only: bool=False) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::validate_dependency_dag(root_path: Path, changed_nodes: Optional[List[str]]=None) -> List[str]
- ./packages/idirectory/src/core/fwengine.py::audit_repository(root_path: Path, fix: bool=False) -> bool
- ./packages/idirectory/src/core/fwengine.py::reconcile_repository(root_path: Path, check_only: bool=False) -> bool
- ./packages/idirectory/src/core/fwengine.py::main() -> Any
- ./packages/idirectory/tools/build_runtime.py::put(path, raw, check=False) -> Any
- ./packages/idirectory/tools/build_runtime.py::build(check=False) -> Any
- ./packages/ireadme/scripts/init_readme.py::atomic_write_text(file_path: Path, content: str, encoding: str='utf-8') -> None
- ./packages/ireadme/scripts/init_readme.py::generate_readmes(root_dir: Path=ROOT_DIR, update_golden: bool=False) -> Any
- ./packages/ireadme/scripts/install_skill.py::get_home_dir() -> Path
- ./packages/ireadme/scripts/install_skill.py::install_to_antigravity() -> bool
- ./packages/ireadme/scripts/install_skill.py::install_to_codex() -> bool
- ./packages/ireadme/scripts/install_skill.py::install_to_claude() -> bool
- ./packages/ireadme/scripts/install_skill.py::install_to_directory(dest_path: Path) -> bool
- ./packages/ireadme/scripts/install_skill.py::main() -> Any
- ./packages/ireadme/src/ireadme/generator.py::detect_icontext_layers(repo_path: Path) -> Dict[str, Dict[str, Any]]
- ./packages/ireadme/src/ireadme/generator.py::render_badges_block(layers: Dict[str, Dict[str, Any]], custom_badges: Optional[List[str]]=None) -> str
- ./packages/ireadme/src/ireadme/generator.py::render_federation_section(layers: Dict[str, Dict[str, Any]], lang: str='en') -> str
- ./packages/ireadme/src/ireadme/generator.py::atomic_write_text(target: Path, content: str, encoding: str='utf-8') -> None
- ./packages/ireadme/src/ireadme/generator.py::extract_project_metadata(repo_path: Path) -> Dict[str, Any]
- ./packages/ireadme/src/ireadme/generator.py::generate_universal_readmes(repo_path: Path, write_to_disk: bool=True, update_golden: bool=False) -> Tuple[str, str]
- ./packages/ireadme/src/ireadme/generator.py::main() -> Any
- ./packages/ireadme/src/ireadme/runtime.py::read_json(path, default=None) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::digest(value) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::atomic_write(path, content) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::write_json(path, value) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::ignore_patterns(root) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::ignored(relative, patterns) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::crawl_allowed(directory) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::python_contracts(source, relative) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::input_hash(inv, layer) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::estimated_tokens(value) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::validate_seed(path, index=None) -> Any
- ./packages/ireadme/src/ireadme/runtime.py::validate_readmes(root) -> Any
- ./packages/metricsthinking/scripts/hnsw_index_rebuild.py::rebuild_hnsw_index(index_dir: str, compact: bool=True, dry_run: bool=False) -> dict[str, int]
- ./packages/metricsthinking/scripts/hnsw_index_rebuild.py::main() -> Any
- ./packages/metricsthinking/scripts/install_skill.py::get_user_home() -> Path
- ./packages/metricsthinking/scripts/install_skill.py::install_antigravity(dest_root: Path, is_global: bool=False, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::install_codex(dest_root: Path, is_global: bool=False, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::install_claude(dest_root: Path, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::install_cursor(dest_root: Path, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::install_copilot(dest_root: Path, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::install_mcp_config(dest_root: Path, dry_run: bool=False) -> list[Path]
- ./packages/metricsthinking/scripts/install_skill.py::run_installer(target: str='all', dest: str='.', is_global: bool=False, dry_run: bool=False) -> Any
- ./packages/metricsthinking/scripts/install_skill.py::main() -> Any
- ./packages/metricsthinking/scripts/run_benchmark.py::main() -> Any
- ./packages/metricsthinking/src/metricsthinking/backends/__init__.py::get_active_backend() -> str
- ./packages/metricsthinking/src/metricsthinking/backends/__init__.py::scan_directory(path, ignore_patterns=None, include_content=True, cache_path=None, persist=False, full=False) -> Any
- ./packages/metricsthinking/src/metricsthinking/backends/__init__.py::fast_shannon_entropy(data: str) -> float
- ./packages/metricsthinking/src/metricsthinking/backends/__init__.py::calculate_shingling_jaccard(a: str, b: str, k: int=3) -> float
- ./packages/metricsthinking/src/metricsthinking/backends/__init__.py::compute_ast_coupling(python_files: dict[str, str]) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/backends/python_fallback.py::fast_shannon_entropy(data: str) -> float
- ./packages/metricsthinking/src/metricsthinking/backends/python_fallback.py::calculate_shingling_jaccard(a: str, b: str, k: int=3) -> float
- ./packages/metricsthinking/src/metricsthinking/backends/python_fallback.py::scan_directory(path, ignore_patterns=None, include_content=True, cache_path=None, persist=False, full=False) -> Any
- ./packages/metricsthinking/src/metricsthinking/backends/python_fallback.py::compute_ast_coupling(python_files: dict[str, str]) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/cli.py::list_available_profiles() -> None
- ./packages/metricsthinking/src/metricsthinking/cli.py::main() -> Any
- ./packages/metricsthinking/src/metricsthinking/collector.py::ProjectEvidence(class)
- ./packages/metricsthinking/src/metricsthinking/collector.py::ProjectCollector(class)
- ./packages/metricsthinking/src/metricsthinking/detector.py::ArchetypeScore(class)
- ./packages/metricsthinking/src/metricsthinking/detector.py::ArchetypeDetectionResult(class)
- ./packages/metricsthinking/src/metricsthinking/detector.py::ArchetypeDetector(class)
- ./packages/metricsthinking/src/metricsthinking/detector.py::probe_archetype(target_path: str='.', custom_profiles_dir: Path | None=None) -> ArchetypeDetectionResult
- ./packages/metricsthinking/src/metricsthinking/engine.py::resolve_profile_name(hint_or_name: str | None) -> str
- ./packages/metricsthinking/src/metricsthinking/engine.py::probe_project(target_path: str='.', custom_profiles_dir: Path | None=None) -> ArchetypeDetectionResult
- ./packages/metricsthinking/src/metricsthinking/engine.py::run_audit(target_path: str='.', profile_name: str='default', archetype: str | None=None, out_dir: str | None=None, prefix: str='MetricsThinking', quiet: bool=False, prune: bool=False, medallion: bool=False, reconcile_plans: bool=True, full: bool=False) -> tuple[ProjectAuditReport, dict[str, Path]]
- ./packages/metricsthinking/src/metricsthinking/evaluator.py::CriteriaEvaluator(class)
- ./packages/metricsthinking/src/metricsthinking/fpai/ablation.py::run_ablation_sampling(chunks: list[dict[str, Any]], sample_ratio: float=0.05) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/fpai/attribution.py::resolve_context_attribution(query: str, chunks: list[dict[str, Any]]) -> list[dict[str, Any]]
- ./packages/metricsthinking/src/metricsthinking/fpai/compensation.py::generate_pruning_plan(target_path: str, dead_files: list[str], redundant_files: list[str], structural_files: list[str], file_sizes: dict[str, int]) -> ContextPruningPlan
- ./packages/metricsthinking/src/metricsthinking/fpai/compensation.py::apply_pruning_plan(plan: ContextPruningPlan, repo_root: str, update_agentignore: bool=True) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/fpai/confidence.py::calculate_confidence_envelope(sample_values: list[float], confidence_level: float=0.95) -> dict[str, float | int]
- ./packages/metricsthinking/src/metricsthinking/fpai/drift_auditor.py::audit_seed_to_code_drift(seed_path: str, repo_files: dict[str, str]) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/fpai/gatekeeper.py::calculate_shannon_entropy(data: str) -> float
- ./packages/metricsthinking/src/metricsthinking/fpai/gatekeeper.py::is_safe_placeholder(text: str) -> bool
- ./packages/metricsthinking/src/metricsthinking/fpai/gatekeeper.py::scan_file_security(file_path: str, content: str, entropy_threshold: float=4.5) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/fpai/gatekeeper.py::scan_repository_security(file_contents: dict[str, str], lockfile_present: bool=True, entropy_threshold: float=4.5, ignore_tests: bool=True) -> SecurityVulnerabilityReport
- ./packages/metricsthinking/src/metricsthinking/fpai/medallion.py::run_local_medallion_pipeline(raw_telemetry_dir: str='data/raw/telemetry', processed_dir: str='data/processed/telemetry') -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/fpai/spectral_engine.py::compute_spectral_vector(p_active: float, q_dead: float, q_dup: float, d_structural: float, gain_coefficient: float=1.0) -> FPAISpectralVector
- ./packages/metricsthinking/src/metricsthinking/incremental.py::rule_fingerprint(evaluator, function, config, evidence, attribute_cache) -> Any
- ./packages/metricsthinking/src/metricsthinking/incremental.py::observed_context(evidence) -> Any
- ./packages/metricsthinking/src/metricsthinking/lifecycle.py::extract_plan_metadata(plan_path: Path) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/lifecycle.py::update_plan_frontmatter(plan_path: Path, updates: dict[str, Any]) -> None
- ./packages/metricsthinking/src/metricsthinking/lifecycle.py::evaluate_plan_completion(plan_path: Path, checkpoint_data: dict[str, Any] | None=None) -> tuple[bool, str]
- ./packages/metricsthinking/src/metricsthinking/lifecycle.py::sync_backlog_queue(repo_root: Path, archived_plan_ids: list[str]) -> int
- ./packages/metricsthinking/src/metricsthinking/lifecycle.py::reconcile_active_plans(repo_root: Path | str='.', check_only: bool=False) -> dict[str, Any]
- ./packages/metricsthinking/src/metricsthinking/mcp_server.py::handle_list_tools() -> list[dict[str, Any]]
- ./packages/metricsthinking/src/metricsthinking/mcp_server.py::handle_call_tool(name: str, arguments: dict[str, Any]) -> list[dict[str, Any]]
- ./packages/metricsthinking/src/metricsthinking/mcp_server.py::run_mcp_server() -> Any
- ./packages/metricsthinking/src/metricsthinking/models.py::DomainArchetype(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::InspectionMode(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::EvidencePrimitiveSummary(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::ModuleStatus(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::MaturityBand(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::AuditCriterion(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::CanonicalModuleEvaluation(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::RemediationItem(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::FPAISpectralVector(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::SecurityVulnerabilityReport(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::SystemsResilienceReport(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::PruningActionItem(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::ContextPruningPlan(class)
- ./packages/metricsthinking/src/metricsthinking/models.py::ProjectAuditReport(class)
- ./packages/metricsthinking/src/metricsthinking/renderer.py::ReportRenderer(class)
- ./packages/metricsthinking/src/metricsthinking/runtime.py::read_json(path, default=None) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::digest(value) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::atomic_write(path, content) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::write_json(path, value) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::ignore_patterns(root) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::ignored(relative, patterns) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::crawl_allowed(directory) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::python_contracts(source, relative) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::input_hash(inv, layer) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::estimated_tokens(value) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::validate_seed(path, index=None) -> Any
- ./packages/metricsthinking/src/metricsthinking/runtime.py::validate_readmes(root) -> Any
- ./packages/metricsthinking/src/metricsthinking/scorer.py::AuditScorer(class)
- ./packages/thinkingseed/scripts/context_runtime.py::read_json(path, default=None) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::digest(value) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::atomic_write(path, content) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::write_json(path, value) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::repository_lock(root, name='publish', timeout=10) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::publish_layer(root, layer, payload) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::ignore_patterns(root) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::ignored(relative, patterns) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::crawl_allowed(directory) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::iter_files(root, patterns=None) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::python_contracts(source, relative) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::inventory(root, persist=False, full=False) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::contracts_index(root, persist=False, full=False) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::input_hash(inv, layer) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::estimated_tokens(value) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::bounded(payload, limit, removable=('contracts_ast', 'edges', 'files', 'active_topology', 'layers')) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::query_orientation(root, target='.', tier='1a', expand=False) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::validate_seed(path, index=None) -> Any
- ./packages/thinkingseed/scripts/context_runtime.py::validate_readmes(root) -> Any
- ./packages/thinkingseed/scripts/install_skills.py::upsert_segmented_rule_file(src_path: Path, dest_path: Path, tool_key: str='THINKINGSEED', backup: bool=False) -> bool
- ./packages/thinkingseed/scripts/install_skills.py::get_home_dir() -> Path
- ./packages/thinkingseed/scripts/install_skills.py::install_antigravity_global() -> bool
- ./packages/thinkingseed/scripts/install_skills.py::install_claude_code_global() -> bool
- ./packages/thinkingseed/scripts/install_skills.py::install_codex_global() -> bool
- ./packages/thinkingseed/scripts/install_skills.py::inject_into_project(target_path: Path, backup: bool=False, check_only: bool=False) -> bool
- ./packages/thinkingseed/scripts/install_skills.py::main() -> Any
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_llm_contract_headers(seed_content: str) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_zero_code_invariant(seed_content: str) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_path_portability(seed_content: str) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_secret_leaks(seed_content: str, seed_dir: Path=None) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::extract_repo_ast_contracts(repo_path: Path) -> Dict[str, List[str]]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_ast_contract_coverage(repo_path: Path, seed_content: str) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::check_local_tree_freshness(repo_path: Path) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::analyze_repo(repo_path: Path) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::analyze_seed(seed_path: Path) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::compute_coverage(repo_meta: Dict[str, Any], seed_meta: Dict[str, Any], repo_path: Path) -> Dict[str, Any]
- ./packages/thinkingseed/scripts/test_seed_coverage.py::generate_report(repo_meta: Dict[str, Any], hybrid_meta: Dict[str, Any], master_meta: Dict[str, Any], cov_hybrid: Dict[str, Any], cov_master: Dict[str, Any], anonymize: bool=True) -> str
- ./packages/thinkingseed/scripts/test_seed_coverage.py::main() -> None
- ./skills/v6/icontext/scripts/run.py::matches_version(path) -> Any
- ./skills/v6/idir/scripts/run.py::matches_version(path) -> Any
- ./skills/v6/metrics/scripts/run.py::matches_version(path) -> Any
- ./skills/v6/readme/scripts/run.py::matches_version(path) -> Any
- ./skills/v6/seed-master/scripts/run.py::matches_version(path) -> Any
- ./skills/v6/seed/scripts/run.py::matches_version(path) -> Any
- ./src/core/benchmark.py::percentile(values, fraction) -> Any
- ./src/core/benchmark.py::benchmark(root, samples=7) -> Any
- ./src/core/icontext_cli.py::ecosystem_root(value=None) -> Any
- ./src/core/icontext_cli.py::outputs(root, layer) -> Any
- ./src/core/icontext_cli.py::output_hash(root, layer) -> Any
- ./src/core/icontext_cli.py::layer_hash(inv, layer, root) -> Any
- ./src/core/icontext_cli.py::plan(root, full=False) -> Any
- ./src/core/icontext_cli.py::status(root) -> Any
- ./src/core/icontext_cli.py::audit(root, full=False) -> Any
- ./src/core/icontext_cli.py::request(root, layer, inv, fingerprint, delta) -> Any
- ./src/core/icontext_cli.py::complete(root, layer, expected) -> Any
- ./src/core/icontext_cli.py::metrics(root, eco, full=False, profile='default') -> Any
- ./src/core/icontext_cli.py::sync(root, eco, dry_run=False, full=False) -> Any
- ./src/core/icontext_cli.py::pack(root, path='.', tier='1a', expand=False, task='') -> Any
- ./src/core/icontext_cli.py::main(argv=None) -> Any
- ./src/core/skill_installer.py::source_bundles(eco) -> Any
- ./src/core/skill_installer.py::inspect_installation(eco, home) -> Any
- ./src/core/skill_installer.py::install(eco, agents, home, local=None, dry_run=False, only=None, source_runtime=None) -> Any

CLI flags: --agents, --all, --antigravity, --apply, --archetype, --audit, --backup, --base, --budget, --bus, --capsule, --check, --check-freshness, --check-only, --claude, --clear, --codex, --compact, --constraint, --decision, --dest, --dry-run, --evidence-hash, --expand, --expires-at, --fix, --force-defaults, --full, --global, --global-install, --hint, --home, --include-pruned, --index-dir, --input-hash, --json, --list-profiles, --local, --medallion, --move, --next, --no-anonymize, --no-discover, --no-reconcile-plans, --objective, --out-dir, --output, --overwrite, --pack, --pack-ecosystem, --phase, --plan-id, --prefix, --probe, --processed-dir, --profile, --prune, --quiet, --radius, --raw-dir, --resolve, --root, --section, --session-id, --set, --show, --slice, --status, --step-done, --sync, --target, --target-dir, --target-repo, --task, --tier, --toc, --update-golden, --verbose, -a, -d, -g, -o, -p, -q, -t, -v
### 4.2 Artefactos y propiedad de escritura

[CONFIRMADO]
- `.context/inventory.json`: Registro incremental de evidencias con hashing SHA-256.
- `.context/contracts_ast.json`: Índice de contratos y firmas públicas extraídas por AST.
- `.context/icontext_bus.json`: Bus cognitivo federado unificado.
- `.context/layers/`: Sidecars de validación emitidos por cada productor (`l0_idirectory.json`, `l1_thinkingseed.json`, `l2_metricsthinking.json`, `l3_ireadme.json`).
- `.context/sync_state.json`: Estado criptográfico de sincronización entre capas.
- `.context/checkpoint.json`: Continuidad atencional multi-agente con expiración TTL y objetivos.

---

## 5. FPAI MATHEMATICAL ENGINES & STATE MODELS

- Spectral apparent power: S_spectral = sqrt(P^2 + (Q_dead + Q_dup)^2 + D^2)
- Power factor: PF_spectral = min(1.0, (P / S_spectral) * G)
- Topological invariant hash: H_topo = SHA256(sum(SHA256(path_i || mtime_i || size_i)))
- Parity metric: phi = (|S_EN cap S_ES| / |S_EN cup S_ES|) * (1.0 - lambda_leakage)

---

## 6. EXECUTION & VERIFICATION FLOW

- Fast status: python icontext.py status
- Full doctor check: python icontext.py doctor
- Auto-repair: python icontext.py doctor --fix
- Multi-layer sync: python icontext.py sync --all
- Forensic audit: python icontext.py audit
- Surgical module seed: python icontext.py prepare seed --target packages/metricsthinking
- Subagent capsule (<450 tokens): python icontext.py pack packages/idirectory --tier 1a

---

## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA

- [CONFIRMADO] La ruta rápida reutiliza tamaño y mtime_ns para evitar lecturas innecesarias de disco. La verificación `--full` recalcula contenidos completos.
- [CONFIRMADO] Los contratos AST automáticos cubren Python a nivel de módulo. Las extensiones de lenguaje no-Python se gobiernan mediante esquemas JSON formales.
- [CONFIRMADO] En el monorepo modular, los SeedMasters en `packages/<modulo>/01_seed/` aíslan el consumo de tokens para correcciones quirúrgicas; el SeedMaster general en la raíz solo se invoca en rediseños transversales.
- [CONFIRMADO] Concurrencia resiliente con reintentos exponenciales y jitter para prevenir contención de bloqueos en sistemas de archivos NTFS.

---

## 8. EPISTEMIC RIGOR TAGS

- [CONFIRMADO] ContextKernel consolida y orquesta los paquetes modulares L0-L3.
- [CONFIRMADO] Escrituras atómicas multiplataforma erradican condiciones de carrera en el bus.
- [CONFIRMADO] Validación determinista de 6 gates ejecutada en cada ciclo de vida.
- [CONFIRMADO] Cero rutas absolutas de host y cero secretos reales (`<REDACTED>`).

---

## 9. HISTORICAL DELTA & MIGRATION LINEAGE

### 9.0 Línea de Tiempo de Evolución Arquitectónica

- v5.0.0: Desacoplamiento inicial del protocolo de federación iContext.
- v6.0.0: Introducción del runtime unificado y bundles de agentes para Antigravity y Codex.
- v6.1.0: **Consolidación definitiva en el Monorepo Modular ContextKernel**. Eliminación de la copia física de runtime, establecimiento de la jerarquía de SeedMasters de doble nivel y soporte nativo de workspace Python.

---

## 10. REPORTE DE CUMPLIMIENTO

| Área Evaluada | Cobertura | Confianza | Método de Verificación |
|---|---|---|---|
| Topología Monorepo L0 | 100.0% | Alta | FWengine.py reconcile [CONFIRMADO] |
| Contratos Simbólicos AST | 100.0% | Alta | test_seed_coverage.py [CONFIRMADO] |
| Jerarquía de SeedMasters | 100.0% | Alta | Inspección estructural 01_seed [CONFIRMADO] |
| Portabilidad Zero Local Paths | 100.0% | Alta | Invariante [INV-08] [CONFIRMADO] |
| Seguridad Zero-Trust (<REDACTED>) | 100.0% | Alta | Scanner regex [CONFIRMADO] |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es la semilla maestra (**ThinkingSeed Master v6.1**) de **ContextKernel**: el vector arquitectónico y ADN del plano de control (`contains_source_code="false"`), no su repositorio de código completo. Refleja el avance real, los contratos simbólicos y la superficie de tensión del sistema. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, contratos simbólicos, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** evaluando activamente la Superficie de Tensión (Sección 7) y los contratos de cada paquete.
> 3. **Generar código o soluciones compatibles** respetando estrictamente las rutas relativas (`./`), firmas simbólicas e invariantes definidas aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados en `packages/` usando las rutas relativas (`./`).
3. Revisa restricciones (`[INV-01]` a `[INV-08]`), contratos simbólicos (Sección 4.1) y vectores de tensión (Sección 7).
4. Si la tarea afecta a un solo paquete, invoca su SeedMaster modular (`packages/<modulo>/01_seed/seed-<modulo>-master.md`) para optimizar el presupuesto de tokens.
5. Propone cambios por archivo con rutas relativas claras y separadores Unix (`/`).

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde confirmando que asimilaste el ADN arquitectónico v6.1 de **ContextKernel** (`<SEED_ARCHITECTURAL_VECTOR>`) y ponte a disposición para auditar o colaborar.

</SEED_ARCHITECTURAL_VECTOR>
