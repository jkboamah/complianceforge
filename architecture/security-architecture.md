# NovaBank Security Architecture

## ComplianceForge Enterprise Security Model

```mermaid
flowchart TB

Users[Users] --> WAF[Web Application Firewall]

WAF --> API[API Gateway]

API --> App[Application Layer]

App --> IAM[Identity & Access Management]

IAM --> MFA[Multi-Factor Authentication]

App --> Services[Microservices Layer]

Services --> DB[(Encrypted Databases)]
Services --> Storage[(Secure Cloud Storage)]

Services --> Logs[Central Logging / SIEM]

Logs --> SOC[Security Operations Center]

SOC --> IR[Incident Response System]

Services --> AI[AI Governance Layer]

AI --> PromptGuard[Prompt Injection Defense]
AI --> OutputFilter[Output Validation Engine]

Cloud[Cloud Infrastructure] --> CSPM[Cloud Security Posture Management]

CSPM --> SOC

DB --> Backup[(Secure Backups)]
