# Weather App

This Python application fetches the current weather and the forecast for a future date in a specified city using the OpenWeatherMap API.

## Features

- **City-based weather data**: Fetch current weather conditions for any city.
- **Future date forecast**: Retrieve weather forecast for a specified future date.
- **Dockerized**: Easily deployable using Docker.
- **CI/CD**: Automated build, test, and deployment pipeline with GitHub Actions and Argo CD.

## Prerequisites

- Python 3.9+
- Docker
- Kubernetes (for deployment)
- Helm (for Kubernetes package management)
- Argo CD (for continuous deployment)

## Setup and Installation

### Clone the Repository
```bash
git clone https://github.com/irrenasem/weatherapp.git
cd weather-app
```
### Install Dependencies
```bash
pip install -r requirements.txt
```
### Run the Application Locally
```bash
python weather_app.py
```
###
Kubernetes Deployment with Helm
 Package the Helm chart:
 ```bash
helm package charts/weather-app
```
Deploy to Kubernetes:
```bash
    helm install weather-app ./weather-app-0.1.0.tgz
```
Continuous Deployment with Argo CD
```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl apply -f weatherapp/argo-app.yaml
kubectl port-forward svc/argocd-server -n argocd 8080:443
```


