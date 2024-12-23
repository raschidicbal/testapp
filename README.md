## Setting Up the EKS Cluster Using Pulumi

To create a highly available EKS cluster spanning two subnets across two availability zones, follow the steps below. This setup ensures improved fault tolerance and availability.

### Step 1: Clone the Repository
Start by cloning the GitHub repository to your local machine.

```bash
git clone <repository-url>
cd <repository-folder>/infra
```

Step 2: Preview and Deploy the EKS Cluster
Use Pulumi to preview and deploy the infrastructure. Ensure Pulumi is installed. You can install Pulumi by following the instructions here.

```bash
pulumi preview  # This will show the changes Pulumi will make.
pulumi up       # This command applies the changes and creates the EKS cluster.
```
