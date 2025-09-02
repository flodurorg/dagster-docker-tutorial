# Dagster Docker Tutorial

![Docker Publish](https://github.com/flodurorg/dagster-docker-tutorial/actions/workflows/docker-publish.yml/badge.svg)

## Introduction

Welcome to the Dagster Docker Tutorial! This repository provides a hands-on introduction to setting up a basic data pipeline using Dagster within Docker containers. Dagster is a powerful data orchestrator tool designed for building, running, and observing data pipelines. Docker enhances this by offering an isolated and consistent environment, making your pipelines portable and scalable. This tutorial will guide you through the process of setting up a simple data pipeline using Dagster within a Docker container and print "Hello, Dagster!" to the console.

## Prerequisites

Before diving into this tutorial, ensure you have the following installed on your machine:

- Docker and Docker Compose
- Python 3.12 or higher

A basic understanding of Python programming, Docker containerization, and data pipeline concepts will be helpful.

## Setup Instructions

### Clone the Repository

Start by cloning this repository to your local machine:

```bash
git clone https://github.com/flodurorg/dagster-docker-tutorial
cd dagster-docker-tutorial
```

### Build the Docker Image

Next, build the Docker image using the provided `Dockerfile`:

```bash
docker build -t dagster-tutorial .
```

### Start the Docker Container

Once the image is built, start the Docker container:

```bash
docker compose up -d
```

### Access the Dagster UI

Open your browser and navigate to `http://localhost:3000` to access the Dagster UI. You should see the Dagster dashboard with the tutorial repository loaded.

## Using the Pre-Built Image

Each push to the `main` branch automatically builds and publishes a Docker image to the GitHub Container Registry.

Pull the latest image:

```bash
docker pull ghcr.io/flodurorg/dagster-docker-tutorial:latest
```

Run it (requires a Postgres instance if you use the compose file):

```bash
docker run -p 3000:3000 ghcr.io/flodurorg/dagster-docker-tutorial:latest
```

Or with docker compose (will rebuild locally if you keep build context):

```bash
docker compose up -d --pull always
```

