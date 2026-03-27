# Production-Grade DevOps Project on AWS EKS

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![EKS Status](https://img.shields.io/badge/EKS-production-blue)
![Docker Version](https://img.shields.io/badge/Docker-24.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## Project Overview
This project demonstrates a **production-ready DevOps workflow** for deploying containerized applications on **Amazon EKS**, showcasing **cloud-native deployment, containerization, monitoring, and automation**.  

It reflects real-world industry practices, highlighting skills sought by top tech companies.

---

## Key Features

- **Containerized Deployment**: Dockerized application deployed on Kubernetes.  
- **Cloud Native Architecture**: AWS EKS cluster with secure access and load balancing.  
- **High Availability**: Auto-scaling and rolling updates for zero downtime.  
- **Monitoring & Observability**: Prometheus + Grafana dashboards and alerts.  
- **Production Best Practices**: Health checks, IAM roles with least privilege, structured logging.  

---

## Technology Stack

| Layer | Tool / Service |
|-------|----------------|
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Amazon EKS, kubectl, eksctl |
| Monitoring & Logging | Prometheus, Grafana |
| Application | Python Flask (demo) |
| Automation | Jenkins / GitHub Actions (optional) |
| Cloud Management | AWS CLI |

---

## Architecture

```mermaid id="7kmf8l"
flowchart LR
    A[Developer Commit] --> B[GitHub]
    B --> C[Docker Build & Push]
    C --> D[Amazon ECR]
    D --> E[Amazon EKS Deployment]
    E --> F[LoadBalancer & Service]
    E --> G[Prometheus + Grafana Monitoring]



```
## Screenshots / Demo

**Application Running on EKS**  
![App Screenshot](screenshots/app_home.png)
![App Add User Screenshot](screenshots/app_user_add.png)
![App User List Screenshot](screenshots/app_user_list.png

**Grafana Monitoring Dashboard**  
![Grafana Dashboard](screenshots/grafana_dashboard.png)
