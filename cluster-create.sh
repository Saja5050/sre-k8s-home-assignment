#!/bin/bash

# Create resource group
az group create --name sre-home-assignment-rg --location eastus

# Create AKS cluster with Calico network policy and RBAC enabled
  az aks create \
  --resource-group sre-home-assignment-rg \
  --name bitcoin-k8s-cluster \
  --node-count 1 \
  --enable-addons monitoring \
  --generate-ssh-keys \
  --load-balancer-sku standard \
  --node-vm-size Standard_B2ms \
  --network-plugin kubenet \
  --network-policy calico \
  --location eastus

