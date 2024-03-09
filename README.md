# TechTrends Web Application

This is a Flask application that lists the latest articles within the cloud-native ecosystem.

## Run 

### On Host

To run this application there are 2 steps required:

1. Initialize the database by using the `python init_db.py` command. This will create or overwrite the `database.db` file that is used by the web application.
1.  Run the TechTrends application by using the `python app.py` command. The application is running on port `3111` and you can access it by querying the `http://127.0.0.1:3111/` endpoint.

### On Docker

To run this application in a Docker container, you can use the following commands:

1. Build the Docker image by using the `make build` command. This will create a Docker image with the `techtrends:latest` tag.
1. Run the Docker container by using the `make run` command. This will start a Docker container with the `techtrends` image and expose the application on port `7111`.

### On Kubernetes

To run this application in a Kubernetes cluster, you can use the following commands:

1. Apply the Kubernetes deployment by using the `make k_apply` command. This will create a deployment and a service in the `sandbox` namespace (after creating the namespace if it doesn't exist).
2. Check that the app is running by shelling into a pod within the `sandbox` namespace and running the `wget -qO- http://{CLUSTER_IP}:4111/healthz` command. (or the `curl` equivalent)

## Changelog

### 2024-03-09 17:03:51: Step 6:

- Add the ArgoCD manifests
- Document the ArgoCD commands

### 2024-03-04 00:12:59: Step 5

- Added Helm chart for the application

### 2024-03-03 16:49:56: Step 4

- Added K8s deployment files

### 2024-03-03 16:12:10: Step 3

- Added CI step to build the image & push to Docker Hub

### 2024-03-02 23:28:05: Step 2

- Dockerize the application

### 2024-03-02 18:03:42: Step 1

- Added the /healthz endpoint
- Added the /metrics endpoint
- Added logging
