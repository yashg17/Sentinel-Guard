# Monitoring & Incident Response SOP

## Alert: `BruteForceAttack`
**Severity:** Critical
1. Check the **Grafana Security Dashboard**.
2. Identify the source `instance` and `IP`.
3. Verify if the traffic is a legitimate peak or a malicious scan.
4. If malicious, update the AWS Security Group to null-route the IP.

## Grafana Variables
Use the `$instance` variable to filter between `prometheus-1` and `prometheus-2`.
