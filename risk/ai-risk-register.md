# AI Risk Register

## Purpose
Identify, assess, and manage risks specific to artificial intelligence systems.

## Risk Inventory

| Risk ID | Risk Description | AI System | Impact | Likelihood | Exploitability | Score | Controls | Residual | Owner |
|---------|------------------|-----------|--------|------------|----------------|-------|----------|----------|-------|
| AI-R01 | Prompt injection data leak | Banking LLM | 5 | 3 | 4 | 60 (High) | Input validation | Medium | AI Security |
| AI-R02 | Model drift wrong decisions | Credit AI | 5 | 3 | 2 | 30 (Medium) | Retraining | Low | ML Engineer |
| AI-R03 | Training data poisoning | All AI | 4 | 2 | 3 | 24 (Medium) | Data integrity | Low | Data Gov |
| AI-R04 | Lack of transparency | High-risk AI | 4 | 4 | 2 | 32 (Medium) | Model cards | Low | AI Gov |
| AI-R05 | EU AI Act non-compliance | Credit AI | 5 | 2 | 1 | 10 (Low) | Conformity assessment | Low | Compliance |

## Scoring: Impact × Likelihood × Exploitability (1-5 each). Critical >80, High 51-80, Medium 21-50, Low ≤20.
