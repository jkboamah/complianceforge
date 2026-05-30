# Regulatory & Legal Obligations Register

## Purpose
Inventory of applicable laws, regulations, and contractual requirements for the reference enterprise environment. Maps each obligation to internal controls.

---

## Obligations Table

| Obligation ID | Source | Requirement | Applicable Assets | Owner | Control Mapping | Review Frequency |
|---------------|--------|-------------|--------------------|-------|-----------------|------------------|
| REG-001 | GDPR (Art. 32) | Security of processing – encryption, availability | Customer PII | Data Protection Officer | POL-006, encryption standards | Annual |
| REG-002 | ISO 27001:2022 A.5.1 | Information security policy | All information systems | Security Governance Team | POL-001 | Annual |
| REG-003 | SOC2 (CC6.1) | Logical access controls | IAM system, cloud consoles | IAM Lead | POL-002, RBAC, MFA | Quarterly |
| REG-004 | PCI DSS v4.0 (Req 10) | Logging and monitoring | Cardholder data environment | SOC Lead | SIEM configuration | Monthly |
| REG-005 | NIST CSF (PR.IP-1) | Baseline configuration | Servers, containers, endpoints | Infrastructure Lead | CIS benchmarks | Quarterly |
| REG-006 | AI Act (EU) – Article 15 | Transparency and human oversight | AI/LLM systems | AI Governance Lead | AI Security Policy | Annual |

## Obligation Lifecycle

1. Identification → 2. Classification → 3. Control Assignment → 4. Monitoring → 5. Annual Review

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | Initial obligations register (GDPR, ISO27001, SOC2, PCI DSS, NIST, AI Act) |

