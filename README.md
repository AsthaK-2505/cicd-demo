# 🚀 CI/CD Pipeline for a Dockerized Flask Application

A simple Flask application built to demonstrate an end-to-end CI/CD workflow using Docker, GitHub Actions, GitHub Container Registry (GHCR), and Render.

Every time changes are pushed to the `main` branch, GitHub Actions automatically runs tests, builds a Docker image, publishes it to GHCR, and Render deploys the latest version.

🌐 **Live Demo:** https://cicd-demo-5nm8.onrender.com/

---

## Project Overview

This project was built to gain hands-on experience with modern DevOps practices and understand what happens after code is pushed to GitHub.

The workflow automates:

- Running automated tests with **pytest**
- Building a Docker image
- Publishing the image to **GitHub Container Registry (GHCR)**
- Deploying the latest version on **Render**

---

## Tech Stack

- Python
- Flask
- Docker
- Git & GitHub
- GitHub Actions
- GitHub Container Registry (GHCR)
- Render
- Pytest
- Ubuntu Linux

---

## Project Architecture

```text
             Developer
                 │
             git push
                 │
                 ▼
        GitHub Repository
                 │
                 ▼
      GitHub Actions (CI)
                 │
        Install Dependencies
                 │
            Run Tests
                 │
        Build Docker Image
                 │
        Push Image to GHCR
                 │
                 ▼
      Render Deployment (CD)
                 │
                 ▼
      Live Flask Application
```

---

## Project Structure

```
cicd-demo/
│
├── .github/
│   └── workflows/
│       └── ci.yml
├── app.py
├── test_app.py
├── Dockerfile
├── requirements.txt
├── .dockerignore
└── README.md
```

---

## Running the Project Locally

### Clone the repository

```bash
git clone git@github.com:AsthaK-2505/cicd-demo.git
cd cicd-demo
```

### Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Visit:

```
http://localhost:5000
```

---

## Running with Docker

Build the Docker image

```bash
docker build -t flask-demo .
```

Run the container

```bash
docker run -p 5000:5000 flask-demo
```

Open:

```
http://localhost:5000
```

---

## Running Tests

```bash
pytest -v
```

---

## CI/CD Workflow

Every push to the `main` branch automatically triggers the pipeline.

- Checkout repository
- Install project dependencies
- Run automated tests using **pytest**
- Build a Docker image
- Publish the Docker image to **GitHub Container Registry (GHCR)**
- Render automatically deploys the latest version

---

