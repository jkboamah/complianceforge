# EU AI Act – Compliance Obligations

## Purpose
Identify and map applicable requirements of the EU AI Act for the reference enterprise environment.

---

## Risk Classification of Our AI Use Cases

| Use Case | AI Act Risk Level | Key Obligations |
|----------|-------------------|------------------|
| AI-assisted banking analytics | **High-risk** (Annex III – creditworthiness, risk assessment) | Conformity assessment, risk management system, technical documentation, human oversight |
| LLM-based support chatbot | **Limited risk** | Transparency obligation (disclose AI, enable deepfake notice) |
| Internal code autocompletion | **Minimal risk** | No additional obligations (except voluntary codes) |

---

## High‑Risk AI System Obligations (Article 15–27)

| Obligation | Implementation |
|-------------|----------------|
| Risk management system (Art. 9) | AI risk register + RCSA |
| Data governance (Art. 10) | Data quality controls, lineage, bias assessment |
| Technical documentation (Art. 11) | Model cards, system architecture diagrams |
| Transparency & human oversight (Art. 13–14) | User notification, human‑in‑the‑loop |
| Accuracy, robustness, cybersecurity (Art. 15) | Adversarial testing, prompt injection lab |
| Conformity assessment (Art. 43) | Internal assessment (Annex VI) or notified body |
| Post-market monitoring (Art. 72) | KRI dashboard, incident logging |

## Prohibited AI Practices (Article 5) – Not applicable to our reference use cases
- Subliminal manipulation
- Exploitation of vulnerabilities
- Social scoring
- Real‑time biometric identification in public spaces

## Governance & Reporting

- Register of high‑risk AI systems → `inventory/ai-system-inventory.md`
- Incident reporting to national authorities → AI incident playbook
- Annual review by AI Governance Committee

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | EU AI Act obligations for high‑risk and limited risk AI systems |
