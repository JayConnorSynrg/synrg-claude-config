#!/usr/bin/env python3
"""
SYNRG Security Gate Hook for Claude Code
Enterprise-level security validation before code changes.

Triggers on: Edit, Write, MultiEdit
Purpose: Scan for secrets, OWASP patterns, and privilege escalation
Exit codes:
  0 - Allow (passed security check)
  2 - Block (security issue found)
"""

import json
import os
import re
import sys
from datetime import datetime

DEBUG_LOG_FILE = "/tmp/synrg-security-gate-log.txt"


def debug_log(message):
    """Append debug message to log file."""
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(DEBUG_LOG_FILE, "a") as f:
            f.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass


# Security patterns to detect
SECURITY_PATTERNS = {
    "secrets": {
        "severity": "CRITICAL",
        "patterns": [
            (r'["\']?(?:api[_-]?key|apikey)["\']?\s*[:=]\s*["\'][a-zA-Z0-9_\-]{20,}["\']', "Hardcoded API key detected"),
            (r'["\']?(?:password|passwd|pwd)["\']?\s*[:=]\s*["\'][^"\']{4,}["\']', "Hardcoded password detected"),
            (r'["\']?(?:secret|token)["\']?\s*[:=]\s*["\'][a-zA-Z0-9_\-]{16,}["\']', "Hardcoded secret/token detected"),
            (r'-----BEGIN\s+(?:RSA\s+)?PRIVATE\s+KEY-----', "Private key detected in code"),
            (r'AKIA[0-9A-Z]{16}', "AWS Access Key ID detected"),
            (r'(?:ghp|gho|ghu|ghs|ghr)_[a-zA-Z0-9]{36}', "GitHub token detected"),
            (r'sk-[a-zA-Z0-9]{48}', "OpenAI API key detected"),
            (r'xox[baprs]-[a-zA-Z0-9\-]{10,}', "Slack token detected"),
        ]
    },
    "injection": {
        "severity": "HIGH",
        "patterns": [
            (r'eval\s*\([^)]*\$|eval\s*\([^)]*\+', "Potential eval injection"),
            (r'exec\s*\([^)]*\$|exec\s*\([^)]*\+', "Potential exec injection"),
            (r'os\.system\s*\([^)]*\+|os\.system\s*\([^)]*f["\']', "Potential OS command injection"),
            (r'shell\s*=\s*True', "Shell=True in subprocess (potential injection)"),
            (r'innerHTML\s*=\s*[^;]*\+|innerHTML\s*=\s*[^;]*\$', "Potential XSS via innerHTML"),
            (r'document\.write\s*\([^)]*\+', "Potential XSS via document.write"),
            (r'\.query\s*\([^)]*\+[^)]*\)|\.query\s*\(f["\']', "Potential SQL injection"),
            (r'\.execute\s*\([^)]*\+[^)]*\)|\.execute\s*\(f["\']', "Potential SQL injection"),
        ]
    },
    "privilege": {
        "severity": "MEDIUM",
        "patterns": [
            (r'sudo\s+', "Sudo command detected - verify authorization"),
            (r'chmod\s+777', "World-writable permissions detected"),
            (r'chmod\s+666', "World-readable/writable permissions detected"),
            (r'as\s+root|--user\s*=?\s*root', "Root user operation detected"),
        ]
    }
}

# State management for warnings shown
def get_state_file(session_id):
    return os.path.expanduser(f"~/.claude/session-env/security_warnings_{session_id}.json")


def load_state(session_id):
    state_file = get_state_file(session_id)
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                return set(json.load(f))
        except (json.JSONDecodeError, IOError):
            return set()
    return set()


def save_state(session_id, shown_warnings):
    state_file = get_state_file(session_id)
    try:
        os.makedirs(os.path.dirname(state_file), exist_ok=True)
        with open(state_file, "w") as f:
            json.dump(list(shown_warnings), f)
    except IOError:
        pass


def extract_content(tool_name, tool_input):
    """Extract content to scan from tool input."""
    if tool_name == "Write":
        return tool_input.get("content", "")
    elif tool_name == "Edit":
        return tool_input.get("new_string", "")
    elif tool_name == "MultiEdit":
        edits = tool_input.get("edits", [])
        return " ".join(edit.get("new_string", "") for edit in edits)
    return ""


def scan_content(content, file_path):
    """Scan content for security patterns."""
    findings = []

    for category, config in SECURITY_PATTERNS.items():
        for pattern, message in config["patterns"]:
            try:
                if re.search(pattern, content, re.IGNORECASE):
                    findings.append({
                        "category": category,
                        "severity": config["severity"],
                        "message": message,
                        "file": file_path
                    })
            except re.error:
                debug_log(f"Regex error in pattern: {pattern}")

    return findings


def format_security_report(findings):
    """Format findings into a security report."""
    if not findings:
        return None

    # Group by severity
    critical = [f for f in findings if f["severity"] == "CRITICAL"]
    high = [f for f in findings if f["severity"] == "HIGH"]
    medium = [f for f in findings if f["severity"] == "MEDIUM"]

    report_lines = [
        "",
        "=" * 70,
        "SYNRG ENTERPRISE SECURITY GATE - FINDINGS DETECTED",
        "=" * 70,
        ""
    ]

    if critical:
        report_lines.append("CRITICAL ISSUES (Must fix before proceeding):")
        for f in critical:
            report_lines.append(f"  - [{f['category'].upper()}] {f['message']}")
            report_lines.append(f"    File: {f['file']}")
        report_lines.append("")

    if high:
        report_lines.append("HIGH SEVERITY ISSUES (Strongly recommended to fix):")
        for f in high:
            report_lines.append(f"  - [{f['category'].upper()}] {f['message']}")
            report_lines.append(f"    File: {f['file']}")
        report_lines.append("")

    if medium:
        report_lines.append("MEDIUM SEVERITY ISSUES (Review recommended):")
        for f in medium:
            report_lines.append(f"  - [{f['category'].upper()}] {f['message']}")
            report_lines.append(f"    File: {f['file']}")
        report_lines.append("")

    report_lines.extend([
        "-" * 70,
        "ACTION REQUIRED:",
        "  - Review each finding and address security concerns",
        "  - Remove hardcoded secrets and use environment variables",
        "  - Use parameterized queries and safe execution patterns",
        "-" * 70,
        ""
    ])

    return "\n".join(report_lines)


def main():
    # Check if security gate is enabled
    if os.environ.get("SYNRG_SECURITY_GATE_DISABLED", "0") == "1":
        sys.exit(0)

    # Read input
    try:
        raw_input = sys.stdin.read()
        input_data = json.loads(raw_input)
    except json.JSONDecodeError as e:
        debug_log(f"JSON decode error: {e}")
        sys.exit(0)

    session_id = input_data.get("session_id", "default")
    tool_name = input_data.get("tool_name", "")
    tool_input = input_data.get("tool_input", {})

    # Only process file modification tools
    if tool_name not in ["Edit", "Write", "MultiEdit"]:
        sys.exit(0)

    file_path = tool_input.get("file_path", "")
    content = extract_content(tool_name, tool_input)

    if not content:
        sys.exit(0)

    # Scan for security issues
    findings = scan_content(content, file_path)

    if findings:
        # Check if we've already warned about these in this session
        shown_warnings = load_state(session_id)
        warning_key = f"{file_path}-{hash(tuple(f['message'] for f in findings))}"

        if warning_key not in shown_warnings:
            shown_warnings.add(warning_key)
            save_state(session_id, shown_warnings)

            report = format_security_report(findings)
            print(report, file=sys.stderr)

            # Block on CRITICAL findings
            if any(f["severity"] == "CRITICAL" for f in findings):
                debug_log(f"BLOCKED: Critical security issue in {file_path}")
                sys.exit(2)

    # Allow tool to proceed
    sys.exit(0)


if __name__ == "__main__":
    main()
