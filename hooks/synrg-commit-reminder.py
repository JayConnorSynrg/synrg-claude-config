#!/usr/bin/env python3
"""
SYNRG Commit Reminder Hook for Claude Code
Detects uncommitted changes at session end and reminds about commit workflow.

Triggers on: Stop (session end)
Purpose: Ensure proper commit workflow is followed
"""

import json
import os
import subprocess
import sys
from datetime import datetime

DEBUG_LOG_FILE = "/tmp/synrg-commit-reminder-log.txt"


def debug_log(message):
    """Append debug message to log file."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DEBUG_LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass


def get_git_status():
    """Check for uncommitted changes in git."""
    try:
        # Check if we're in a git repo
        result = subprocess.run(
            ["git", "rev-parse", "--is-inside-work-tree"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        if result.returncode != 0:
            return None, None

        # Get status
        status_result = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )

        if status_result.returncode != 0:
            return None, None

        # Parse status
        lines = status_result.stdout.strip().split("\n") if status_result.stdout.strip() else []

        staged = []
        unstaged = []

        for line in lines:
            if not line:
                continue
            status = line[:2]
            filename = line[3:]

            if status[0] != " " and status[0] != "?":
                staged.append(filename)
            if status[1] != " ":
                unstaged.append(filename)

        return staged, unstaged

    except Exception as e:
        debug_log(f"Error checking git status: {e}")
        return None, None


def get_current_branch():
    """Get current git branch name."""
    try:
        result = subprocess.run(
            ["git", "branch", "--show-current"],
            capture_output=True,
            text=True,
            cwd=os.getcwd()
        )
        return result.stdout.strip() if result.returncode == 0 else None
    except Exception:
        return None


def format_reminder(staged, unstaged, branch):
    """Format the commit reminder message."""
    lines = [
        "",
        "=" * 70,
        "SYNRG COMMIT WORKFLOW REMINDER",
        "=" * 70,
        "",
        f"Current branch: {branch or 'unknown'}",
        ""
    ]

    total_changes = len(staged) + len(unstaged)

    if staged:
        lines.append(f"Staged changes ({len(staged)} files):")
        for f in staged[:5]:
            lines.append(f"  + {f}")
        if len(staged) > 5:
            lines.append(f"  ... and {len(staged) - 5} more")
        lines.append("")

    if unstaged:
        lines.append(f"Unstaged changes ({len(unstaged)} files):")
        for f in unstaged[:5]:
            lines.append(f"  M {f}")
        if len(unstaged) > 5:
            lines.append(f"  ... and {len(unstaged) - 5} more")
        lines.append("")

    lines.extend([
        "-" * 70,
        "RECOMMENDED ACTIONS:",
        "",
        "  Option 1: Use /synrg-commit for guided commit workflow",
        "            Provides atomic commit decomposition and",
        "            senior-level commit messages",
        "",
        "  Option 2: Manual commit following COMMIT_MESSAGE protocol",
        "            git add <files>",
        '            git commit -m "<type>(<scope>): <summary>"',
        "",
        f"  Note: {total_changes} file(s) have uncommitted changes",
        "-" * 70,
        ""
    ])

    return "\n".join(lines)


def main():
    # Check if reminder is enabled
    if os.environ.get("SYNRG_COMMIT_REMINDER_DISABLED", "0") == "1":
        sys.exit(0)

    # Read input (Stop hook gets session info)
    try:
        raw_input = sys.stdin.read()
        input_data = json.loads(raw_input) if raw_input else {}
    except json.JSONDecodeError:
        input_data = {}

    # Check git status
    staged, unstaged = get_git_status()

    # If not in git repo or no changes, exit silently
    if staged is None or (not staged and not unstaged):
        sys.exit(0)

    # Get branch info
    branch = get_current_branch()

    # Format and display reminder
    reminder = format_reminder(staged, unstaged, branch)
    print(reminder, file=sys.stderr)

    debug_log(f"Reminded about {len(staged)} staged, {len(unstaged)} unstaged files")

    # Don't block - just remind
    sys.exit(0)


if __name__ == "__main__":
    main()
