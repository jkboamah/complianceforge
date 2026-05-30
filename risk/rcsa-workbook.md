# RCSA Workbook (Risk & Control Self‑Assessment)

## Purpose
Document inherent risks, existing controls, and residual risk levels for key business processes in the reference enterprise environment.

---

## RCSA Table

| Process ID | Process Name | Inherent Risk | Existing Controls | Residual Risk | Owner | Next Assessment |
|------------|--------------|---------------|-------------------|----------------|-------|------------------|
| PR-001 | User Provisioning & Deprovisioning | High | MFA, RBAC, quarterly access reviews | Low | IAM Lead | 2026-06-01 |
| PR-002 | Backup & Recovery | High | Daily automated backups, encryption at rest, quarterly restore tests | Low | Infra Lead | 2026-06-01 |
| PR-003 | Vulnerability Management | Medium | Weekly scans, patch SLA (7 days critical), exception process | Low | Security Eng | 2026-06-01 |
| PR-004 | Third‑Party Onboarding | Medium | Vendor risk questionnaire, contract security clauses | Medium | Vendor Risk Lead | 2026-06-01 |
| PR-005 | Change Management | Medium | PR approvals, automated CI/CD gating, rollback plan | Low | DevOps Lead | 2026-06-01 |
| PR-006 | Incident Response | High | Defined playbooks, tabletop exercises, SIEM alerting | Low | SOC Lead | 2026-06-01 |

## Risk Rating Scale

| Inherent / Residual | Score | Description |
|---------------------|-------|-------------|
| Low | 1–20 | Acceptable; no further action |
| Medium | 21–50 | Requires monitoring or periodic review |
| High | 51–80 | Requires treatment plan |
| Critical | 81–125 | Immediate remediation required |

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | Initial RCSA workbook |

