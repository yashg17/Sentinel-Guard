# Parent Portal Sentinel 🛡️

## Overview
A High-Availability DevSecOps pipeline for the Parent Portal application. 
Includes automated SAST scanning and real-time log mining.

## Architecture
- **App:** Flask-based Python app.
- **CI/CD:** Jenkins + GitHub Webhooks + SonarQube.
- **Monitoring:** HA Prometheus (2 Replicas) + Alertmanager + Grafana.

## Quick Start
1. Ensure `docker-compose` and `Docker` are installed.
2. Run `docker compose up -d`.
3. Access Grafana at `http://localhost:3000`.
