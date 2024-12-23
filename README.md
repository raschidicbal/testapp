# Hometask for DevOps Engineer

Setting Up the EKS Cluster Using Pulumi
Follow these steps to set up the EKS cluster:

Clone the Repository
Clone this repository to your local machine and navigate to the infra directory:

bash
Copy code
git clone <repository-url>
cd <repository-folder>/infra
Preview and Deploy the EKS Cluster
Ensure you have Pulumi installed. Then, run the following commands:

bash
Copy code
pulumi preview
pulumi up
pulumi preview: Displays the changes Pulumi will apply.
pulumi up: Creates the EKS cluster based on the Pulumi configuration.
Export Kubeconfig
After the cluster is created, export the kubeconfig file to interact with the Kubernetes cluster:

bash
Copy code
pulumi stack output kubeconfig > kubeconfig.yaml
export KUBECONFIG=$(pwd)/kubeconfig.yaml
Install kubectl
Ensure that kubectl is installed on your machine. You can install it using the following commands:

bash
Copy code
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/$(uname | tr '[:upper:]' '[:lower:]')/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
Verify the installation:

bash
Copy code
kubectl version --client
Configure AWS CLI
Ensure that the AWS CLI is installed and configured with credentials that have the necessary permissions:

bash
Copy code
aws configure
Enter the following information when prompted:

AWS Access Key
AWS Secret Access Key
Default region (e.g., us-east-1)
Output format (e.g., json)
Verify the Cluster
Use kubectl to verify that your cluster is up and running:

bash
Copy code
kubectl get nodes
This command should return a list of nodes in your EKS cluster.

By following these steps, you’ll have an EKS cluster set up and ready for deployments.
