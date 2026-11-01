# ContextControl: iContext v6

Coordinate four independent products. Use python icontext.py status, pack, sync, audit and doctor. Exit 3 means agent redaction is pending; exit 1 means failure. Repairs require doctor --fix.

- Use the smallest sufficient context: focused pack or verified .context/tree.json before inspection. Never traverse a crawl:false ancestor or scan blindly. Never preload the seed for scoped work.
- Precedence: code and schemas, context_policy.json, verified maps and layer states, active session, seeds, approved plans. Preserve the user's scope, constraints and existing work.
- Queries, checks and dry runs never write. Redact secrets and use relative paths in generated documentation.
- Use skills/v6 and its bundled script; resolve resources from the skill installation. .context/toolchain.json pins the runtime. Antigravity uses /skill and Codex uses $skill.
- Maintain objective, constraints, evidence, decisions and next action in an identified session when switching agents. After topology or beacon changes, run python FWengine.py reconcile once.
- Detailed workflow: docs/specs/icontext-v6.md. Complete previous rules remain in docs/specs/governance-agents-before-v6.md; current code and schemas govern v6 semantics.
