# KRI Dashboard (Key Risk Indicators)

## Purpose
Quarterly dashboard of key risk indicators for the reference enterprise environment. Alert thresholds trigger management review.

---

## Current Status

| KRI | Metric | Current Value | Threshold (Alert) | Status | Trend |
|-----|--------|----------------|-------------------|--------|-------|
| MFA Coverage | % of users with MFA enabled | 94% | <95% | ⚠️ Alert | Improving |
| Critical Vulnerabilities | Unpatched CVSS ≥9.0 older than 7 days | 3 | >5 | ✅ Healthy | Stable |
| Phishing Susceptibility | % of users who clicked in simulated phish | 4.2% | >5% | ✅ Healthy | Improving |
| Backup Success Rate | % of successful backups (last 30 days) | 99.8% | <99% | ✅ Healthy | Stable |
| Failed Login Attempts (External) | Count per day | 1,200 | >2,000 | ✅ Healthy | Increasing |
| Security Awareness Training Completion | % of employees completed | 97% | <90% | ✅ Healthy | Stable |
| Vendor Risk Exceptions | Open exceptions past due | 2 | >5 | ✅ Healthy | Stable |
| Mean Time to Detect (MTTD) | Hours from compromise to detection | 3.5h | >8h | ✅ Healthy | Improving |
| Mean Time to Respond (MTTR) | Hours from detection to containment | 6h | >12h | ✅ Healthy | Stable |

## Alert Definitions

- **Red** – Immediate management review required
- **Yellow** – Watch; action plan due within 30 days
- **Green** – Within acceptable range

## Review Cadence

- **Weekly** – SOC Lead
- **Quarterly** – Risk Committee / Board Dashboard

## Version History

| Version | Date | Description |
|---------|------|-------------|
| 1.0 | 2025-06-01 | Initial KRI dashboard |

