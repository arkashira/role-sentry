# Product Requirements Document (PRD) – role‑sentry

---

## 1. Executive Summary  

**Product name:** *role‑sentry*  
**Repository:** `arkashira/role-sentry`  
**Verdict:** New product – addresses a unique pain point in Postgres role permission management that is not covered by any existing Axentx offering.  

**Goal:** Deliver a lightweight, declarative, and auditable role‑permission management tool for Postgres that reduces human error, speeds up onboarding, and provides real‑time compliance reporting.

---

## 2. Problem Statement  

PostgreSQL users and roles are traditionally managed via ad‑hoc SQL scripts or manual `GRANT`/`REVOKE` commands. This approach suffers from:

| Pain | Impact |
|------|--------|
| **Human error** – typos or missing revocations lead to privilege creep. | Security breaches, accidental data exposure. |
| **Lack of auditability** – no single source of truth for who has what permission. | Compliance violations, difficulty in forensic analysis. |
| **Slow onboarding** – new developers or DBAs must learn complex SQL syntax and navigate legacy scripts. | Reduced productivity, increased support tickets. |
| **Inconsistent environments** – dev, test, and prod roles drift apart. | Hard to reproduce bugs, fragile CI pipelines. |

Existing Axentx products focus on data pipelines, AI inference, or IPC libraries; none provide a dedicated, declarative role‑management layer for Postgres.

---

## 3. Target Users  

| Persona | Role | Pain Points | How role‑sentry Helps |
|---------|------|-------------|-----------------------|
| **DBA/DBA‑Ops** | Manage permissions across environments | Manual scripts, audit trails | Declarative config, automated sync, audit logs |
| **Backend Engineer** | Grant access to services | Complex SQL, onboarding | Simple YAML/JSON files, CI integration |
| **Security Lead** | Ensure least‑privilege | Compliance reporting | Built‑in compliance checks, exportable reports |
| **DevOps/Infra** | Automate infra provisioning | Drift between infra and DB roles | Terraform/Ansible integration, state sync |

---

## 4. Goals & Success Metrics  

| Goal | Success Metric | Target |
|------|----------------|--------|
| **Reduce permission errors** | % of permission‑related incidents | < 1% of total incidents |
| **Improve auditability** | Time to generate a full permission audit | ≤ 2 minutes |
| **Accelerate onboarding** | Avg. time to grant a new role | ≤ 5 minutes |
| **Ensure compliance** | % of environments passing compliance checks | 100% |
| **Adoption** | Number of active repos using role‑sentry | ≥ 10 internal repos by Q3 2026 |

---

## 5. Key Features (Prioritized)

| # | Feature | Description | Priority |
|---|---------|-------------|----------|
| 1 | **Declarative Role Definition** | YAML/JSON schema to define roles, permissions, and role hierarchies. | Must |
| 2 | **State Sync Engine** | Detect drift between desired state and actual DB state; auto‑apply or flag differences. | Must |
| 3 | **Audit Log & Reporting** | Immutable audit trail of all changes; exportable CSV/JSON reports. | Must |
| 4 | **Compliance Checker** | Built‑in rules for least‑privilege, role expiration, and sensitive table access. | Must |
| 5 | **CI/CD Integration** | GitHub Actions / GitLab CI templates to run checks on PRs. | Should |
| 6 | **Terraform Provider** | Manage Postgres roles as Terraform resources. | Should |
| 7 | **CLI & Web UI** | Interactive CLI for quick changes; optional lightweight web UI for visual audit. | Could |
| 8 | **Role Templates & Inheritance** | Reusable role blocks and role inheritance to reduce duplication. | Could |
| 9 | **Multi‑Cluster Support** | Manage roles across multiple Postgres instances (e.g., prod, staging). | Could |
|10 | **Backup & Rollback** | Snapshot current state and revert to previous state if needed. | Could |

---

## 6. Scope

### In‑Scope

* Core engine for declarative role management (YAML/JSON).
* State synchronization and drift detection.
* Immutable audit logs and compliance reporting.
* CI/CD integration via GitHub Actions.
* Basic CLI tool for local execution.
* Documentation and example repos.

### Out‑of‑Scope (for first release)

* Full‑featured web UI (will be a separate micro‑service later).
* Terraform provider (planned for v2.0).
* Multi‑cluster orchestration (planned for v1.5).
* Integration with external IAM systems (e.g., AWS IAM, GCP IAM).
* Advanced role inheritance logic (basic inheritance only).

---

## 7. Technical Architecture

```
┌───────────────────────┐
│   role‑sentry CLI     │
│  (YAML/JSON parser)   │
└─────────────┬─────────┘
              │
              ▼
┌───────────────────────┐
│   State Sync Engine   │
│  (Postgres driver)    │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   Audit & Compliance   │
│  (SQLite log + rules)  │
└───────┬───────────────┘
        │
        ▼
┌───────────────────────┐
│   CI/CD Integration   │
│  (GitHub Actions)     │
└───────────────────────┘
```

* **Postgres Driver** – Uses `pgx` for efficient connection pooling.  
* **Audit Log** – Stored in a lightweight SQLite DB embedded in the repo; immutable append‑only.  
* **Compliance Engine** – Rule engine written in Go, configurable via YAML.  
* **CLI** – Exposes commands: `apply`, `diff`, `audit`, `check`.  

---

## 8. Deliverables

| Item | Description | Owner |
|------|-------------|-------|
| `role-sentry` CLI | Executable binary | Engineering Lead |
| `docs/` | Usage guide, schema reference, examples | Technical Writer |
| `examples/` | Sample YAML configs for dev, staging, prod | Engineering Lead |
| `ci/` | GitHub Actions workflow templates | DevOps |
| `CHANGELOG.md` | Release notes | Release Manager |
| `LICENSE` | Apache-2.0 | Legal |

---

## 9. Timeline (Milestones)

| Milestone | Date | Deliverable |
|-----------|------|-------------|
| MVP Definition | 2026‑07‑01 | PRD + Architecture |
| Core Engine | 2026‑08‑15 | CLI + State Sync |
| Audit & Compliance | 2026‑09‑30 | Audit logs + compliance checks |
| CI Integration | 2026‑10‑15 | GitHub Actions template |
| Beta Release | 2026‑11‑01 | v0.1.0 on GitHub |
| Public Release | 2026‑12‑01 | v1.0.0 with docs |

---

## 10. Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| **SQL injection via config** | Security breach | Validate all inputs; use parameterized queries |
| **Drift detection false positives** | Unnecessary alerts | Allow whitelisting of known exceptions |
| **Performance on large role sets** | Slow apply | Batch operations, connection pooling |
| **User adoption** | Low usage | Provide templates, integrate with existing CI pipelines |

---

## 11. Dependencies

* PostgreSQL ≥ 13
* Go 1.22 (for CLI)
* GitHub Actions (for CI templates)
* Optional: Terraform 1.5+ (future integration)

---

## 12. Acceptance Criteria

1. **Declarative config** – YAML file correctly parsed and validated.  
2. **State sync** – `role-sentry apply` brings DB into desired state without manual intervention.  
3. **Audit** – `role-sentry audit` outputs a CSV with all changes and timestamps.  
4. **Compliance** – `role-sentry check` returns pass/fail with detailed violations.  
5. **CI integration** – GitHub Action runs `role-sentry check` on PR and fails if violations exist.  
6. **Documentation** – README includes usage examples, schema, and troubleshooting.  

---

## 13. Future Enhancements (Post‑MVP)

* Terraform provider for IaC integration.  
* Web UI for visual role management.  
* Multi‑cluster orchestration with Kubernetes CRDs.  
* Integration with external IAM providers.  

---
