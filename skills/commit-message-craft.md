---
name: commit-message-craft
description: Senior-level intuitive commit messages accessible to all skill levels
version: 1.0.0
---

# COMMIT MESSAGE CRAFT PROTOCOL (CMC v1.0)

## Core Principle

Every commit must be understandable by:
- **Junior developers**: WHAT changed (clear description)
- **Senior developers**: WHY it matters (professional insight)
- **Non-technical stakeholders**: IMPACT (business value)

---

## MESSAGE FORMAT

```
<type>(<scope>): <summary - what changed in plain English>

<WHY paragraph - business/technical justification>

<HOW paragraph - technical details for developers>

<IMPACT paragraph - what this enables or prevents>

---
Files changed: <count>
Risk level: LOW|MEDIUM|HIGH
Tested: <how it was verified>

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## TYPE DEFINITIONS

| Type | When to Use | Example Summary |
|------|-------------|-----------------|
| `feat` | New user-facing functionality | "Add password reset email flow" |
| `fix` | Bug correction | "Fix login timeout causing session loss" |
| `refactor` | Code restructure, no behavior change | "Simplify user validation logic" |
| `perf` | Performance improvement | "Reduce API response time by 40%" |
| `security` | Security enhancement | "Add rate limiting to prevent brute force" |
| `docs` | Documentation only | "Document API authentication flow" |
| `test` | Test additions/fixes | "Add integration tests for checkout" |
| `chore` | Build, deps, config | "Update dependencies to patch CVEs" |
| `revert` | Reverting previous commit | "Revert payment processor change" |

---

## SCOPE GUIDELINES

Scope should be the affected module/component:

```
auth        → Authentication/authorization
api         → API endpoints
ui          → User interface
db          → Database/models
config      → Configuration
deps        → Dependencies
build       → Build system
ci          → CI/CD pipeline
```

---

## WRITING THE SUMMARY LINE

### Rules:
1. Use imperative mood ("Add" not "Added" or "Adds")
2. Don't capitalize first letter after type
3. No period at the end
4. Max 72 characters total
5. Be specific, not vague

### BAD Examples:
```
fix: fixed bug                    # Too vague
feat: Updated the thing           # Wrong tense, vague
chore: stuff                      # Meaningless
feat(api): Add new endpoint.      # Has period
```

### GOOD Examples:
```
fix(auth): resolve session timeout after 30min idle
feat(api): add bulk user import endpoint
refactor(db): extract query builders into separate module
security(auth): implement TOTP two-factor authentication
```

---

## WRITING THE WHY PARAGRAPH

This explains the business or technical justification.

### Template:
```
This change addresses [problem/opportunity] which was causing [impact].
[Stakeholder/users] will benefit from [specific improvement].
```

### Example:
```
This change addresses the security vulnerability CVE-2024-1234 which
was allowing session hijacking through predictable token generation.
All users will benefit from significantly improved session security,
reducing the risk of unauthorized account access.
```

---

## WRITING THE HOW PARAGRAPH

This explains technical implementation for developers.

### Template:
```
Implementation: [approach taken]
Key changes:
- [Change 1 with file/function reference]
- [Change 2 with file/function reference]
Trade-offs: [any compromises made and why]
```

### Example:
```
Implementation: Replaced Math.random() with crypto.randomBytes() for
token generation, increasing entropy from 32 to 256 bits.
Key changes:
- src/auth/token.ts: New SecureTokenGenerator class
- src/auth/session.ts: Updated to use new generator
- tests/auth/: Added entropy validation tests
Trade-offs: Slightly slower token generation (~2ms) but negligible
for authentication flows.
```

---

## WRITING THE IMPACT PARAGRAPH

This explains what the change enables or prevents.

### Template:
```
This enables: [new capability or improvement]
This prevents: [problem or risk mitigated]
Dependencies: [any follow-up work needed]
```

### Example:
```
This enables: Secure session management meeting SOC2 requirements.
This prevents: Session hijacking attacks that could lead to data breach.
Dependencies: None - fully backward compatible with existing sessions.
```

---

## COMPLETE EXAMPLE

```
security(auth): implement cryptographic session token generation

This change addresses the security vulnerability identified in the
Q4 security audit where session tokens were generated using
predictable methods. Production users are exposed to potential
session hijacking, which could result in unauthorized data access.

Implementation: Replaced the legacy Math.random() based token
generation with Node.js crypto.randomBytes(), increasing entropy
from 32 bits to 256 bits. Added token rotation on privilege changes.
Key changes:
- src/auth/token.ts: New SecureTokenGenerator class (lines 15-89)
- src/auth/session.ts: Integrated new generator, added rotation
- tests/auth/token.test.ts: Entropy and uniqueness validation
Trade-offs: Token generation is ~2ms slower, acceptable for auth flow.

This enables: SOC2 compliant session management for enterprise clients.
This prevents: Session hijacking attacks (OWASP A07:2021).
Dependencies: None - existing sessions remain valid until expiry.

---
Files changed: 4
Risk level: MEDIUM (auth system core change)
Tested: Unit tests, integration tests, manual testing in staging

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
```

---

## ATOMIC COMMIT PRINCIPLES

### Each commit should:
1. **Be complete**: Pass all tests independently
2. **Be focused**: One logical change only
3. **Be reversible**: Can be reverted without breaking others
4. **Be understandable**: Message explains full context

### Splitting large changes:
```
WRONG: One commit with 50 files and vague message

RIGHT: Series of atomic commits:
1. refactor(db): extract user query methods
2. feat(db): add bulk operation support
3. feat(api): add bulk import endpoint
4. test(api): add bulk import integration tests
5. docs(api): document bulk import endpoint
```

---

## GIT COMMIT COMMAND FORMAT

Always use heredoc for proper formatting:

```bash
git commit -m "$(cat <<'EOF'
security(auth): implement cryptographic session token generation

This change addresses the security vulnerability identified in the
Q4 security audit where session tokens were generated using
predictable methods.

Implementation: Replaced Math.random() with crypto.randomBytes().
Key changes:
- src/auth/token.ts: New SecureTokenGenerator class
- src/auth/session.ts: Integrated new generator

This enables: SOC2 compliant session management.
This prevents: Session hijacking attacks (OWASP A07:2021).

---
Files changed: 4
Risk level: MEDIUM
Tested: Unit tests + staging verification

Co-Authored-By: Claude Opus 4.5 <noreply@anthropic.com>
EOF
)"
```

---

## INTEGRATION WITH SYNRG-COMMIT

When `/synrg-commit` is invoked, this protocol provides:
1. Analysis of changes for type/scope determination
2. Generation of WHY/HOW/IMPACT paragraphs
3. Atomic decomposition if changes span multiple concerns
4. Final message formatting and validation
