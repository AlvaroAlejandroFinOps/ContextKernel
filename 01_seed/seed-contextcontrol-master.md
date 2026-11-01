<SEED_ARCHITECTURAL_VECTOR version="6.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">

# ThinkingSeed Master v5.0: ContextControl

> **[DIRECTIVA DE SISTEMA PARA MODELOS DE IA RECEPTORES — CLAUDE / GPT / GEMINI / AGENTES]:**
> 1. **Naturaleza del Artefacto:** Este documento es un **Vector Arquitectónico y Memoria Técnica (ThinkingSeed Master v5.0)** con `contains_source_code="false"`. **NO es el repositorio de código fuente completo** ni un volcado truncado. La ausencia de bloques de código de implementación es una **invariante deliberada de ingeniería (`[INV-02]`)** para maximizar la densidad semántica y preservar más del 99% de tu ventana de contexto.
> 2. **Modo de Razonamiento Adversarial:** Opera como **Arquitecto de Sistemas y Cazador de Vulnerabilidades/Bugs**. Utiliza las firmas simbólicas AST (Sección 4.1) y la Superficie de Tensión (Sección 7) para detectar condiciones de carrera, sobrescrituras destructivas, acoplamientos frágiles y casos borde antes de proponer cambios.
> 3. **Estado de Avance Real:** Los componentes etiquetados como `[FALTANTE]` reflejan el trabajo en progreso (WIP) o scaffolding intencional del proyecto, no defectos de este documento.

## 0. IDENTIDAD, METADATOS Y CONTRATO DEL RECEPTOR

```yaml
seed_schema_version: "6.0"
project_name: "ContextControl"
repository_name: "ContextControl"
project_type: "orchestrator-command-plane"
repository_mode: "single-project"
generated_at: "2026-10-31T19:22:25.423594+00:00"
generated_by: "Codex / iContext v6 migration"
repository_root: "./"
git_branch: "master"
analysis_mode: "static+git+validated"
coverage_level: "high"
```

### 0.1 Instrucciones para el modelo receptor
1. **ADN vs Repositorio:** Reconoce este documento como la memoria técnica y el ADN del proyecto (`contains_source_code="false"`), no como el repositorio completo ni como una prueba de ejecución en vivo.
2. **Contexto Pasivo y Quirúrgico:** No generes código no solicitado ni reclames por archivos ausentes; espera instrucciones específicas del usuario o utilízalo como Ground Truth para responder consultas técnicas.
3. **Estado de Avance:** Considera que las secciones o directorios marcados como `[FALTANTE]` representan el avance real del proyecto y oportunidades de asistencia, no errores del documento.
4. **Rigor Epistemológico:** Respeta las etiquetas `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[NO VERIFICADO]` y `[FALTANTE]`. No transformes inferencias en hechos.
5. **Portabilidad de Rutas:** Antes de proponer cambios, identifica módulos y archivos afectados citando sus rutas exactas relativas al repositorio (`./ruta/archivo`) con barras inclinadas (`/`). Prohibido emitir rutas absolutas locales o URIs con esquema de archivo local.
6. **Contratos Simbólicos:** Conserva la arquitectura, convenciones `all-lowercase`, firmas simbólicas AST (Sección 4.1) e invariantes (`[INV-01]` a `[INV-08]`).
7. **Postura Adversarial Constructiva:** Evalúa siempre la Sección 7 (Superficie de Tensión) para anticipar impactos laterales en reglas de agentes, sincronización satelital, pruebas y seguridad.
8. **Seguridad Zero-Trust:** Nunca reveles, inventes ni solicites secretos reales; utiliza siempre el marcador `<REDACTED>`.

---

## 1. RESUMEN EJECUTIVO Y ALCANCE

[CONFIRMADO] Coordina sincronización, diagnóstico y auditoría de los cuatro productos independientes. El CLI prepara evidencia, bloquea dependencias ante fallos y solicita al agente actual la redacción pendiente; no integra un proveedor de IA externo.

[CONFIRMADO] Puede operar sin clones de los otros repositorios. La federación comparte artefactos versionados y ContextControl coordina el flujo cuando está disponible.

## 2. DIRECTORY BEACONS & STRUCTURAL ROLES

### 2.0 Estado vigente v6

[CONFIRMADO] En v6, FWengine.py es un lanzador y tools/icontext_runtime es una distribución generada. Los orígenes mantenidos están en iDirectory/src/core y ContextControl/src/core; las copias generadas se verifican por manifest. skills/v6 contiene bundles con scripts y recursos completos. Las capas siguen siendo L0 iDirectory, L1 ThinkingSeed, L2 MetricsThinking y L3 iReadme.
- ./.context: role="context_engineering" | crawl=true | key_files=["tree.json", "icontext_bus.json", "contracts_ast.json"]
- ./.agents/skills: role="agent_skills" | crawl=true | key_files=["icontext/SKILL.md"]
- ./01_seed: role="dna" | crawl=true | seed_reference="required"
- ./config: role="configuration" | crawl=true | key_files=["context_policy.json"]
- ./schemas: role="data_contracts" | crawl=true
- ./artifacts: role="evaluation_artifacts" | crawl=true
- ./scripts: role="ops_automation" | crawl=true
- ./tests: role="test_suites" | crawl=true

---

## 3. CRYPTOGRAPHIC INVARIANTS & OPERATIONAL RULES

### 3.0 Estado vigente v6

[CONFIRMADO] El flujo v6 es detectar cambios, actualizar evidencia L0, preparar SeedMaster, evaluar Metrics y preparar README. sync devuelve 3 cuando el agente debe redactar, 1 ante fallo requerido y 0 al completar. prepare es de lectura; complete rechaza hashes de entrada que hayan cambiado. Sin subcomando se muestra ayuda; las reparaciones requieren doctor --fix.
- [INV-01] Resilient NTFS I/O with 10 jittered backoff retries on icontext_bus.json.
- [INV-02] Zero blind recursive filesystem scans (find ., Get-ChildItem -Recurse prohibited).
- [INV-03] Hierarchical pruning propagation (crawl=false prohibits sub-tree exploration).
- [INV-08] Zero host-specific absolute path leakage (strictly relative ./ paths).

---

## 4. CONTRATOS SIMBÓLICOS, MODELO DE DATOS Y PERSISTENCIA

### 4.1 Contratos públicos vigentes v6

[CONFIRMADO] Firmas simbólicas extraídas de archivos activos, con hash de contenido y versión del analizador.

- `./skills/v6/icontext/scripts/run.py::./skills/v6/icontext/scripts/run.py::matches_version(path) -> Any`
- `./src/core/benchmark.py::./src/core/benchmark.py::percentile(values, fraction) -> Any`
- `./src/core/benchmark.py::./src/core/benchmark.py::benchmark(root, samples=7) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::ecosystem_root(value=None) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::outputs(root, layer) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::output_hash(root, layer) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::layer_hash(inv, layer, root) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::plan(root, full=False) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::status(root) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::audit(root, full=False) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::request(root, layer, inv, fingerprint, delta) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::complete(root, layer, expected) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::metrics(root, eco, full=False, profile='default') -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::sync(root, eco, dry_run=False, full=False) -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::pack(root, path='.', tier='1a', expand=False, task='') -> Any`
- `./src/core/icontext_cli.py::./src/core/icontext_cli.py::main(argv=None) -> Any`
- `./src/core/skill_installer.py::./src/core/skill_installer.py::source_bundles(eco) -> Any`
- `./src/core/skill_installer.py::./src/core/skill_installer.py::inspect_installation(eco, home) -> Any`
- `./src/core/skill_installer.py::./src/core/skill_installer.py::install(eco, agents, home, local=None, dry_run=False, only=None, source_runtime=None) -> Any`

CLI flags: `--agents`, `--all`, `--constraint`, `--decision`, `--dry-run`, `--evidence-hash`, `--expand`, `--fix`, `--full`, `--home`, `--input-hash`, `--json`, `--local`, `--next`, `--objective`, `--pack`, `--profile`, `--root`, `--session-id`, `--set`, `--show`, `--target`, `--task`, `--tier`, `--verbose`, `-v`

### 4.2 Artefactos y propiedad de escritura

[CONFIRMADO] .context/orientation_cache.json conserva vistas compiladas; las consultas rápidas verifican poda y metadatos de archivos y declaran la generación registrada. El CLI usa UTF-8 en Windows.

[CONFIRMADO] .context/inventory.json mantiene evidencia; .context/contracts_ast.json conserva contratos; .context/layers contiene estados por productor y icontext_bus.json se agrega bajo bloqueo del repositorio. .context/sync_state.json registra entradas y salidas aceptadas. .context/update_request.json transfiere redacción pendiente. Los checkpoints de sesión tienen identidad, objetivo, restricciones, decisiones, evidencia y próxima acción.

## 5. FPAI MATHEMATICAL ENGINES & STATE MODELS
- Spectral apparent power: S_spectral = sqrt(P^2 + (Q_dead + Q_dup)^2 + D^2)
- Power factor: PF_spectral = min(1.0, (P / S_spectral) * G)
- Topological invariant hash: H_topo = SHA256(sum(SHA256(path_i || mtime_i || size_i)))
- Parity metric: phi = (|S_EN cap S_ES| / |S_EN cup S_ES|) * (1.0 - lambda_leakage)

---

## 6. EXECUTION & VERIFICATION FLOW
- Fast status: python icontext.py status
- 5-Phase sync: python icontext.py sync
- Forensic audit: python audit_federation.py
- Subagent capsule: python icontext.py capsule --target <dir> --task "<task>"

---

## 7. SUPERFICIE DE TENSIÓN, CONTRADICCIONES Y MODOS DE FALLA

- [CONFIRMADO] La ruta rápida reutiliza tamaño y mtime_ns para evitar lecturas. La verificación --full recalcula contenidos, incluso ante timestamps restaurados; la consulta de estado registrada no certifica por sí sola la frescura física.
- [CONFIRMADO] Los contratos AST automáticos cubren Python a nivel de módulo. No equivalen a cobertura semántica de todos los lenguajes, cuerpos de funciones o comportamiento observado del producto.
- [CONFIRMADO] FPAI y el recuento heurístico de tokens son indicadores auxiliares. La distorsión y los resultados de atención no observados permanecen expresamente sin medir.
- [CONFIRMADO] complete comprueba estructura y contratos públicos; la exactitud narrativa requiere revisión del agente sobre la evidencia afectada. La ausencia de errores estructurales no demuestra ausencia de bugs.
- [CONFIRMADO] La agregación del bus usa bloqueo de proceso. El checkpoint compatible apunta a la última sesión seleccionada; la continuidad paralela debe usar identificadores de sesión explícitos.
- [CONFIRMADO] La paridad de bundles y sus comandos puede comprobarse sin invocar modelos. El éxito de tareas en sesiones reales de ambos proveedores requiere evidencia observada separada y no se presume de estas pruebas.

## 8. EPISTEMIC RIGOR TAGS
- [CONFIRMADO] icontext.py and audit_federation.py orchestrate L0-L3 layers.
- [CONFIRMADO] Multi-process atomic write eliminates race conditions.
- [CONFIRMADO] 6 gates validation enforced deterministically. Todos los secretos redactados como `<REDACTED>`.

---

## 9. HISTORICAL DELTA & MIGRATION LINEAGE

### 9.0 Estado vigente v6

[CONFIRMADO] La migración v6 conserva los comandos compatibles y registra las pruebas y mediciones de esta entrega en .context/v6_validation.json y .context/benchmark_v6.json. Las reglas y workflows anteriores se conservan como referencias históricas podadas. La versión de cada proyecto puede fijarse en .context/toolchain.json.
- v5.0.0: Initial decoupled migration from iContext root to ContextControl central command repository.

---

## 10. REPORTE DE CUMPLIMIENTO
| Área Evaluada | Cobertura | Confianza | Método de Verificación |
|---|---|---|---|
| Topología Física L0 | 100.0% | Alta | FWengine.py reconcile [CONFIRMADO] |
| Contratos Simbólicos AST | 100.0% | Alta | test_seed_coverage.py [CONFIRMADO] |
| Portabilidad Zero Local Paths | 100.0% | Alta | Invariante [INV-08] [CONFIRMADO] |
| Seguridad Zero-Trust (<REDACTED>) | 100.0% | Alta | Scanner regex [CONFIRMADO] |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Mensaje de orientación para el modelo de IA receptor:**
> "Esto es una semilla de proyecto (**ThinkingSeed Master v5.0**): el vector arquitectónico y ADN del proyecto (`contains_source_code="false"`), no su repositorio de código completo. Refleja el avance real, los contratos simbólicos y la superficie de tensión del sistema hasta la fecha. Como modelo receptor, tu función es usar esta semilla como memoria técnica para:
> 1. **Responder preguntas** sobre la arquitectura, contratos simbólicos, dependencias y flujos del sistema.
> 2. **Auditar riesgos y sugerir mejoras** evaluando activamente la Superficie de Tensión (Sección 7) y las áreas marcadas como `[FALTANTE]`.
> 3. **Generar código o soluciones compatibles** respetando estrictamente las rutas relativas (`./`), firmas simbólicas e invariantes definidas aquí, cuando el usuario te lo solicite."

### Pautas de resolución:
Antes de resolver una solicitud:
1. Identifica el objetivo del usuario.
2. Localiza los componentes afectados usando las rutas relativas (`./`) del Seed.
3. Revisa restricciones (`[INV-01]` a `[INV-08]`), contratos simbólicos (Sección 4.1) y vectores de tensión (Sección 7).
4. Propone cambios por archivo con rutas relativas claras y separadores Unix (`/`).

### 🤝 Acuse de Recibo Inicial
Si el usuario adjuntó esta semilla **sin una instrucción específica**, no intentes generar código ni completar archivos vacíos. Responde confirmando que asimilaste el ADN arquitectónico v5.0 de **ContextControl** (`<SEED_ARCHITECTURAL_VECTOR>`) y ponte a disposición para auditar o colaborar.

</SEED_ARCHITECTURAL_VECTOR>
