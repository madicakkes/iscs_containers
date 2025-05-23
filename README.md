# MSYS22FP - Django WebApp Kubernetes Deployment

## Overview
This repository contains a Django web application configured for deployment on a local Kubernetes cluster using Minikube. The setup includes PostgreSQL as the database, automated deployment scripts, and verification steps to ensure public reproducibility.

---

## Prerequisites

**Required Software:**
- Docker Desktop (https://www.docker.com/products/docker-desktop)
- Minikube (https://minikube.sigs.k8s.io/docs/start/)
- kubectl (https://kubernetes.io/docs/tasks/tools/)
- Git (https://git-scm.com/)

## Quick Start (5-Minute Deployment)

bash
# 1. Clone the repository
git clone https://github.com/madicakkes/iscs_containers
cd iscs_containers

# 2. Make scripts executable
chmod +x scripts/*.sh

# 3. Start Minikube
minikube start --memory=4096 --cpus=2
minikube addons enable ingress metrics-server

# 4. Deploy the application
./scripts/deploy.sh

# 5. Access the application
kubectl port-forward service/webapp-service 8000:80 -n webapp
# Visit: http://localhost:8000


## Step-by-Step Verification Process

# 1. Clone and Setup
bash
git clone https://github.com/madicakkes/iscs_containers
cd iscs_containers
chmod +x scripts/*.sh

# 2. Quick Deploy
bash
./scripts/deploy.sh

# 3. Verify Components:
bash
./scripts/verify.sh


# 4. Manual Verification:

# 4.1. Application and Dependencies
kubectl get deployments -n webapp
# Should show: webapp, webapp-postgres

# 4.2. Pods
kubectl get pods -n webapp
# Should show running pods

# 4.3. Services (NO LoadBalancer)
kubectl get services -n webapp
# Should show ClusterIP services only

# 4.4. Ingress
kubectl get ingress -n webapp
# Should show webapp-ingress

# 4.5. Autoscaling
kubectl get hpa -n webapp
# Should show webapp-hpa

# 4.6. Storage Persistence
kubectl get pvc -n webapp
# Should show webapp-postgres-pvc


# 5. Test Application
bash
# Port forward and test
kubectl port-forward service/webapp-service 8000:80 -n webapp &
curl http://localhost:8000/health/
curl http://localhost:8000/

# 6. Test Persistence
bash
# Delete postgres pod and verify data survives
kubectl delete pod -l app=webapp-postgres -n webapp
kubectl wait --for=condition=Ready pod -l app=webapp-postgres -n webapp
# Data should still exist

## Verification
bash
./scripts/verify.sh

## Troubleshooting

### ✅ 1. Prerequisites Needed
**Software Requirements:**
bash
# They need to install:
- Docker Desktop
- Minikube
- kubectl
- Git
**Hardware Requirements**
bash
# Minimum system requirements:
- 4GB RAM available for Minikube
- 2 CPU cores
- 20GB free disk space

## Helper Scripts
scripts/deploy.sh:
bash
#!/bin/bash
set -e
echo "Deploying WebApp to Kubernetes..."

# Check prerequisites
command -v minikube >/dev/null 2>&1 || { echo "Minikube not installed"; exit 1; }
command -v kubectl >/dev/null 2>&1 || { echo "kubectl not installed"; exit 1; }
# Start minikube if not running
if ! minikube status >/dev/null 2>&1; then
echo "Starting Minikube..."
minikube start --memory=4096 --cpus=2
minikube addons enable ingress metrics-server
fi

# Deploy application
echo "Deploying Kubernetes manifests...
kubectl apply -f kubernetes-manifests/"

# Wait for deployments
echo "Waiting for deployments to be ready..."
kubectl wait --for=condition=available --timeout=300s deployment/webapp-postgres -n web
kubectl wait --for=condition=available --timeout=300s deployment/webapp -n webapp
echo "Deployment complete!"
echo "Access your app:"
echo "Port-forward: kubectl port-forward service/webapp-service 8000:80 -n webapp"
echo "Then visit: http://localhost:8000"

scripts/verify.sh:
bash
#!/bin/bash
echo "Verifying deployment..."

# Check all components
kubectl get all,pvc,ingress,hpa -n webapp
# Verify no LoadBalancer services
echo "Checking for LoadBalancer services (should be none)..."
LB
_
SERVICES=$(kubectl get svc -n webapp --field-selector spec.type=LoadBalancer --no-he
if [ "$LB
SERVICES"
_
-eq 0 ]; then
echo "No LoadBalancer services found (correct)"
else
echo "LoadBalancer services found (incorrect)"
fi

# Test application health
echo "Testing application health..."
kubectl port-forward service/webapp-service 8080:80 -n webapp &
PF
_
PID=$!
sleep 5
if curl -s http://localhost:8080/health/ | grep -q "healthy"; then
echo "Application health check passed"
else
echo "Application health check failed"
fi
kill $PF
_
PID 2>/dev/null
echo "Verification complete!"


## Test Application
bash
# Port forward and test
kubectl port-forward service/webapp-service 8000:80 -n webapp &
curl http://localhost:8000/health/
curl http://localhost:8000/

## Test Persistence
bash
# Delete postgres pod and verify data survives
kubectl delete pod -l app=webapp-postgres -n webapp
kubectl wait --for=condition=Ready pod -l app=webapp-postgres -n webapp
# Data should still exist
