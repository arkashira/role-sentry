# TECH_SPEC.md – role‑sentry

---

## 1. Overview

**role‑sentry** is a SaaS‑native service that automates, audits, and visualises PostgreSQL role and permission management.  
It solves the pain of manual role churn, accidental privilege escalation, and compliance drift in large PostgreSQL deployments.  
The product is a **new‑product** for Axentx, complementing the existing portfolio without overlap.

---

## 2. Architecture

```
┌───────────────────────┐
│  Client (Web UI / API)│
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  API Gateway (FastAPI)│
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  Service Layer (Python)│
│  - Role Engine          │
│  - Policy Engine        │
│  - Audit Logger         │
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  PostgreSQL DB (Target)│
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  Redis (Cache & Queue)│
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  Celery Workers (Async)│
└───────┬───────┬───────┘
        │       │
┌───────▼───────▼───────┐
│  Grafana / Loki (Observability)│
└───────────────────────┘
```

* **API Gateway** – Exposes REST/GraphQL endpoints, rate‑limits, auth (JWT + OAuth2).
* **Service Layer** – Core business logic, role‑diff engine, policy evaluation, audit trail.
* **PostgreSQL Target** – The database whose roles are managed; role‑sentry connects via a dedicated monitoring user.
* **Redis** – Fast cache for role snapshots and Celery broker.
* **Celery** – Background jobs for bulk role import, scheduled audits, and notification dispatch.
* **Observability** – Grafana dashboards for role health, Celery metrics; Loki for logs.

---

## 3. Components

| Component | Responsibility | Tech |
|-----------|----------------|------|
| **Auth Service** | OAuth2 + JWT, integration with Axentx SSO | FastAPI, python-jose |
| **Role Engine** | Pulls role definitions, computes diffs, proposes changes | Python, psycopg2 |
| **Policy Engine** | Enforces custom policies (e.g., no superuser in prod) | Python, Casbin |
| **Audit Logger** | Immutable audit trail, writes to PostgreSQL audit table + S3 | Python, SQLAlchemy |
| **Notification Service** | Email/SMS/Slack alerts | SendGrid, Twilio, Slack SDK |
| **Web UI** | Role visualisation, change approval workflow | React, Vite, Tailwind |
| **CLI Tool** | DevOps integration, local testing | Click, rich |
| **Deployment** | Docker + Docker‑Compose + Helm | Docker, Kubernetes |

---

## 4. Data Model

### 4.1 Core Tables (PostgreSQL)

| Table | Columns | Notes |
|-------|---------|-------|
| `roles` | `id`, `name`, `created_at`, `updated_at`, `created_by`, `updated_by` | Normalised role metadata |
| `role_privileges` | `role_id`, `privilege`, `granted_to`, `granted_by`, `granted_at` | Tracks privileges granted to roles |
| `role_hierarchy` | `role_id`, `inherits_role_id` | Role inheritance |
| `audit_log` | `id`, `role_id`, `action`, `old_value`, `new_value`, `changed_by`, `changed_at` | Immutable audit trail |
| `policies` | `id`, `name`, `json_policy`, `enabled`, `created_at` | Custom policy definitions |

### 4.2 Redis Keys

| Key | TTL | Purpose |
|-----|-----|---------|
| `role_snapshot:{db_name}` | 1h | Cached snapshot of roles |
| `audit_queue:{db_name}` | N/A | Celery task queue |

---

## 5. Key APIs / Interfaces

| Endpoint | Method | Description | Request | Response |
|----------|--------|-------------|---------|----------|
| `/api/v1/roles` | GET | List roles | `?page=&size=` | `[{id, name, ...}]` |
| `/api/v1/roles/{id}` | GET | Role detail |  | `{id, name, privileges, inherits}` |
| `/api/v1/roles/{id}/diff` | POST | Compute diff vs snapshot | `{snapshot_id}` | `{added, removed, changed}` |
| `/api/v1/roles/{id}/apply` | POST | Apply proposed changes | `{changes}` | `{status, applied_changes}` |
| `/api/v1/policies` | GET | List policies |  | `[{id, name, ...}]` |
| `/api/v1/policies/{id}` | POST | Evaluate policy | `{role_snapshot}` | `{violations}` |
| `/api/v1/audit` | GET | Audit trail | `?role_id=&since=` | `[{id, action, ...}]` |

**GraphQL** mirror of the above for advanced queries.

---

## 6. Tech Stack

| Layer | Technology | Rationale |
|-------|------------|-----------|
| **Backend** | Python 3.12, FastAPI | Modern async framework, auto‑docs |
| **ORM** | SQLAlchemy 2.0 | Declarative models, migrations (Alembic) |
| **Database** | PostgreSQL 15+ | Target DB + audit tables |
| **Cache / Queue** | Redis 7.x | Low‑latency caching, Celery broker |
| **Async Tasks** | Celery 5.x + RabbitMQ | Background jobs |
| **Observability** | Grafana, Loki, Prometheus | Metrics, logs |
| **Containerization** | Docker, Docker‑Compose | Local dev, CI |
| **Orchestration** | Helm + K8s | Production deployment |
| **CI/CD** | GitHub Actions | Tests, linting, image build |
| **Testing** | PyTest, Hypothesis | Unit + property tests |
| **Security** | OAuth2, JWT, TLS | Secure API access |

---

## 7. Dependencies

| Category | Package | Version |
|----------|---------|---------|
| **Core** | `fastapi`, `uvicorn[standard]`, `sqlalchemy`, `psycopg2-binary`, `alembic`, `pydantic` | latest |
| **Auth** | `python-jose`, `passlib[bcrypt]` | latest |
| **Policy** | `casbin`, `casbin-py` | latest |
| **Async** | `celery`, `redis`, `kombu` | latest |
| **Observability** | `prometheus-client`, `loguru` | latest |
| **Testing** | `pytest`, `pytest-asyncio`, `hypothesis` | latest |
| **Dev** | `black`, `isort`, `mypy`, `pre-commit` | latest |

All dependencies are pinned in `pyproject.toml` and `requirements.txt` for reproducibility.

---

## 8. Deployment

### 8.1 Local Development

```bash
git clone https://github.com/arkashira/role-sentry.git
cd role-sentry
docker compose up -d
```

* `docker compose` starts PostgreSQL, Redis, Celery worker, and FastAPI.
* Run tests: `pytest`.

### 8.2 Production

1. **Helm Chart** – `helm upgrade --install role-sentry ./charts/role-sentry`
2. **Secrets** – Store DB credentials, JWT secret, S3 keys in K8s secrets.
3. **Autoscaling** – Horizontal Pod Autoscaler on CPU/Memory.
4. **Backup** – Daily WAL shipping to S3; audit logs archived nightly.
5. **Observability** – Grafana dashboards deployed via Helm; Loki for logs.

### 8.3 CI/CD Pipeline

* **Lint** – `pre-commit run --all-files`
* **Test** – `pytest`
* **Build** – Docker image tagged `role-sentry:<sha>`
* **Push** – To GitHub Container Registry
* **Deploy** – Helm upgrade via GitHub Actions on `main` merge.

---

## 9. Security & Compliance

| Requirement | Implementation |
|-------------|----------------|
| **Least Privilege** | Role‑sentry connects using a dedicated monitoring user with `SELECT` on `pg_catalog` only. |
| **Audit Trail** | Immutable audit table; writes are append‑only, signed by HMAC. |
| **Transport Security** | All API traffic TLS‑encrypted; internal services use mTLS. |
| **Data Residency** | Configurable region for audit logs (S3 bucket). |
| **GDPR** | No PII stored; logs are anonymised. |

---

## 10. Roadmap (High‑Level)

| Quarter | Milestone |
|---------|-----------|
| Q3 2026 | MVP: role listing, diff, apply, audit log |
| Q4 2026 | Policy engine, notification service, UI |
| Q1 2027 | Multi‑tenant support, SSO integration |
| Q2 2027 | AI‑driven role recommendations (future integration) |

---

## 11. Appendix

### 11.1 Sample Role Diff JSON

```json
{
  "added": [
    {"role": "analytics_user", "privileges": ["SELECT"]},
    {"role": "reporting_role", "inherits": ["analytics_user"]}
  ],
  "removed": [
    {"role": "old_viewer", "privileges": ["SELECT"]},
    {"role": "old_viewer", "inherits": []}
  ],
  "changed": [
    {"role": "app_user", "privileges": {"added": ["INSERT"], "removed": ["DELETE"]}}
  ]
}
```

### 11.2 Policy Example (Casbin)

```json
{
  "name": "no_superuser_in_prod",
  "json_policy": {
    "p": [["role", "superuser", "deny"]],
    "g": [["role", "superuser", "admin"]]
  }
}
```

---
