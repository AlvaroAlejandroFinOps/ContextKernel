"""
Unit tests for MetricsThinking™ active plans lifecycle and archiving governance.
"""
import json
from pathlib import Path
from metricsthinking.lifecycle import (
    extract_plan_metadata,
    update_plan_frontmatter,
    evaluate_plan_completion,
    sync_backlog_queue,
    reconcile_active_plans,
)


def test_extract_and_update_plan_frontmatter(tmp_path):
    plan_file = tmp_path / "sample_plan.md"
    plan_file.write_text(
        "---\nplan_id: BKL-001\nstatus: executing\nexecutable: true\n---\n\n# Body content\n",
        encoding="utf-8"
    )

    meta = extract_plan_metadata(plan_file)
    assert meta["plan_id"] == "BKL-001"
    assert meta["status"] == "executing"
    assert meta["executable"] is True

    update_plan_frontmatter(plan_file, {"status": "completed", "executable": False})
    new_meta = extract_plan_metadata(plan_file)
    assert new_meta["status"] == "completed"
    assert new_meta["executable"] is False
    assert "# Body content" in plan_file.read_text(encoding="utf-8")


def test_evaluate_plan_completion_by_status(tmp_path):
    plan_file = tmp_path / "plan_done.md"
    plan_file.write_text(
        "---\nplan_id: P-100\nstatus: completed\n---\n# Plan\n",
        encoding="utf-8"
    )
    should_archive, reason = evaluate_plan_completion(plan_file)
    assert should_archive is True
    assert "completed" in reason


def test_evaluate_plan_completion_by_checkboxes(tmp_path):
    # All checked
    done_file = tmp_path / "all_done.md"
    done_file.write_text(
        "# Plan Tasks\n- [x] Step 1\n- [X] Step 2\n* [x] Step 3\n",
        encoding="utf-8"
    )
    should_archive, reason = evaluate_plan_completion(done_file)
    assert should_archive is True
    assert "100% ground truth" in reason

    # Some pending
    pending_file = tmp_path / "pending.md"
    pending_file.write_text(
        "# Plan Tasks\n- [x] Step 1\n- [ ] Step 2\n",
        encoding="utf-8"
    )
    should_archive, reason = evaluate_plan_completion(pending_file)
    assert should_archive is False
    assert "pending" in reason


def test_sync_backlog_queue(tmp_path):
    backlog_dir = tmp_path / "artifacts" / "plans" / "backlog"
    backlog_dir.mkdir(parents=True, exist_ok=True)
    queue_file = backlog_dir / "queue.json"

    initial_queue = {
        "version": "1.0",
        "items": [
            {
                "id": "BKL-001",
                "target_nodes": ["src/core"],
                "tier_estimate": "1a",
                "intent": "Implement core feature",
                "status": "queued",
                "acceptance_test": "pytest tests/test_core.py"
            },
            {
                "id": "BKL-002",
                "target_nodes": ["src/api"],
                "tier_estimate": "1b",
                "intent": "Refactor API",
                "status": "queued",
                "acceptance_test": "pytest tests/test_api.py"
            }
        ]
    }
    queue_file.write_text(json.dumps(initial_queue, indent=2), encoding="utf-8")

    updated = sync_backlog_queue(tmp_path, ["BKL-001"])
    assert updated == 1

    updated_data = json.loads(queue_file.read_text(encoding="utf-8"))
    assert updated_data["items"][0]["status"] == "done"
    assert updated_data["items"][1]["status"] == "queued"


def test_reconcile_active_plans_full_workflow(tmp_path):
    active_dir = tmp_path / "artifacts" / "plans" / "active"
    archive_dir = tmp_path / "artifacts" / "plans" / "archive"
    mt_dir = tmp_path / "artifacts" / "plans" / "metricsthinking"
    active_dir.mkdir(parents=True, exist_ok=True)

    # 1. Stray MetricsThinking artifact in active/
    stray_roadmap = active_dir / "INFERRED_ROADMAP.md"
    stray_roadmap.write_text("# Roadmap content", encoding="utf-8")

    # 2. Completed plan in active/
    comp_plan = active_dir / "completed_plan.md"
    comp_plan.write_text(
        "---\nplan_id: BKL-010\nstatus: completed\nexecutable: true\n---\n# Done",
        encoding="utf-8"
    )

    # 3. Executing plan in active/
    exec_plan = active_dir / "executing_plan.md"
    exec_plan.write_text(
        "---\nplan_id: BKL-011\nstatus: executing\nexecutable: true\n---\n- [ ] Task 1",
        encoding="utf-8"
    )

    res = reconcile_active_plans(tmp_path)

    # Check stray artifact moved to metricsthinking/
    assert not stray_roadmap.exists()
    assert (mt_dir / "INFERRED_ROADMAP.md").exists()
    assert "INFERRED_ROADMAP.md" in res["cleaned_artifacts"]

    # Check completed plan moved to archive/
    assert not comp_plan.exists()
    assert (archive_dir / "completed_plan.md").exists()
    archived_meta = extract_plan_metadata(archive_dir / "completed_plan.md")
    assert archived_meta["status"] == "completed"
    assert archived_meta["executable"] is False

    # Check executing plan remains in active/
    assert exec_plan.exists()
    assert len(res["retained_plans"]) == 1
    assert res["retained_plans"][0]["file"] == "executing_plan.md"
