# SYNRG Extension Point Examples

This document provides concrete, implementable examples for extending each SYNRG command.

---

## 1. Adding a Custom Agent to synrg-commit.md

### Extension Point: commit-ep-002 (Sub-Agent Registry)

**Location:** Lines 224-189, Section "Sub-Agent Specifications"

**Current Agents:** 6 parallel sub-agents for analyzing commits

**Example: Security Commit Analyzer**

```markdown
<!-- EXTENSION: sub-agent-specifications -->

#### Sub-Agent 7 (Optional): Security Vulnerability Scanner

**Role**: Scan commit changes for potential security vulnerabilities

**Context Scope**: Diff content, imported packages, credential patterns

**Tools**: `Grep`, `Read`, `Bash`

**Execution**:
```javascript
async function scanSecurityVulnerabilities(diff, changedFiles) {
  const security = {
    vulnerabilities: [],
    riskScore: 0,
    recommendations: []
  };

  // Check for hardcoded credentials
  for (const file of changedFiles) {
    const content = await readFile(file);

    // Scan for secrets pattern
    const secretPatterns = [
      /password\s*=\s*["']([^"']+)["']/gi,
      /api[_-]?key\s*=\s*["']([^"']+)["']/gi,
      /token\s*=\s*["']([^"']+)["']/gi,
      /secret\s*=\s*["']([^"']+)["']/gi
    ];

    for (const pattern of secretPatterns) {
      const matches = content.match(pattern);
      if (matches) {
        security.vulnerabilities.push({
          type: 'hardcoded-secret',
          file: file,
          pattern: pattern.toString(),
          severity: 'critical'
        });
        security.riskScore += 30;
      }
    }
  }

  // Check for dependency vulnerabilities
  const hasPackageJson = changedFiles.some(f => f.includes('package.json'));
  if (hasPackageJson) {
    const auditResult = await runCommand('npm audit');
    if (auditResult.includes('critical')) {
      security.vulnerabilities.push({
        type: 'vulnerable-dependency',
        severity: 'critical'
      });
      security.riskScore += 25;
    }
  }

  return security;
}
```

**Deliverable**:
```javascript
{
  vulnerabilities: [
    {
      type: 'hardcoded-secret',
      file: 'src/api/config.ts',
      severity: 'critical',
      remediation: 'Use environment variables instead'
    }
  ],
  riskScore: 55,
  recommendations: [
    'Rotate any exposed secrets immediately',
    'Use 1Password or similar for credential management',
    'Configure pre-commit hooks to detect secrets'
  ],
  securityGatesPassed: false
}
```

**Integration:** Add to Phase 1 reconnaissance with optional trigger
```javascript
const subAgents = [
  gitDiffAnalyzer,
  contextMapper,
  intentDetector,
  qualityChecker,
  impactAssessor,
  commitHistoryAnalyzer,
  // NEW: Only if user enables security scanning
  ...(options.enableSecurityScan ? [securityScanner] : [])
];
```

**How to Activate:**
```bash
/synrg-commit --enable-security-scan
```

---

## 2. Adding a Custom Phase to synrg-refactor.md

### Extension Point: refactor-ep-003 (Phase Pipeline)

**Location:** Lines 240-250, Section "Execution Overview"

**Current Phases:** 7 phases with 9 sub-phases

**Example: Phase 2.5 - Cost Analysis**

```markdown
<!-- EXTENSION: phase-pipeline -->

## Phase 2.5: Cost-Benefit Analysis (NEW)

**Purpose**: Analyze refactoring effort vs. benefit ROI

**Trigger**: After Phase 2 (Risk Analysis) completes

**Entry Requirements**:
- Phase 2 Risk Report complete
- Refactoring Strategy defined

**Deliverable**: Cost Analysis Report

**Exit Condition**: Cost-benefit assessment complete

### Execution Protocol

```javascript
async function executeCostAnalysisPhase(riskReport, strategy) {
  const costAnalysis = {
    estimatedEffort: calculateEffort(strategy),
    expectedBenefits: calculateBenefits(riskReport, strategy),
    roi: 0,
    recommendation: ''
  };

  // Calculate effort
  const developmentHours = strategy.batches.reduce((sum, batch) => {
    return sum + (batch.files.length * batch.averageHoursPerFile);
  }, 0);

  const validationHours = riskReport.validationHours;
  const reviewHours = strategy.batches.length * 2;

  costAnalysis.estimatedEffort = {
    development: developmentHours,
    validation: validationHours,
    review: reviewHours,
    total: developmentHours + validationHours + reviewHours,
    estimatedCost: (developmentHours + validationHours + reviewHours) * teamHourlyRate
  };

  // Calculate benefits
  costAnalysis.expectedBenefits = {
    maintenanceSavings: riskReport.codeSmells * 5, // 5 hours per smell over 2 years
    performanceImprovement: riskReport.performanceGains,
    developerProductivity: strategy.modules.length * 10, // 10 hours per module saved
    defectReduction: riskReport.defectRisk * 10,
    totalBenefits: (riskReport.codeSmells * 5) + riskReport.performanceGains + (strategy.modules.length * 10)
  };

  // Calculate ROI
  costAnalysis.roi = {
    breakEvenMonths: costAnalysis.estimatedEffort.total / costAnalysis.expectedBenefits.totalBenefits,
    yearlySavings: (costAnalysis.expectedBenefits.totalBenefits - costAnalysis.estimatedEffort.total),
    recommendation: costAnalysis.roi.yearlySavings > 0 ? 'Proceed' : 'Reconsider'
  };

  return costAnalysis;
}
```

**Output Report Example**:
```markdown
## Cost-Benefit Analysis Report

### Estimated Effort
- Development: 120 hours
- Validation: 40 hours
- Review: 8 hours
- **Total: 168 hours ($8,400 at $50/hour)**

### Expected Benefits (Over 2 Years)
- Maintenance savings: 320 hours
- Developer productivity: 180 hours
- Defect reduction: 120 hours
- **Total: 620 hours ($31,000 in value)**

### ROI
- Break-even: 2.8 months
- Yearly savings: $11,300
- **Recommendation: PROCEED - Strong ROI**
```

**Integration into User Approval**:
```javascript
// In Phase 3.5 (User Approval)
displayRefactoringStrategy(strategy);
displayCostAnalysis(costAnalysis); // NEW

const approval = await askForApproval([
  'Approve entire plan',
  'Approve up to Phase C (cost: $4,200)',
  'Reconsider based on cost'
]);
```

---

## 3. Adding a Custom Template to synrg-spec.md

### Extension Point: spec-ep-004 (Specification Template)

**Location:** Lines 1263-1532, Section "Specification Template"

**Current Templates:** General specification format

**Example: API Specification Template**

```markdown
<!-- EXTENSION: specification-templates -->

## API Specification Template

**Purpose**: Define REST/GraphQL API specifications for backend services

**When to Use**: When feature requires API development

**Template**:

```yaml
---
type: specification
phase: specify
status: in-progress
apiType: rest  # or graphql, grpc
targetVersion: 1.0.0
upstream_hashes:
  constitution: "sha256-abc123..."
---

# API Specification: [Feature Name]

## API Overview

### Base URL
- Development: `https://api.dev.example.com/v1`
- Production: `https://api.example.com/v1`

### Authentication
- Type: [JWT | OAuth2 | API Key]
- Header: `Authorization: Bearer {token}`

## Endpoints

### GET /[resource]
**Purpose**: Retrieve list of [resource]

**Request Parameters**:
- `limit` (integer, optional): Max 100, default 10
- `offset` (integer, optional): Default 0
- `sort` (string, optional): Field name

**Response (200 OK)**:
```json
{
  "data": [
    {
      "id": "uuid",
      "field": "value"
    }
  ],
  "pagination": {
    "total": 100,
    "limit": 10,
    "offset": 0
  }
}
```

**Error Responses**:
- 400: Bad request
- 401: Unauthorized
- 403: Forbidden
- 500: Server error

### POST /[resource]
**Purpose**: Create new [resource]

**Request Body**:
```json
{
  "field1": "value",
  "field2": "value"
}
```

**Response (201 Created)**:
```json
{
  "id": "uuid",
  "field1": "value",
  "field2": "value",
  "createdAt": "2026-01-09T00:00:00Z"
}
```

## Error Handling

### Standard Error Format
```json
{
  "error": {
    "code": "INVALID_REQUEST",
    "message": "Human-readable message",
    "details": {
      "field": "field_name",
      "issue": "Specific issue"
    }
  }
}
```

### Rate Limiting
- Limit: 1000 requests/hour
- Header: `X-RateLimit-Remaining`

## Changelog
- **v1.0.0** (2026-01-09): Initial release
```

**Success Criteria for API Specs**:
- [ ] All endpoints documented with HTTP method, path, parameters
- [ ] All response formats defined with examples
- [ ] Error responses for all status codes
- [ ] Authentication method clearly specified
- [ ] Rate limiting documented
- [ ] Backward compatibility strategy defined

---

## 4. Adding a Custom Validator to synrg-commit.md

### Extension Point: commit-ep-004 (Validation Rules)

**Location:** Lines 955-985, Section "Pre-Commit Validation"

**Current Validators:** Tests, lint, type-check, security, build

**Example: Changelog Validator**

```javascript
<!-- EXTENSION: pre-commit-validators -->

async function runChangelogValidation(commits, quality) {
  const validation = {
    changelogUpdated: false,
    entryFormat: 'valid',
    versionBump: false,
    breakingChangeDocumented: false,
    allGatesPassed: false
  };

  // Check if CHANGELOG.md was updated
  const files = commits.flatMap(c => c.files);
  if (!files.some(f => f === 'CHANGELOG.md')) {
    return {
      canProceed: false,
      validation,
      blockers: [
        'CHANGELOG.md not updated',
        'Add entry describing changes in CHANGELOG.md'
      ]
    };
  }

  // Validate CHANGELOG format
  const changelogContent = await readFile('CHANGELOG.md');

  // Check for proper entry format (Keep a Changelog format)
  const hasNewEntry = changelogContent.includes(`## [${getNextVersion()}]`);
  if (!hasNewEntry) {
    validation.entryFormat = 'invalid';
    return {
      canProceed: false,
      validation,
      blockers: [
        'CHANGELOG entry not in correct format',
        'Use format: ## [X.Y.Z] - YYYY-MM-DD'
      ]
    };
  }

  // Check if version was bumped
  const packageJson = JSON.parse(await readFile('package.json'));
  validation.versionBump = isVersionBumped(packageJson.version);

  // Check if breaking changes are documented
  if (commits.some(c => c.message.includes('BREAKING CHANGE'))) {
    validation.breakingChangeDocumented = changelogContent.includes('### Breaking Changes');
  }

  validation.allGatesPassed =
    validation.changelogUpdated &&
    validation.entryFormat === 'valid' &&
    validation.versionBump &&
    !commits.some(c => c.message.includes('BREAKING CHANGE') && !validation.breakingChangeDocumented);

  return {
    canProceed: validation.allGatesPassed,
    validation,
    blockers: validation.allGatesPassed ? [] : [
      !validation.changelogUpdated && 'CHANGELOG.md not updated',
      validation.entryFormat !== 'valid' && 'CHANGELOG entry format invalid',
      !validation.versionBump && 'Version not bumped in package.json',
      commits.some(c => c.message.includes('BREAKING CHANGE') && !validation.breakingChangeDocumented) && 'Breaking changes not documented in CHANGELOG'
    ].filter(Boolean)
  };
}
```

**Integration**:
```javascript
// In Phase 3: Validation & Execution
const validation = {
  testsPass: quality.testsPassing,
  lintPass: quality.lintStatus !== 'errors',
  typeCheckPass: quality.typeErrors === 0,
  securityPass: quality.securityIssues.filter(i => i.severity === 'critical').length === 0,
  buildPass: true,
  changelogPass: (await runChangelogValidation(commits)).allGatesPassed  // NEW
};
```

---

## 5. Adding Custom Questions to synrg-scaffold.md

### Extension Point: scaffold-ep-002 (Project Type Questions)

**Location:** Lines 159-266, Section "Phase 1: Project Type Discovery"

**Current Types:** 8 project types

**Example: Adding Blockchain Project Type**

```markdown
<!-- EXTENSION: project-type-questions -->

Add to existing options:

{
  label: "Blockchain/Smart Contracts",
  description: "Smart contracts, DeFi protocols, or blockchain-based applications"
}
```

Then create Phase 2 questions for blockchain projects:

```markdown
<!-- EXTENSION: adaptive-questions -->

### 2.9: Blockchain Project Questions

If `projectType === "Blockchain/Smart Contracts"`:

```javascript
AskUserQuestion({
  questions: [
    {
      question: "What blockchain network(s) are you targeting?",
      header: "Blockchain",
      multiSelect: true,
      options: [
        { label: "Ethereum", description: "EVM-compatible, largest ecosystem" },
        { label: "Solana", description: "High-speed, low-cost transactions" },
        { label: "Polygon", description: "Ethereum sidechain/L2" },
        { label: "Near", description: "Sharded, developer-friendly" },
        { label: "Cosmos", description: "Multi-chain IBC protocol" }
      ]
    },
    {
      question: "What smart contract language(s)?",
      header: "Contract Language",
      multiSelect: true,
      options: [
        { label: "Solidity", description: "EVM-based contracts" },
        { label: "Rust", description: "Solana/Cosmos programs" },
        { label: "Vyper", description: "Python-like EVM language" },
        { label: "Move", description: "Aptos/Sui contracts" }
      ]
    },
    {
      question: "What smart contract framework(s)?",
      header: "Framework",
      multiSelect: true,
      options: [
        { label: "Hardhat", description: "Ethereum dev environment" },
        { label: "Foundry", description: "Rust-based Ethereum dev" },
        { label: "OpenZeppelin", description: "Standard contracts library" },
        { label: "Anchor", description: "Solana framework" }
      ]
    },
    {
      question: "Do you need on-chain or off-chain storage?",
      header: "Storage",
      multiSelect: false,
      options: [
        { label: "On-chain", description: "Data stored in blockchain" },
        { label: "Off-chain", description: "IPFS, Arweave, or databases" },
        { label: "Hybrid", description: "Both on-chain and off-chain" }
      ]
    }
  ]
})
```

**Storage responses:**
- `blockchainNetworks` (array)
- `contractLanguages` (array)
- `contractFramework` (array)
- `storageType`

---

## 6. Extending Validation Rules in synrg-spec.md

### Extension Point: spec-ep-002 (Phase Gate Validators)

**Location:** Lines 172-177, Section "Phase Gate Validation Rules"

**Current Validators:** Artifact exists, status check, pending items

**Example: Security Review Gate**

```markdown
<!-- EXTENSION: phase-gate-validators -->

## Phase 4 (PLAN) Entry - Add Security Review Gate

Before entering PLAN phase, check:

```javascript
async function validateSecurityReviewGate(specDir) {
  // Check if spec.md mentions security requirements
  const specContent = readFile(`${specDir}/spec.md`);

  const securityTerms = [
    'security',
    'authentication',
    'authorization',
    'encryption',
    'compliance',
    'privacy'
  ];

  const hasSecurityRequirements = securityTerms.some(term =>
    specContent.toLowerCase().includes(term)
  );

  if (hasSecurityRequirements) {
    // Check if security review has been performed
    const reviewFile = `${specDir}/security-review.md`;

    if (!fileExists(reviewFile)) {
      return {
        allowed: false,
        reason: 'Specification mentions security requirements but no security review found',
        remediation: 'Run security review: run security-review-agent'
      };
    }

    const reviewContent = readFile(reviewFile);
    if (!reviewContent.includes('status: complete')) {
      return {
        allowed: false,
        reason: 'Security review incomplete',
        remediation: 'Complete security review before proceeding to PLAN phase'
      };
    }
  }

  return { allowed: true };
}
```

**Integration**:
```javascript
function canEnterPhase(phase, specDir) {
  const requirements = PHASE_REQUIREMENTS[phase];

  // ... existing checks ...

  // NEW: Security review gate for PLAN phase
  if (phase === 'plan') {
    const securityGate = await validateSecurityReviewGate(specDir);
    if (!securityGate.allowed) {
      return securityGate;
    }
  }

  return { allowed: true };
}
```

---

## Implementation Checklist for Extensions

When implementing a new extension:

- [ ] Identify the SYNRG command to extend
- [ ] Locate the exact extension point (line numbers)
- [ ] Use the appropriate marker format: `<!-- EXTENSION: type-name -->`
- [ ] Create agent file if adding agents (in ~/.claude/agents/)
- [ ] Create supporting files (templates, validators, etc.)
- [ ] Update the extension manifest
- [ ] Test the extension with real scenarios
- [ ] Document the extension in the EXTENSION_GUIDE.md
- [ ] Update related documentation
- [ ] Create example usage in project docs

---

## Testing Your Extension

```bash
# Test an agent extension
/synrg --test-extension agent-name

# Test a template extension
/synrg-spec --validate-template template-name

# Test a validator extension
/synrg-commit --test-validator validator-name

# Test a question set extension
/synrg-scaffold --test-questions question-set-name
```

---

## Support & Resources

- **Full Extension Analysis:** `EXTENSION_POINTS_ANALYSIS.yaml`
- **Summary:** `EXTENSION_POINTS_SUMMARY.md`
- **Framework Guide:** (To be created)
- **API Reference:** (To be created)
