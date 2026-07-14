"""Create run folders from baselines/ and materials/."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

from lib.paths import get_root
from lib.runs import (
    CONDITION_CONTEXT_FILES,
    CONDITIONS,
    DEFAULT_REPETITIONS,
    RUN_DIR_PATTERN,
    USER_STORY_IDS,
    RunInfo,
    validate_run_inputs,
)


def _iter_run_specs(repetitions: int) -> list[tuple[str, str, str, int]]:
    """Return (run_id, us_id, condition, repetition) for the full matrix."""
    specs: list[tuple[str, str, str, int]] = []
    for us_id in USER_STORY_IDS:
        for condition in CONDITIONS:
            for repetition in range(1, repetitions + 1):
                run_id = f"{us_id}_{condition}_R{repetition}"
                specs.append((run_id, us_id, condition, repetition))
    return specs


def _remove_matching_runs(target_runs_dir: Path, *, dry_run: bool) -> int:
    removed = 0
    if not target_runs_dir.is_dir():
        return removed

    for entry in sorted(target_runs_dir.iterdir()):
        if not entry.is_dir() or not RUN_DIR_PATTERN.match(entry.name):
            continue
        removed += 1
        if dry_run:
            print(f"[dry-run] remove {entry}")
            continue
        shutil.rmtree(entry)
        print(f"Removed {entry.name}")
    return removed


def scaffold_run(
    run_path: Path,
    us_id: str,
    condition: str,
    *,
    root: Path,
    force: bool,
    dry_run: bool,
) -> str:
    """
    Create one run folder with inputs only (no outputs).

    Returns: 'created' | 'updated' | 'skipped' | 'would-create' | 'would-update'
    """
    baseline_dir = root / "baselines" / us_id
    materials_dir = root / "materials" / us_id
    context_source_name = CONDITION_CONTEXT_FILES.get(condition)

    required = [
        baseline_dir / "spec.md",
        baseline_dir / "checklists" / "requirements.md",
        materials_dir / "user-story.md",
    ]
    if context_source_name:
        required.append(materials_dir / context_source_name)

    missing = [str(path) for path in required if not path.is_file()]
    if missing:
        raise FileNotFoundError(
            f"Missing source files for {run_path.name}:\n- " + "\n- ".join(missing)
        )

    exists = run_path.is_dir()
    if exists and not force:
        return "skipped"
    if dry_run:
        return "would-update" if exists else "would-create"

    experiment_input = run_path / "experiment-input"
    checklists = run_path / "checklists"
    experiment_input.mkdir(parents=True, exist_ok=True)
    checklists.mkdir(parents=True, exist_ok=True)

    shutil.copy2(baseline_dir / "spec.md", run_path / "spec.md")
    shutil.copy2(
        baseline_dir / "checklists" / "requirements.md",
        checklists / "requirements.md",
    )
    shutil.copy2(materials_dir / "user-story.md", experiment_input / "user-story.md")

    context_path = experiment_input / "context.md"
    if condition == "C0":
        if context_path.exists():
            context_path.unlink()
    else:
        assert context_source_name is not None
        shutil.copy2(materials_dir / context_source_name, context_path)

    return "updated" if exists else "created"


def scaffold_all(
    *,
    repetitions: int,
    clean: bool,
    force: bool,
    dry_run: bool,
    root: Path | None = None,
) -> int:
    root = (root or get_root()).resolve()
    target_runs_dir = root / "runs"

    if repetitions < 1:
        raise ValueError("repetitions must be >= 1")

    specs = _iter_run_specs(repetitions)
    print(f"Root: {root}")
    print(f"Runs dir: {target_runs_dir}")
    print(
        f"Matrix: {len(USER_STORY_IDS)} US × {len(CONDITIONS)} conditions × "
        f"{repetitions} repetitions = {len(specs)} runs"
    )
    if dry_run:
        print("Mode: dry-run (no filesystem changes)")
    print()

    if clean:
        removed = _remove_matching_runs(target_runs_dir, dry_run=dry_run)
        print(f"Cleaned matching run folders: {removed}\n")

    if not dry_run:
        target_runs_dir.mkdir(parents=True, exist_ok=True)

    counts = {
        "created": 0,
        "updated": 0,
        "skipped": 0,
        "would-create": 0,
        "would-update": 0,
    }

    # After --clean, every planned folder is (re)created from sources.
    effective_force = force or clean

    for run_id, us_id, condition, _repetition in specs:
        run_path = target_runs_dir / run_id
        action = scaffold_run(
            run_path,
            us_id,
            condition,
            root=root,
            force=effective_force,
            dry_run=dry_run,
        )
        if dry_run and clean:
            action = "would-create"
        counts[action] += 1
        if action in {"created", "updated", "would-create", "would-update"}:
            print(f"{action:12} {run_id}")

    if not dry_run:
        for run_id, us_id, condition, _repetition in specs:
            validate_run_inputs(
                RunInfo(run_id, us_id, condition, target_runs_dir / run_id)
            )

    print("\nSummary")
    for key, value in counts.items():
        if value:
            print(f"  {key}: {value}")
    print(f"  total planned: {len(specs)}")
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Scaffold clarification run folders from baselines/ and materials/. "
            f"Default matrix uses {DEFAULT_REPETITIONS} repetitions."
        )
    )
    parser.add_argument(
        "-n",
        "--repetitions",
        type=int,
        default=DEFAULT_REPETITIONS,
        help=f"Repetitions per US×condition (default: {DEFAULT_REPETITIONS})",
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Remove existing US*_COND_R* run folders before recreating them",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite input files when a run folder already exists",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show actions without writing or deleting anything",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return scaffold_all(
            repetitions=args.repetitions,
            clean=args.clean,
            force=args.force,
            dry_run=args.dry_run,
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Fatal error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
