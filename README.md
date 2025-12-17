# Vehicle Parking System Management

This repository contains a Vehicle Parking System that started as a
Python-based Parking Lot Management assignment and was later extended
into a Dockerized FastAPI application deployed on Kubernetes (Minikube).

The project demonstrates:
- Clean Python domain modeling
- Separation of business logic and API layer
- Docker containerization
- Kubernetes deployment using Minikube
- Service exposure using NodePort

---

## Tech Stack
- Python
- FastAPI
- Docker
- Kubernetes (Minikube)
- Pytest
- GitHub Actions (CI/CD)

---

## High-Level Architecture

CLI / API Client
        |
        v
FastAPI (`parking_lot/main.py`)
        |
        v
Parking Lot Service Layer
        |
        v
Core Domain Models
(`vehicle`, `slot`, `parking_lot_core`)

---

## Project Structure
```text
VEHICLE_PARKING_SYSTEM/
│
├── .github/workflows/
│   └── deploy-to-ec2.yml
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── parking_lot/
│   ├── __init__.py
│   ├── main.py               # entry point
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   ├── parking_lot_core.py
│   │   ├── slot.py
│   │   └── vehicle.py
│   │
│   ├── services/
│   │   └── parking_lot.py
│   │
│   └── tests/
│       └── test_smoke.py
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── README.md
└── .gitignore




# Vehicle Parking System

A FastAPI-based parking management system containerized with Docker and orchestrated via Kubernetes.

---

## Run with Docker (Local)

### Prerequisites
- Docker Desktop installed and running

1. Build Docker Image
```bash
docker build -t vehicle-parking-system:1.0 .

2. Run Container
docker run -p 8000:8000 vehicle-parking-system:1.0

3. Access Application
API Root: http://localhost:8000
Swagger UI: http://localhost:8000/docs



## Deploy to Kubernetes (Minikube)
###Prerequisites
  Minikube installed
  kubectl installed
  Docker Desktop running

1. Start Minikube
minikube start

### Point Docker to Minikube
eval $(minikube docker-env)

2. Build Docker Image inside Minikube
docker build -t vehicle-parking-system:1.0 .

3. Deploy Kubernetes Resources
# Apply deployment and service manifests to the namespace
kubectl apply -f deployment.yaml -n vechile-parking-system
kubectl apply -f service.yaml -n vechile-parking-system

4. Verify Deployment
kubectl get pods -n vechile-parking-system
kubectl get service -n vechile-parking-system

5. Access via Port-Forwarding
# Run this to bridge the K8s pod to your local machine
kubectl -n vechile-parking-system port-forward deployment/vehicle-parking-deployment 8000:8000
