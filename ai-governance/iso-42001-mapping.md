# ISO/IEC 42001:2023 – Artificial Intelligence Management System (AIMS)

## Purpose
Map the reference enterprise environment’s AI governance controls to ISO/IEC 42001 requirements.

---

## Clause Mapping

| ISO 42001 Clause | Requirement | Control Implementation | Evidence |
|------------------|-------------|------------------------|----------|
| 5.1.1 | AI policy | AI Security & Governance Policy (POL-008) | Policy document |
| 6.1.3 | AI risk assessment | AI risk register (see `risk/ai-risk-register.md`) | Risk assessment report |
| 6.1.4 | AI controls | Prompt filtering, output validation, human oversight | Technical controls + playbooks |
| 7.5 | Documented information | AI system inventory, data lineage, model cards | `inventory/ai-system-inventory.md` |
| 8.3 | AI system impact assessment | Conformity assessment for high-risk AI | Impact assessment template |
| 9.2 | Internal audit | Annual AI controls audit | Audit reports |
| 10.2 | Nonconformity & corrective action | Issue register (ISS-003 OpenAI vendor risk) | Issue register |

## Annex A Controls (AI-specific)

| Annex A Control | Title | Our Control |
|----------------|-------|--------------|
| A.5.1 | Data quality for AI | Data validation pipeline |
| A.6.2 | Robustness & resilience | Adversarial testing (prompt injection lab) |
| A.6.4 | Transparency | Model cards, user-facing AI disclosure |
| A.7.2 | Human oversight | Human-in-the-loop for high-risk decisions |

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | ISO 42001 mapping for AI management system |
