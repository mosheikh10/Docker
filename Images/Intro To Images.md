# Understanding Dockerfile

A `Dockerfile` is a script that defines how to build a Docker image. Each line is an instruction that layers on top of the previous one.

## Key Instructions:

- **`FROM`**  
  → Specifies the base image to start from (e.g., `python:3.9`, `node:18`, `alpine`).

- **`RUN`**  
  → Executes commands during build time (e.g., `apt-get install`, `pip install`).

- **`COPY`**  
  → Copies files or directories from your host machine into the container.

- **`WORKDIR`**  
  → Sets the working directory for all subsequent instructions (like `cd` in a shell).

- **`CMD`**  
  → Specifies the default command to run when the container starts (can be overridden at runtime).

---

<img width="1168" height="664" alt="image" src="https://github.com/user-attachments/assets/ae088a2d-eca9-4ab3-bfed-a7a2c0e5944c" />

---
 
