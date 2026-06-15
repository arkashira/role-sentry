# STORIES.md

## Project: role‑sentry  
**Goal** – Simplify and secure Postgres role permission management for database administrators and developers.  
**MVP** – A web‑based UI + CLI that lets users view, create, modify, and audit roles and privileges with minimal friction, while providing automated compliance checks and audit logs.

---

## Epics & Story Backlog

| Epic | Story | Acceptance Criteria |
|------|-------|---------------------|
| **1. Core Role Management** | **1.1** As a DBA, I want to list all existing roles so that I can review current permissions. | • UI shows paginated list of roles.<br>• CLI `role-sentry list-roles` returns JSON array of role names.<br>• List includes role attributes (login, superuser, inherit, replication, createdb, createrole). |
| | **1.2** As a DBA, I want to create a new role with custom attributes so that I can grant appropriate privileges. | • UI form accepts role name, password, and attribute toggles.<br>• CLI `role-sentry create-role --name <name> [options]` creates role.<br>• Validation errors shown for duplicate names or invalid attributes.<br>• Role appears in list immediately. |
| | **1.3** As a DBA, I want to modify an existing role’s attributes so that I can adjust permissions. | • UI edit page pre‑populated with current attributes.<br>• CLI `role-sentry alter-role --name <name> [options]` updates attributes.<br>• Changes persist after reload. |
| | **1.4** As a DBA, I want to delete a role safely so that I can remove stale accounts. | • UI delete button prompts confirmation.<br>• CLI `role-sentry drop-role --name <name>` removes role after confirmation.<br>• Deletion fails if role has dependent objects unless `--force` is used. |
| **2. Privilege Granting & Revocation** | **2.1** As a DBA, I want to grant privileges to a role on a table so that I can control access. | • UI “Grant” dialog lists tables and privilege checkboxes.<br>• CLI `role-sentry grant --role <role> --table <table> --privileges <privs>` applies grant.<br>• Grant appears in role’s detail view. |
| | **2.2** As a DBA, I want to revoke privileges from a role so that I can tighten security. | • UI “Revoke” dialog lists current grants.<br>• CLI `role-sentry revoke --role <role> --table <table> --privileges <privs>` removes grant.<br>• Revocation reflected in audit log. |
| **3. Role Hierarchies & Inheritance** | **3.1** As a DBA, I want to create role inheritance relationships so that I can reuse permission sets. | • UI “Create Inheritance” dialog selects parent and child roles.<br>• CLI `role-sentry inherit --parent <p> --child <c>` establishes relationship.<br>• Inheritance status visible in role detail. |
| | **3.2** As a DBA, I want to view inherited privileges for a role so that I can audit effective permissions. | • UI “Effective Privileges” tab lists all privileges including inherited.<br>• CLI `role-sentry effective-privileges --role <role>` outputs JSON list. |
| **4. Compliance & Auditing** | **4.1** As a compliance officer, I want to export a snapshot of all roles and privileges so that I can perform audits. | • UI “Export” button downloads CSV/JSON.<br>• CLI `role-sentry export --format csv|json` writes to file.<br>• Export includes role attributes, grants, and inheritance. |
| | **4.2** As a DBA, I want automated compliance checks (e.g., no superuser without audit) so that I can enforce policies. | • CLI `role-sentry compliance-check` returns list of violations.<br>• UI shows compliance status badge per role.<br>• Violations include severity and suggested remediation. |
| | **4.3** As a DBA, I want an audit log of all role changes so that I can trace actions. | • UI “Audit Log” page shows timestamp, actor, action, and details.<br>• CLI `role-sentry audit-log --since <date>` streams logs.<br>• Logs are immutable and stored in a separate audit table. |
| **5. Security & Authentication** | **5.1** As a user, I want to authenticate via existing Postgres credentials so that I can use the tool securely. | • UI login uses Postgres `pg_hba` authentication.<br>• CLI accepts `PGUSER`, `PGPASSWORD`, or `.pgpass` file.<br>• Failed auth shows clear error message. |
| | **5.2** As a DBA, I want role‑based access to the tool so that only authorized users can modify roles. | • Tool checks Postgres `pg_authid` for `role_sentry_admin` role.<br>• Non‑admin users can only view roles, not modify.<br>• UI shows read‑only mode for non‑admins. |
| **6. Integration & Extensibility** | **6.1** As a developer, I want a REST API so that I can integrate role‑sentry into CI/CD pipelines. | • API endpoints: `/roles`, `/roles/{name}`, `/grants`, `/audit`.<br>• Authentication via JWT derived from Postgres session.<br>• Swagger docs auto‑generated. |
| | **6.2** As a DBA, I want to schedule automated role cleanup jobs so that stale roles are removed. | • CLI `role-sentry schedule-cleanup --days <n>` creates cron job.<br>• Job logs to audit table.<br>• UI shows next run time and status. |
| **7. Documentation & Help** | **7.1** As a new user, I want comprehensive help text so that I can use the CLI without external docs. | • `role-sentry --help` displays all commands, options, and examples.<br>• `role-sentry <command> --help` gives command‑specific help.<br>• Help includes links to online docs. |
| | **7.2** As a user, I want in‑app tooltips and inline validation so that I can avoid errors. | • UI form fields show real‑time validation messages.<br>• Tooltips explain each attribute.<br>• CLI prints warnings for common mistakes. |

---

## MVP Release Order

1. **Epic 1** – Core Role Management (list, create, alter, delete).  
2. **Epic 2** – Privilege Granting & Revocation.  
3. **Epic 4** – Compliance & Auditing (export, compliance check, audit log).  
4. **Epic 5** – Security & Authentication (Postgres auth, role‑based access).  
5. **Epic 3** – Role Hierarchies & Inheritance (inherit, effective privileges).  
6. **Epic 6** – Integration & Extensibility (REST API, scheduled cleanup).  
7. **Epic 7** – Documentation & Help.

---

## Notes

- All data operations must use the existing Postgres connection pool from the Axentx shared BRAIN.  
- UI built with React + Ant Design; CLI built with Go (v1.22).  
- Persist audit logs in a dedicated `role_sentry_audit` schema to avoid cluttering `pg_catalog`.  
- Ensure compliance checks run automatically on every role modification.  

---
