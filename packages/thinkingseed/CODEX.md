# ThinkingSeed v5.0 Codex Instructions / CODEX.md

> Standard instructions for OpenAI Codex, Codex CLI, and Codex-powered agent environments (iContext Federation Protocol v5.0 - Capa L1).

## 🧬 Core Architecture: `<SEED_ARCHITECTURAL_VECTOR>` Contract (v5.0)
- A **ThinkingSeed** is the **architectural DNA, symbolic contract map, and technical memory** of a project (`contains_source_code="false"`). **It is NOT the full source code repository**.
- Every seed generated must open and close with `<SEED_ARCHITECTURAL_VECTOR version="5.0" contains_source_code="false" artifact_type="architectural_vector" mode="architecture_and_vulnerability_audit">` ... `</SEED_ARCHITECTURAL_VECTOR>`.
- The absence of implementation code blocks is an intentional architectural invariant (**Zero Source Code**). Never attempt to regenerate or report missing implementation source code inside a seed.
- Components tagged as `[FALTANTE]` indicate intentional scaffolding or work-in-progress (WIP).
- All generated seeds must reside exclusively in `./01_seed/` (`./01_seed/seed-[project-name].md` or `./01_seed/seed-[project-name]-master.md`).

---

## 🛠️ Workflows & Commands

### 1. `/seed` or "Generar Seed Híbrido" (Fast Architectural Vector)
When invoked with `/seed` or requested to create/update the project seed:
1. Identify the project root and ensure `./01_seed/` exists.
2. Read `./ThinkingSeed_MasterHybrid.md` and `.agents/skills/seed/SKILL.md` as reference templates.
3. Perform incremental Delta-Seeding if a previous seed exists, inspecting `./.context/tree.json`.
4. Extract public functions, classes, and CLI flags as **1-line AST symbolic signatures**:
   `module/path.py::function_name(param: Type) -> ReturnType | Invariant`
   **Never dump full implementation code blocks (>5 lines).**
5. Enforce **Zero Local Absolute Paths**: use relative paths (`./`) and set `repository_root: "./"`. Prohibit drive letters (`C:`, `D:`) or `file://` schemes.
6. Apply epistemic tags: `[CONFIRMADO]`, `[INFERIDO]`, `[DECLARADO]`, `[FALTANTE]`. Redact secrets with `<REDACTED>`.
7. Output to `./01_seed/seed-[project-name].md`.

### 2. `/seedMaster` or "Generar Seed Master" (Exhaustive & Adversarial Vector)
When invoked with `/seedMaster` or requested for a deep audit seed:
1. Read `./ThinkingSeed Master.md` and `.agents/skills/seedMaster/SKILL.md`.
2. Inspect `./.context/tree.json` and `.context.yaml` boundary beacons.
3. Consolidate into the **11 Core Sections (`0` to `10`)** with polymorphic pruning of conditional sub-modules and strict DRY referencing.
4. Extract all public symbols and CLI flags into the Section 4 Symbolic Contracts table.
5. Perform an **Adversarial Tension Audit** in Section 7 (trust boundaries, mutable state, casing drift, PATH dependencies).
6. Validate the seed against the 6 deterministic gates: `python scripts/test_seed_coverage.py --target-repo . --no-anonymize`.
7. Output to `./01_seed/seed-[project-name]-master.md`.
