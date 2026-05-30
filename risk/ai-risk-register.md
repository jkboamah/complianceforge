# AI Risk Register

## Purpose
Identify, assess, and manage risks specific to artificial intelligence systems in the reference enterprise environment.

---

## Risk Inventory

| Risk ID | Risk Description | AI System Affected | Inherent Risk (1-5) | Likelihood (1-5) | Exploitability (1-5) | Risk Score | Controls | Residual Risk | Owner |
|---------|------------------|--------------------|---------------------|------------------|----------------------|------------|-----------|---------------|-------|
| AI-R01 | Prompt injection leading to data leak | Banking analytics LLM | 5 | 3 | 4 | 60 (High) | Input validation, output filtering, rate limiting | Medium | AI Security Lead |
| AI-R02 | Model drift causing incorrect credit decisions | Credit risk AI | 5 | 3 | 2 | 30 (Medium) | Regular retraining, performance monitoring | Low | ML Engineer |
| AI-R03 | Training data poisoning | All AI systems | 4 | 2 | 3 | 24 (Medium) | Data provenance, integrity checks | Low | Data Governance |
| AI-R04 | Lack of transparency (black box) | High-risk AI | 4 | 4 | 2 | 32 (Medium) | Model cards, explainability tools (SHAP) | Low | AI Governance |
| AI-R05 | EU AI Act non-compliance | Credit risk AI | 5 | 2 | 1 | 10 (Low) | Obligations register, conformity assessment | Low | Compliance Lead |

## Risk Scoring Formula

Risk Score = Impact × Likelihood × Exploitability (each 1–5)

- Critical: 81–125
- High: 51–80
- Medium: 21–50
- Low: 1–20

## Mitigation Timeline

| Risk ID | Mitigation Action | Target Date | Status |
|---------|-------------------|-------------|--------|
| AI-R01 | Deploy prompt injection firewall | 2025-08-01 | In progress |
| AI-R02 | Implement model drift dashboard | 2025-07-15 | Planned |
| AI-R05 | Complete conformity assessment | 2025-12-01 | Not started |

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | Initial AI risk register |
