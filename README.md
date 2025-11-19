# Docker Learning
🚀 Docker Learning Module – README / Learning Summary
📌 Overview

This module introduced me to the foundational concepts of Docker, containers, images, Dockerfiles, and Docker Compose, and then guided me through building a real multi-container application using Flask and Redis.

By the end of the module, I built a fully containerised web app with a persistent Redis counter and learned how to orchestrate both services using Docker Compose.

🧠 What I Learned
🔹 1. Understanding Containers

What containers are and how they differ from virtual machines

Why containers are lightweight, portable, and reproducible

How containers help developers avoid “it works on my machine” problems

🔹 2. Docker Images & Docker Hub

What a Docker image is and how it’s used as a template for containers

How to pull official images (e.g., python, redis) from Docker Hub

Image layers and caching

How Docker uses your Dockerfile to build custom images

🔹 3. Dockerfile Basics

I learned how to write a Dockerfile that:

Chooses a base image (python:3.9)

Sets a working directory

Installs dependencies from requirements.txt

Copies project files into the image

Exposes the app port

Defines the container’s startup command

This taught me how to package a Python app into a fully isolated container.

🔹 4. Running Containers

I learned how to run containers using commands like:

docker build -t <image-name> .
docker run -p host_port:container_port <image-name>
docker ps
docker logs <container>
docker exec -it <container> bash


This gave me hands-on experience with building, running, and interacting with containers in a real workflow.

🔹 5. Introduction to Redis

This module also introduced me to Redis as a key–value store. I learned:

How key–value databases work

How Redis increments values atomically

How to run Redis in Docker

How to connect a Python Flask app to Redis

🔹 6. Flask + Redis Integration

I created a simple Flask web application with two routes:

/ → welcome message

/count → increments a Redis key "visits" and displays the count

This helped me understand:

Using environment variables

Creating a Redis client in Python

How a backend interacts with an in-memory database

🔹 7. Docker Compose

One of the biggest skills gained was orchestrating multiple containers using Docker Compose.

I learned how to:

Launch multiple services with one command

Automatically create container networks

Pass environment variables to containers

Link containers so Flask can communicate with Redis

Use depends_on to control startup order

Key command:

docker compose up --build


With this, I successfully ran a multi-service architecture:

web → Flask app

redis → Redis database

All working together seamlessly.

🔹 8. Testing & Debugging

I learned how to:

Test containers with curl/browser

Inspect Redis using redis-cli

Use docker compose logs to debug issues

Restart and rebuild when changes are made

📚 Skills Gained (Summary)
Skill	Description
Docker Basics	Images, containers, Dockerfile, CLI commands
Docker Compose	Multi-container orchestration
Networking	How containers communicate internally
Python Backend	Flask routing, environment variables
Redis	Atomic counters, key–value storage
Debugging	Checking logs, exec into containers
🏁 Final Result

I built a fully containerised micro-application consisting of:

A Flask API

A Redis database

A Dockerfile for building the web image

A Docker Compose setup for running both services together

This is a real-world example of how modern applications are built, shipped, and run in the DevOps ecosystem.
