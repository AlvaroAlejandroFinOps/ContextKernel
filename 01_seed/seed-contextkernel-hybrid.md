<SEED_ARCHITECTURAL_VECTOR version="6.1" contains_source_code="false" artifact_type="architectural_vector" mode="agile_context_seed">

# ThinkingSeed Hybrid v6.1: ContextKernel

> **[DIRECTIVA DE SISTEMA]:** Vector arquitectónico ágil (<1,000 tokens) para operaciones rápidas sin saturación de contexto.

## 0. IDENTIDAD Y METADATOS

```yaml
seed_schema_version: "6.1"
project_name: "ContextKernel"
repository_name: "ContextControl"
slogan: "ContextKernel is a context and attention control plane for AI engineering agents"
project_type: "monorepo-context-control-plane"
repository_root: "./"
git_branch: "master"
coverage_level: "agile"
```

### 0.1 Instrucciones para el agente receptor
1. Memoria técnica ágil (`contains_source_code="false"`).
2. Usa rutas relativas Unix (`./`) y convención `all-lowercase`.
3. Seguridad Zero-Trust: secretos como `<REDACTED>`.

---

## 1. RESUMEN ARQUITECTÓNICO

[CONFIRMADO] **ContextKernel** es el plano de control cognitivo para agentes de ingeniería de IA:
- **L0 (iDirectory)**: `packages/idirectory/` (Topología, semáforos `.context.yaml` y satélite `.context/tree.json`).
- **L1 (ThinkingSeed)**: `packages/thinkingseed/` (ADN arquitectónico determinista de 6 gates).
- **L2 (MetricsThinking)**: `packages/metricsthinking/` (Auditoría forense M01-M10 y FPIA espectral).
- **L3 (iReadme)**: `packages/ireadme/` (Documentación bilingüe con paridad Phi = 1.0).
- **CLI Orchestrator**: `packages/contextkernel-cli/` (Entrada unificada y bus `.context/icontext_bus.json`).

---

## 2. TOPOLOGÍA CANÓNICA

- `./.context`: role="context_engineering" | key_files=["tree.json", "icontext_bus.json"]
- `./01_seed`: role="dna" | key_files=["seed-contextkernel-master.md", "seed-contextkernel-hybrid.md"]
- `./packages/idirectory`: role="l0_topological_governor"
- `./packages/thinkingseed`: role="l1_architectural_dna"
- `./packages/metricsthinking`: role="l2_forensic_auditor"
- `./packages/ireadme`: role="l3_paper_grade_synthesizer"
- `./packages/contextkernel-cli`: role="core_orchestrator"
- `./tests`: role="integration_tests"

---

## 3. INVARIANTES OPERACIONALES

- [INV-01] Resilient NTFS I/O backoff on `.context/icontext_bus.json`.
- [INV-02] Zero blind recursive filesystem scans.
- [INV-03] Hierarchical pruning propagation (`crawl=false`).
- [INV-04] Atomic bus updates under repository lock.
- [INV-05] Zero credential leakage (`<REDACTED>`).
- [INV-06] Deterministic epistemic tags (`[CONFIRMADO]`, `[INFERIDO]`, `[FALTANTE]`).
- [INV-07] Strict bilingual doc parity (Phi = 1.0).
- [INV-08] Zero host-specific absolute paths (only `./`).

---

## 4. COMANDOS OPERACIONALES RÁPIDOS

- Estado: `python icontext.py status`
- Auditoría: `python icontext.py audit`
- Sincronización: `python icontext.py sync --all`
- Diagnóstico: `python icontext.py doctor`
- Reconciliación: `python FWengine.py reconcile`

---

## 5. REPORTE DE CUMPLIMIENTO
| Gate | Estado | Evidencia |
|---|---|---|
| GATE-01..06 | PASS | Validado por test_seed_coverage.py [CONFIRMADO] |

---

## 📌 CONTEXT HANDOFF & PROTOCOLO DE ASISTENCIA

> **Orientación:** Vector ágil de ContextKernel. Mantén respuestas concisas, utiliza rutas relativas `./` y respeta las invariantes `[INV-01]` a `[INV-08]`.

</SEED_ARCHITECTURAL_VECTOR>
