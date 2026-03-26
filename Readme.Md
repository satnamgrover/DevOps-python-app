# Production-Grade DevOps Project on AWS EKS

## Project Overview
This project demonstrates a **production-ready DevOps workflow** for deploying containerized applications on **Amazon EKS**, showcasing **CI/CD, containerization, cloud deployment, Kubernetes orchestration, auto-scaling, and monitoring**.  

It reflects real-world industry practices, highlighting skills sought by top tech companies.

---

## Key Features

- **Containerized Deployment**: Dockerized application deployed on Kubernetes.  
- **Cloud Native Architecture**: AWS EKS cluster with secure access and load balancing.  
- **High Availability**: Auto-scaling and rolling updates for zero downtime.  
- **Monitoring & Observability**: Prometheus + Grafana for metrics, dashboards, and alerts.  
- **Production Best Practices**: Health checks, IAM roles with least privilege, structured logging.  

---

## Technology Stack

| Layer | Tool / Service |
|-------|----------------|
| CI/CD & Automation | Jenkins, GitHub Actions (optional) |
| Containerization | Docker |
| Container Registry | Amazon ECR |
| Orchestration | Amazon EKS, kubectl, eksctl |
| Monitoring & Logging | Prometheus, Grafana |
| Application | Python Flask (demo) |

---

## Architecture

```mermaid
flowchart LR
    A[Developer Commit] --> B[Version Control: GitHub]
    B --> C[Docker Build & Push]
    C --> D[Amazon ECR]
    D --> E[Amazon EKS Deployment]
    E --> F[LoadBalancer & Service]
    E --> G[Prometheus + Grafana Monitoring]


