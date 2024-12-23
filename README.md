# Step 1: Clone the Repository
git clone <repository-url>
cd <repository-folder>/infra

# Step 2: Preview and Deploy the EKS Cluster
# Ensure you have Pulumi installed (https://www.pulumi.com/docs/get-started/install/)
pulumi preview  # View changes Pulumi will make
pulumi up       # Apply changes to create the EKS cluster

# Note: The EKS cluster is configured to use two subnets across two availability zones, 
# ensuring high availability and fault tolerance.

# Step 3: Export Kubeconfig
pulumi stack output kubeconfig > kubeconfig.yaml
export KUBECONFIG=$(pwd)/kubeconfig.yaml

# Step 4: Install kubectl
# Download and install the kubectl binary for your system
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client  # Verify installation

# Step 5: Configure AWS CLI
# Install and configure AWS CLI with credentials having required permissions
aws configure
# Provide the following details when prompted:
# AWS Access Key: <your-access-key>
# AWS Secret Access Key: <your-secret-access-key>
# Default region: us-east-1 (or your preferred region)
# Output format: json

# Step 6: Verify the Cluster
# Ensure the cluster is running and nodes are available
kubectl get nodes
