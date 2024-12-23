# Step 1: Clone the Repository
# Start by cloning the GitHub repository to your local machine.
git clone <repository-url>
cd <repository-folder>/infra

# Step 2: Preview and Deploy the EKS Cluster
# Use Pulumi to preview and deploy the infrastructure. 
# Ensure Pulumi is installed. You can install Pulumi by following the instructions at:
# https://www.pulumi.com/docs/get-started/install/
pulumi preview  # This will show the changes Pulumi will make.
pulumi up       # This command applies the changes and creates the EKS cluster.

# Note: The EKS cluster is configured to use two subnets across two availability zones, 
# providing high availability and fault tolerance.

# Step 3: Export Kubeconfig
# After the cluster is created, you need to configure kubectl to interact with it.
# Export the kubeconfig file from Pulumi's stack output and set it as an environment variable.
pulumi stack output kubeconfig > kubeconfig.yaml
export KUBECONFIG=$(pwd)/kubeconfig.yaml

# Step 4: Install kubectl
# If you don't already have kubectl installed, download and install it.
# Replace "$(uname | tr '[:upper:]' '[:lower:]')" with your OS (e.g., darwin for macOS, linux, or windows).
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client  # Verify that kubectl is installed successfully.

# Step 5: Configure AWS CLI
# The AWS CLI is required to interact with AWS services.
# Install the AWS CLI by following the instructions at:
# https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
# Once installed, configure it with your AWS credentials.
aws configure
# Provide the following details when prompted:
# AWS Access Key: <your-access-key>
# AWS Secret Access Key: <your-secret-access-key>
# Default region: us-east-1 (or your preferred region)
# Output format: json

# Step 6: Verify the Cluster
# Use kubectl to ensure the EKS cluster is up and running.
kubectl get nodes  # This will list the nodes in your cluster.
