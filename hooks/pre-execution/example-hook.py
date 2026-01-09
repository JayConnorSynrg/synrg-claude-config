#!/usr/bin/env python3
"""
SYNRG Pre-Execution Hook Example
================================

This hook runs before any SYNRG command executes.
Use it for:
- Environment validation
- Pre-requisite checks
- Logging/auditing
- Custom setup

Arguments:
    argv[1]: OBJECTIVE - The user's objective string
    argv[2]: COMMAND_NAME - Which SYNRG command is running

Return codes:
    0 - Success, continue execution
    1 - Failure, abort execution (if failure_action=abort)
"""

import sys
import os
from datetime import datetime


def validate_environment():
    """Check that required environment is set up."""
    required_dirs = [
        os.path.expanduser("~/.claude/commands"),
        os.path.expanduser("~/.claude/agents"),
        os.path.expanduser("~/.claude/skills"),
    ]

    missing = [d for d in required_dirs if not os.path.isdir(d)]
    if missing:
        print(f"[WARN] Missing directories: {missing}")
        return False
    return True


def log_execution(objective: str, command: str):
    """Log execution start for auditing."""
    log_file = os.path.expanduser("~/.claude/hooks/execution.log")
    timestamp = datetime.now().isoformat()

    log_entry = f"{timestamp} | {command} | {objective[:100]}...\n"

    try:
        with open(log_file, "a") as f:
            f.write(log_entry)
    except IOError:
        pass  # Non-critical, don't fail


def main():
    # Parse arguments
    objective = sys.argv[1] if len(sys.argv) > 1 else ""
    command = sys.argv[2] if len(sys.argv) > 2 else "unknown"

    print(f"[PRE-HOOK] Starting: {command}")
    print(f"[PRE-HOOK] Objective: {objective[:80]}...")

    # Validate environment
    if not validate_environment():
        print("[PRE-HOOK] Environment validation failed")
        # Return 0 anyway to not block execution
        # Change to return 1 to enforce strict validation

    # Log execution
    log_execution(objective, command)

    print("[PRE-HOOK] Pre-execution checks complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
