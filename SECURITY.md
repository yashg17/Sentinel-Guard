# Security Policy

## Vulnerability Scanning
All code is subjected to **SonarQube SAST** scanning. 
Critical or High vulnerabilities will automatically break the Jenkins build.

## Log Mining Logic
We use a decoupled sidecar pattern (`log_security.py`) to monitor `security.log`.
**Alert Threshold:** > 5 failed logins per minute triggers a Discord alert.

## Reporting
Please report security concerns via the internal Security Team portal.
