# Hometask for DevOps Engineer

## Scenario
- You’ve been hired as the DevOps Engineer @ [Adios.ai](https://adios.ai/), an online SaaS platform for helping busy professionals improve their email productivity.
- You report to the Head of Engineering and you were tasked to prepare a PoC for migration of Adios.ai infrastructure from Heroku to AWS using EKS

## The task
This repository contains a simple web-server application written in Python using [Flask](https://pypi.org/project/Flask/) framework. The application contains `/users` `GET` endpoint returning all records from `Users` table and `/upload` `POST` endpoint to upload files to S3 bucket

```
GET http://127.0.0.1:5000/users

[
  {
    "email": "alice@example.com",
    "id": 1,
    "name": "Alice"
  },
  {
    "email": "bob@example.com",
    "id": 2,
    "name": "Bob"
  }
]
```

As part of this hometask, you need to implement:
1. Define an infrastructure using [Pulumi](https://www.pulumi.com/) to deploy the application to an EKS cluster. Ensure the infrastructure supports rolling updates and high availability.
2. Use [Helm](https://helm.sh/) or equivalent tools to deploy a sample web application to the Kubernetes cluster.
3. Set up a CI/CD pipeline using GitHub Actions
4. Provide a detailed README file that includes:
   1. Setup and deployment instructions.
   2. Any additional information about your solution
5. Application must be publicly available

Additional notes:
1. Apply best practices, feel free to change application configuration where needed

Have fun! :)