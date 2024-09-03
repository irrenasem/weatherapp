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

### Deployment:

You can pull the Docker image from Docker Hub:
docker pull irrenasem/weatherapp

**Kubernetes Deployment with Helm:**


