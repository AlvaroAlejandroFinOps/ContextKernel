# ContextKernel: Context & Attention Control Plane

**ContextKernel is a context and attention control plane for AI engineering agents.** Incremental evidence updates, portable Antigravity/Codex skills, modular package architecture and session continuity. See the [v6 operation and migration guide](docs/specs/icontext-v6.md).
<!-- ICONTEXT-V6:RELEASE -->


**Language:** [English](README.md) | [Español](README_ES.md)

[![Standard](https://img.shields.io/badge/Standard-Enterprise%20Paper--Grade%20v6.1-2b2b2b?style=flat-square)](#)
[![Ecosystem](https://img.shields.io/badge/Ecosystem-Multi--AI%20%28Google%20%7C%20Claude%20%7C%20OpenAI%20%7C%20Cursor%29-34495e?style=flat-square)](#)
[![iContext Federation](https://img.shields.io/badge/iContext-Federated%20v6.1-1a1a1a?style=flat-square)](#)
[![iDirectory L0](https://img.shields.io/badge/L0-iDirectory%20v6.1-2b2b2b?style=flat-square)](#)
[![ThinkingSeed L1](https://img.shields.io/badge/L1-ThinkingSeed%20v6.1-34495e?style=flat-square)](#)
[![MetricsThinking L2](https://img.shields.io/badge/L2-MetricsThinking%20v6.1-4b5563?style=flat-square)](#)
[![iReadme L3](https://img.shields.io/badge/L3-iReadme%20v6.1-000000?style=flat-square)](#)
[![Engine](https://img.shields.io/badge/Engine-ContextKernel%20Core-1a1a1a?style=flat-square)](#)

---

## 1. Executive Abstract

Modern enterprise software systems, cloud data platforms, and autonomous AI agents face severe architectural friction stemming from unstructured topologies, untracked API drifts, and uncoordinated context boundaries. Without deterministic governance, high-velocity engineering teams accumulate cognitive debt, compromising technical onboarding velocity and breaking automated agent orchestration across production clusters.

ContextKernel coordinates synchronization, auditing, and context boundaries through a unified modular monorepo and versioned runtime. It updates incremental evidence, propagates failures across layers, and provides the current host agent with isolated SeedMaster and documentation sections for surgical authoring. TCO savings and SLA compliance have not been measured.

The architecture functions under a unified Multi-AI ingestion paradigm, operating uniformly across Google Antigravity, Anthropic Claude Code, OpenAI ChatGPT/Codex, and Cursor IDE. Through dual-language synchronization (English/Spanish), formal KaTeX mathematical models, monochromatic high-impact shields, and symmetric ASCII topologies, ContextKernel guarantees institutional transparency for executive leaders and principal engineers alike.

---

## 2. System Architecture & Topology

The system enforces strict topological separation between the Ingestion Control Plane, the Autonomous Analytical Kernel, and the Synchronized Artifact State Plane.

```
+---------------------------------------------------------------------------------------------------+
|                                  CONTEXTKERNEL MONOREPO TOPOLOGY                                 |
+---------------------------------------------------------------------------------------------------+
                                                  |
                 +--------------------------------+--------------------------------+
                 |                                                                 |
                 v                                                                 v
+----------------------------------+                              +----------------------------------+
|     INGESTION CONTROL PLANE      |                              |    ANALYTICAL & DATA PLANE       |
|  - Multi-AI Orchestrators        |                              |  - High-Throughput Rust/Py Engine|
|  - Context Capsule Isolation     |                              |  - Spectral FPIA Verification    |
|  - Topology Hash Integrity       |                              |  - Formal Invariant Enforcement  |
+----------------------------------+                              +----------------------------------+
                 |                                                                 |
                 +--------------------------------+--------------------------------+
                                                  |
                                                  v
+---------------------------------------------------------------------------------------------------+
|                                   SYNCHRONIZED OUTPUT PLANE                                       |
|  - Dual Enterprise Paper-Grade Artifacts (README.md / README_ES.md with phi = 1.0)               |
|  - Cryptographic Satellites (.context/tree.json & .context/icontext_bus.json)                     |
|  - Hierarchical SeedMasters (Root General Vector & Modular Subpackage Seeds)                      |
+---------------------------------------------------------------------------------------------------+
```

### Federated Context Control Protocol (FCCP v6.1)

This monorepo formally implements the **Federated Context Control Protocol v6.1**, orchestrating **5 canonical packages** under `packages/` for autonomous agentic governance and attentional optimization:

| Layer | Component | Package Directory | Primary Engineering Function | Status |
| :--- | :--- | :--- | :--- | :--- |
| `CLI` | **ContextKernel CLI** | `packages/contextkernel-cli` | Universal command-line interface, orchestration runtime, session continuity, and multi-agent skill installer. | `ACTIVE (v6.1)` |
| `L0` | **iDirectory** | `packages/idirectory` | Enforces canonical all-lowercase topology, boundary beacons (`.context.yaml`), cryptographic tree satellite (`tree.json`), token budgeting, and capsule isolation (<450 tokens). | `ACTIVE (v6.1)` |
| `L1` | **ThinkingSeed** | `packages/thinkingseed` | Preserves architectural technical memory and AST symbolic contracts with zero implementation code leakage (Zero Source Code), certified across 6 deterministic validation gates. | `ACTIVE (v6.1)` |
| `L2` | **MetricsThinking** | `packages/metricsthinking` | Computes ground-truth maturity scores across 10 canonical modules, AST semantic drift detection, FPIA spectral efficiency ($S_{\text{spectral}}$, $PF_{\text{spectral}}$), and Zero-Trust security scanning. | `ACTIVE (v6.1)` |
| `L3` | **iReadme** | `packages/ireadme` | Synchronizes dual English/Spanish documentation under the Enterprise Paper-Grade standard, guaranteeing structural parity $\Phi = 1.0$, formal KaTeX formulations, and zero local path leakages. | `ACTIVE (v6.1)` |

Interoperability across these tools is orchestrated in a non-blocking fashion via the **Federated Cognitive Bus** (`./.context/icontext_bus.json`), securing attentional continuity, zero satellite drift, and strict hallucination mitigation across autonomous AI agents.

---

## 3. Mathematical Formulation & Analytical Engines

The architectural stability and computational efficiency of ContextKernel are governed by formal mathematical optimization models.

Let $\mathcal{T}$ denote the tracked filesystem topology, where each node $n_i \in \mathcal{T}$ possesses an active status indicator $\alpha_i \in \{0, 1\}$ governed by boundary beacons. The global active context budget $\Omega(\mathcal{T})$ is formulated as:

$$\Omega(\mathcal{T}) = \sum_{i=1}^{N} \alpha_i \cdot \tau(n_i)$$

where $\tau(n_i)$ represents the estimated token weight of artifact $n_i$. The FPIA spectral power factor $PF_{\text{spectral}}$ evaluates cognitive efficiency:

$$PF_{\text{spectral}} = \frac{P_{\text{active}}}{\sqrt{P_{\text{active}}^2 + Q_{\text{dead}}^2 + Q_{\text{dup}}^2 + D_{\text{structural}}^2}}$$

Structural documentation parity $\Phi$ between language variants is rigorously enforced:

$$\Phi = \frac{1}{M} \sum_{m=1}^{M} \mathbb{I}(\text{Section}_{m}^{\text{EN}} \equiv \text{Section}_{m}^{\text{ES}}) = 1.0$$

The apparent spectral power $S_{\text{spectral}}$ quantifies multi-dimensional repository entropy:

$$S_{\text{spectral}} = \sqrt{P^2 + (Q_{\text{dead}} + Q_{\text{dup}})^2 + D^2}$$

---

## 4. Empirical Performance & Benchmarks

<!-- ICONTEXT-V6:TELEMETRY:START -->
| Evidence / Evidencia | Recorded value / Valor registrado |
| :--- | :--- |
| Metrics score | 80.5 |
| Estimated spectral factor (auxiliary) | 0.9777 |
| Query latency p95 (ms) | 7.313400041311979 |
| Validity | Recorded evidence; verify freshness with icontext audit |
<!-- ICONTEXT-V6:TELEMETRY:END -->

Version 6.1 consolidates the 4 independent products into a single modular monorepo, eradicating duplicated runtime trees and eliminating cross-repository synchronization drift. Release measurements are recorded in `.context/benchmark_v6.json`, including engine/process p50/p95, file reads, and comparison against full inventory scans. Token counts are explicitly estimated. Model attention outcomes require observed host sessions and are not inferred from FPAI.

---

## 5. Repository Structure & Artifacts

The repository enforces canonical `all-lowercase` directory naming and a modular package workspace:

```
ContextKernel/
├── .context/                          # State satellites (tree.json, checkpoint.json, icontext_bus.json)
├── 01_seed/                           # General SeedMaster (seed-contextkernel-master.md)
├── config/                            # Parameterized policy and decoupled configuration
├── schemas/                           # Strict Draft-07 JSON Schemas
├── packages/                          # Isolated high-engineering modules
│   ├── contextkernel-cli/             # Universal CLI entrypoint, runtime, and skill installer
│   ├── idirectory/                    # Layer L0: Topological control plane, beacons, and tree satellite
│   ├── thinkingseed/                  # Layer L1: Symbolic architectural DNA and 6 deterministic gates
│   ├── metricsthinking/               # Layer L2: Forensic technology auditor, FPIA spectral engine, Rust backend
│   └── ireadme/                       # Layer L3: Paper-grade bilingual documentation synthesizer
├── skills/                            # Agent skill bundles (icontext, idir, seed, seed-master, metrics, readme)
├── pyproject.toml                     # Root workspace configuration and unified dependencies
├── Contex.code-workspace              # Multi-root IDE workspace configuration
├── FWengine.py                        # Topological compatibility launcher (L0)
└── icontext.py                        # Universal Master CLI launcher (L0-L3)
```

---

## 6. Execution & Verification Protocol

### Quickstart Execution

Run these commands from the repository root:

```powershell
# 1. Inspect recorded status across all registered packages
python ./icontext.py status --all

# 2. Verify evidence and diagnostic health without mutating files
python ./icontext.py doctor

# 3. Automatically heal topology casing and reinstall agent skills
python ./icontext.py doctor --fix

# 4. Synchronize all layers across the monorepo pipeline
python ./icontext.py sync --all
python ./icontext.py sync --dry-run --all

# 5. Execute forensic evidence audit across all components
python ./icontext.py audit --all

# 6. Reconcile directory topology and rebuild the tree satellite
python ./FWengine.py reconcile
python ./FWengine.py reconcile --check

# 7. Extract surgical modular seed for token-efficient agent work
python ./icontext.py prepare seed --target packages/metricsthinking

# 8. Generate surgical context pack (<450 tokens) for subagents
python ./icontext.py pack packages/idirectory --tier 1a --json

# 9. Run comprehensive automated test suite (238+ tests)
python -m pytest packages/ --import-mode=importlib -v
```

`status` reports the last recorded state; use `audit` to verify current evidence. `reconcile` restores canonical lowercase directory names where the engine recognizes a case mismatch, synchronizes beacons and rebuilds the satellite. `reconcile --check` reports drift without changing files.

---

## 7. Domain Glossary

- **Context Capsule**: Surgical, ultra-dense JSON context payload (<450 tokens) designed for subagents, preventing context degradation.
- **Topology Hash**: Cryptographic SHA-256 fingerprint representing the tracked directory structure, guaranteeing zero undetected drift.
- **Federated Bus**: Interoperability state vector (`.context/icontext_bus.json`) coordinating L0, L1, L2, and L3 layers without blocking file locks.
- **Parity Score ($\Phi$)**: Strict invariant measuring 1-to-1 equivalence between dual English and Spanish paper-grade documentation artifacts.
- **Hierarchical SeedMasters**: Two-level architectural vector system: root General SeedMaster for ecosystem boundaries, and modular package SeedMasters for surgical token-efficient tasks.

---

## 8. Academic & Engineering References

1. **Dean, J., & Ghemawat, S.** (2004). *MapReduce: Simplified Data Processing on Large Clusters*. Communications of the ACM.
2. **Gamma, E., et al.** (1994). *Design Patterns: Elements of Reusable Object-Oriented Software*. Addison-Wesley.
3. **Gravity HyperScale Thinking**. (2026). *ContextKernel: Universal Context & Attention Control Plane for AI Engineering Agents*.

```bibtex
@article{contextkernel2026architecture,
  title={ContextKernel: Universal Context & Attention Control Plane for AI Engineering Agents},
  author={Gravity HyperScale Thinking Systems Architecture Lab},
  year={2026},
  institution={Gravity HyperScale Thinking}
}
```
