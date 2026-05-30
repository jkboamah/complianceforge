# Vendor Risk Register

## Purpose
Track and manage security, compliance, and operational risks associated with third‑party vendors in the reference enterprise environment.

---

## Vendor Inventory

| Vendor | Service / Product | Risk Tier | Assessment Date | Next Review | Status | Key Controls |
|--------|------------------|-----------|----------------|-------------|--------|---------------|
| AWS | Cloud Hosting (IaaS) | Medium | 2025-06-01 | 2026-06-01 | Approved | SOC2, ISO 27001 |
| Microsoft Entra ID | Identity & Access Management | Low | 2025-06-01 | 2026-06-01 | Approved | MFA, Conditional Access |
| OpenAI | AI Services (LLM API) | High | 2025-06-01 | 2026-06-01 | Under Review | Data privacy, prompt injection controls |
| Datadog | Monitoring & SIEM | Low | 2025-06-01 | 2026-06-01 | Approved | Log encryption, access controls |
| GitHub | Source Code & CI/CD | Medium | 2025-06-01 | 2026-06-01 | Approved | SAML SSO, secret scanning |

## Risk Tier Definitions

- **Low** – Public information or non‑critical service; standard due diligence sufficient.
- **Medium** – Processes non‑public data; requires security questionnaire and SOC2/ISO 27001.
- **High** – Accesses sensitive customer data, financial systems, or core AI models; requires on‑site audit or penetration test.

## Vendor Risk Workflow

1. Identification → 2. Questionnaire → 3. Risk Tiering → 4. Approval → 5. Continuous Monitoring → 6. Annual Review

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | Initial vendor risk register |

