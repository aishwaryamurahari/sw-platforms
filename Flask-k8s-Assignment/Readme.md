# Project Name: Flask-k8s-Assignment

## Description
This project is an assignment for the CMPE272 course, focusing on deploying a Flask application on Kubernetes.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/Flask-k8s-Assignment.git`
2. Navigate to the project directory: `cd Flask-k8s-Assignment`
3. Install the required dependencies: `pip install -r requirements.txt`

## Contributing
1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature`
3. Make your changes and commit them: `git commit -m "Add your changes"`
4. Push to the branch: `git push origin feature/your-feature`
5. Submit a pull request

## Deployment on Kubernetes using Kind

To deploy this application on Kubernetes using Kind, follow these steps:

1. Install Kind by following the official documentation: [Kind Installation Guide](https://kind.sigs.k8s.io/docs/user/quick-start/#installation)

2. Create a Kind cluster:
    ```bash
    kind create cluster --name my-cluster
    ```

3. Build the Docker image for the Flask application:
    ```bash
    docker build -t flask-app .
    ```

4. Load the Docker image into the Kind cluster:
    ```bash
    kind load docker-image flask-app --name my-cluster
    ```

5. Apply the Kubernetes deployment and service manifests:
    ```bash
    kubectl apply -f flaskdeployment.yaml
    kubectl apply -f flaskservice.yaml
    kubectl apply -f dbdeployment.yaml
    kubectl apply -f dbservice.yaml
    ```

6. Verify that the application is running:
    ```bash
    kubectl get pods
    ```
7. Use node port forwarding to access the application in local
   ```
   kubectl port-forward service/web-service 8080:80
   kubectl port-forward service/db-service 5432:5432
   ```
8. Access the application in your browser at `http://localhost:8080`

That's it! Your Flask application is now deployed on Kubernetes using Kind.
