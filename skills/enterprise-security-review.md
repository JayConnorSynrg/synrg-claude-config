---
name: enterprise-security-review
description: Enterprise-level security validation for all code changes
version: 1.0.0
---

# ENTERPRISE SECURITY REVIEW PROTOCOL (ESR v1.0)

## Mandatory Security Gate

This gate MUST be passed before ANY code change is approved.

---

## 5-POINT SECURITY VALIDATION

### 1. SECRETS DETECTION (Critical)

```
SCAN ALL CHANGED CODE FOR:

□ Hardcoded API keys
  Pattern: /[a-zA-Z0-9_-]{20,}/
  Common prefixes: sk-, pk-, api_, apikey, API_KEY

□ Passwords and credentials
  Pattern: password|passwd|pwd|secret|credential
  Check: Not in strings, env vars, or config

□ Private keys and certificates
  Pattern: -----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----
  Check: No .pem, .key files in commits

□ Connection strings with credentials
  Pattern: ://[^:]+:[^@]+@
  Check: No embedded passwords in URLs

□ AWS/Cloud credentials
  Pattern: AKIA[0-9A-Z]{16}, aws_secret_access_key
  Check: No cloud provider secrets

SEVERITY: CRITICAL - Block if found
ACTION: Remove secret, use environment variable
```

### 2. OWASP TOP 10 SCAN (High)

```
CHECK FOR VULNERABILITY PATTERNS:

□ SQL Injection (A03:2021)
  BAD:  query = f"SELECT * FROM users WHERE id = {user_input}"
  GOOD: cursor.execute("SELECT * FROM users WHERE id = ?", (user_input,))

□ XSS - Cross-Site Scripting (A03:2021)
  BAD:  innerHTML = userInput
  GOOD: textContent = userInput OR sanitize(userInput)

□ Command Injection (A03:2021)
  BAD:  os.system(f"ls {user_input}")
  GOOD: subprocess.run(["ls", user_input], shell=False)

□ Path Traversal (A01:2021)
  BAD:  open(user_provided_path)
  GOOD: open(os.path.join(BASE_DIR, os.path.basename(path)))

□ Insecure Deserialization (A08:2021)
  BAD:  pickle.loads(user_data)
  GOOD: json.loads(user_data) with schema validation

□ SSRF - Server-Side Request Forgery (A10:2021)
  BAD:  requests.get(user_provided_url)
  GOOD: Validate URL against allowlist before request

SEVERITY: HIGH - Require fix before approval
ACTION: Implement secure alternative pattern
```

### 3. PRIVILEGE ESCALATION CHECK (High)

```
VERIFY NO UNAUTHORIZED PRIVILEGE CHANGES:

□ Sudo/Admin operations
  Check: No sudo, admin, root without explicit user approval
  Required: Document why privilege needed

□ File permission changes
  Check: No chmod 777, no world-writable files
  Required: Minimum necessary permissions

□ Service account usage
  Check: No service account credentials in code
  Required: Use IAM roles or secrets manager

□ Database admin operations
  Check: No DROP, TRUNCATE, ALTER without approval
  Required: Migration scripts with rollback

□ Network/Firewall changes
  Check: No port opens, rule changes without review
  Required: Security team approval for network changes

SEVERITY: HIGH - Require explicit approval
ACTION: Document justification, get user sign-off
```

### 4. DEPENDENCY SECURITY (Medium)

```
CHECK ALL NEW DEPENDENCIES:

□ Known vulnerabilities
  Tool: npm audit, pip-audit, safety check
  Action: No HIGH/CRITICAL vulnerabilities

□ Maintainer reputation
  Check: Active maintenance, known maintainers
  Flag: Unmaintained (>1 year), unknown authors

□ License compatibility
  Check: License compatible with project
  Flag: GPL in proprietary, unclear licensing

□ Supply chain integrity
  Check: Package hash matches expected
  Action: Use lock files, verify integrity

□ Transitive dependencies
  Check: Review what dependencies bring in
  Flag: Excessive transitive deps, known bad actors

SEVERITY: MEDIUM - Warn and document
ACTION: Evaluate alternatives if concerns found
```

### 5. DATA PROTECTION (Medium)

```
VERIFY DATA HANDLING:

□ PII handling
  Check: Personal data encrypted at rest and transit
  Required: No PII in logs, limited access

□ Log sanitization
  Check: No sensitive data in log output
  Pattern: Remove passwords, tokens, PII before logging

□ Error message safety
  Check: Errors don't leak internal details
  BAD:  return {"error": str(exception)}
  GOOD: return {"error": "An error occurred", "code": "E001"}

□ Data retention
  Check: Data deleted when no longer needed
  Required: Retention policy compliance

□ Access control
  Check: Proper authorization checks
  Required: Verify user has permission before action

SEVERITY: MEDIUM - Document and remediate
ACTION: Implement proper data handling
```

---

## SECURITY REVIEW WORKFLOW

```
┌─────────────────────────────────────────────────────────────────────────────┐
│ ENTERPRISE SECURITY GATE                                                     │
│                                                                              │
│ For EACH code change, complete:                                              │
│                                                                              │
│ Step 1: Secrets Scan                                                         │
│   □ Run: grep -rE "(password|secret|api.?key|token)" on changes             │
│   □ Result: PASS / FAIL                                                      │
│                                                                              │
│ Step 2: OWASP Pattern Check                                                  │
│   □ Review each change for injection patterns                                │
│   □ Result: PASS / FAIL / NEEDS_FIX                                          │
│                                                                              │
│ Step 3: Privilege Review                                                     │
│   □ Any admin/sudo/elevated operations?                                      │
│   □ Result: PASS / NEEDS_APPROVAL                                            │
│                                                                              │
│ Step 4: Dependency Audit (if new deps)                                       │
│   □ Run security audit on new packages                                       │
│   □ Result: PASS / WARN / FAIL                                               │
│                                                                              │
│ Step 5: Data Protection Check                                                │
│   □ Any PII/sensitive data handling?                                         │
│   □ Result: PASS / NEEDS_REVIEW                                              │
│                                                                              │
│ FINAL: All PASS → Proceed                                                    │
│        Any FAIL → Block and fix                                              │
│        Any WARN → Document and proceed with caution                          │
│        Any NEEDS_* → Get required approval                                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## QUICK REFERENCE COMMANDS

```bash
# Secrets scan
grep -rE "(password|secret|api.?key|token|credential)" --include="*.{js,ts,py,json,yaml,yml}" .

# Check for eval/exec patterns
grep -rE "(eval\(|exec\(|system\(|shell=True)" --include="*.{js,ts,py}" .

# Check for SQL injection patterns
grep -rE "(\"|').*\+.*(\"|')|f\".*\{.*\}.*\"|f'.*\{.*\}'.*" --include="*.py" .

# npm security audit
npm audit --audit-level=high

# Python security check
pip-audit || safety check

# Check file permissions in repo
find . -perm -002 -type f  # World-writable files
```

---

## INTEGRATION POINTS

This protocol is triggered:
1. In PRE_IMPLEMENTATION_REVIEW - before any code change
2. In POST_IMPLEMENTATION_REVIEW - after changes complete
3. By synrg-security-gate.py hook - automated enforcement
4. During /synrg-commit - before commit approval
