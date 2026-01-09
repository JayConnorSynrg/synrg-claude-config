#!/usr/bin/env python3
"""
SYNRG Post-Execution Hook Example
=================================

This hook runs after a SYNRG command completes.
Use it for:
- Cleanup operations
- Metrics collection
- Notification sending
- State persistence

Arguments:
    argv[1]: OBJECTIVE - The user's objective string
    argv[2]: COMMAND_NAME - Which SYNRG command ran
    argv[3]: EXIT_CODE - How the command exited (0=success)

Return codes:
    0 - Success
    Non-zero - Logged but doesn't affect execution (already complete)
"""

import sys
import os
from datetime import datetime
import json


def collect_metrics(command: str, exit_code: int):
    """Collect execution metrics."""
    metrics_file = os.path.expanduser("~/.claude/hooks/metrics.json")

    # Load existing metrics
    metrics = {"total_executions": 0, "by_command": {}, "success_rate": 0}
    if os.path.exists(metrics_file):
        try:
            with open(metrics_file, "r") as f:
                metrics = json.load(f)
        except (IOError, json.JSONDecodeError):
            pass

    # Update metrics
    metrics["total_executions"] = metrics.get("total_executions", 0) + 1

    if command not in metrics["by_command"]:
        metrics["by_command"][command] = {"total": 0, "success": 0}

    metrics["by_command"][command]["total"] += 1
    if exit_code == 0:
        metrics["by_command"][command]["success"] += 1

    # Calculate success rate
    total_success = sum(c["success"] for c in metrics["by_command"].values())
    metrics["success_rate"] = round(
        total_success / metrics["total_executions"] * 100, 2
    )

    # Save metrics
    try:
        with open(metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)
    except IOError:
        pass


def log_completion(objective: str, command: str, exit_code: int):
    """Log execution completion."""
    log_file = os.path.expanduser("~/.claude/hooks/execution.log")
    timestamp = datetime.now().isoformat()
    status = "SUCCESS" if exit_code == 0 else f"FAILED({exit_code})"

    log_entry = f"{timestamp} | {command} | {status} | {objective[:100]}...\n"

    try:
        with open(log_file, "a") as f:
            f.write(log_entry)
    except IOError:
        pass


def main():
    # Parse arguments
    objective = sys.argv[1] if len(sys.argv) > 1 else ""
    command = sys.argv[2] if len(sys.argv) > 2 else "unknown"
    exit_code = int(sys.argv[3]) if len(sys.argv) > 3 else 0

    print(f"[POST-HOOK] Completed: {command}")
    print(f"[POST-HOOK] Exit code: {exit_code}")

    # Collect metrics
    collect_metrics(command, exit_code)

    # Log completion
    log_completion(objective, command, exit_code)

    print("[POST-HOOK] Post-execution complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
