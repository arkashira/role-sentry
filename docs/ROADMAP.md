# Roadmap – role‑sentry

**Project**: role‑sentry  
**Owner**: Axentx Product & Engineering  
**Goal**: Provide a lightweight, secure, and auditable solution for managing PostgreSQL role permissions, filling a gap in the Axentx portfolio.

---

## Table of Contents

- [Vision & Success Metrics](#vision--success-metrics)
- [MVP (Must‑Have for Launch)](#mvp-must-have-for-launch)
- [Version 1 – Feature‑Rich Core](#version-1-feature-rich-core)
- [Version 2 – Scale & Automation](#version-2-scale--automation)
- [Roadmap Timeline](#roadmap-timeline)
- [Dependencies & Risks](#dependencies--risks)
- [Key Milestones](#key-milestones)

---

## Vision & Success Metrics

| Metric | Target | Notes |
|--------|--------|-------|
| **Adoption** | 10+ active internal projects by Q4 2026 | Measure via internal usage dashboards |
| **Audit Coverage** | 100% of critical roles audited within 24 h | Real‑time alerts |
| **Performance** | < 50 ms per permission query | Benchmark against existing tools |
| **Compliance** | Pass SOC 2, ISO 27001 audit | Security hardening |
| **Revenue** | $50k ARR from external customers | Pilot with 2 external partners |

---

## MVP – Must‑Have for Launch

| Feature | Description | MVP‑Critical? |
|---------|-------------|---------------|
| **PostgreSQL Role CRUD** | Create, read, update, delete roles with granular permission sets | ✅ |
| **Permission Matrix UI** | Web UI to view/edit role permissions in a matrix view | ✅ |
| **Audit Log** | Immutable log of all role changes with timestamp, actor, and diff | ✅ |
| **RBAC Enforcement** | Enforce role permissions at the database level via pg_hba.conf and role attributes | ✅ |
| **CLI Tool** | Command‑line interface for scripting and CI/CD integration | ✅ |
| **Basic Authentication** | OAuth2 / SSO integration for UI access | ✅ |
| **Unit & Integration Tests** | 80% coverage of core logic | ✅ |
| **Documentation** | Quick‑start guide, API reference, and developer docs | ✅ |

**MVP Deliverable**: A fully functional, self‑contained application that can be deployed on a single node and manages PostgreSQL roles with an audit trail.

---

## Version 1 – Feature‑Rich Core

| Theme | Features | Deliverable |
|-------|----------|-------------|
| **Advanced Permission Modeling** | Hierarchical roles, role inheritance, and permission scopes | Role graph API |
| **Policy Engine** | Declarative policies (e.g., “only DB admins can grant SELECT on public schema”) | Policy DSL + engine |
| **Webhooks & Event Bus** | Emit events on role changes for downstream systems | Event schema & SDK |
| **Multi‑Tenant Support** | Isolate roles per tenant with shared infrastructure | Tenant isolation layer |
| **Compliance Templates** | Pre‑built templates for GDPR, HIPAA, PCI | Template library |
| **Performance Optimizations** | Caching layer, batched permission checks | Cache module |
| **CI/CD Integration** | GitHub Actions, GitLab CI templates | CI templates |

**Key Milestones**  
- Q2 2026: Complete advanced permission modeling & policy engine.  
- Q3 2026: Release v1.0 with multi‑tenant and compliance templates.

---

## Version 2 – Scale & Automation

| Theme | Features | Deliverable |
|-------|----------|-------------|
| **Horizontal Scaling** | Stateless API layer, PostgreSQL connection pooling | Scalable architecture |
| **Observability** | Distributed tracing, metrics, alerting dashboards | Prometheus/Grafana stack |
| **Self‑Healing** | Auto‑restart, health checks, graceful shutdown | Kubernetes Helm chart |
| **Machine‑Learning Ops** | Anomaly detection on permission changes (leveraging Axentx ML stack) | ML model integration |
| **Marketplace Integration** | Export role definitions to other Axentx products (e.g., role‑audit) | API connectors |
| **OpenAPI & SDKs** | Auto‑generated SDKs for Python, Go, TypeScript | SDK repo |
| **Internationalization** | UI translations, locale support | i18n framework |

**Key Milestones**  
- Q4 2026: Deploy v2.0 in production with full observability.  
- Q1 2027: Release ML‑driven anomaly detection feature.

---

## Roadmap Timeline

| Quarter | Milestone |
|---------|-----------|
| **Q1 2026** | MVP core development, internal beta |
| **Q2 2026** | MVP launch, first internal adoption |
| **Q3 2026** | V1.0 release, multi‑tenant & compliance |
| **Q4 2026** | V2.0 architecture, observability |
| **Q1 2027** | ML anomaly detection, marketplace integration |

---

## Dependencies & Risks

| Category | Dependency | Risk | Mitigation |
|----------|------------|------|------------|
| **Database** | PostgreSQL 15+ | Compatibility issues with older versions | Provide backward‑compatibility layer |
| **Auth** | OAuth2 provider | Single point of failure | Fallback to local auth |
| **ML** | Axentx ML stack | Data privacy concerns | Enforce data anonymization |
| **Infrastructure** | Kubernetes | Operational overhead | Offer managed Helm chart |

---

## Key Milestones (Detailed)

| Date | Milestone | Owner | Acceptance Criteria |
|------|-----------|-------|---------------------|
| **2026‑03‑15** | MVP Alpha | Engineering Lead | 80% unit coverage, UI functional |
| **2026‑04‑30** | MVP Beta | QA Lead | 100% audit log integrity, no critical bugs |
| **2026‑05‑31** | MVP Release | Product Manager | Internal adoption > 5 projects |
| **2026‑07‑31** | V1.0 Release | Engineering Lead | Multi‑tenant, policy engine, 90% test coverage |
| **2026‑12‑31** | V2.0 Release | Ops Lead | Horizontal scaling, observability dashboards |

---

### Closing Note

role‑sentry fills a critical gap in the Axentx ecosystem by providing a secure, auditable, and extensible PostgreSQL role management solution. By following this roadmap, we will deliver a product that not only meets internal needs but also positions us for external market adoption and revenue generation.
