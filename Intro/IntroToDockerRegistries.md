# Introduction to Docker Registries

A **Docker Registry** is a system for storing and sharing Docker images — like a GitHub for container images.

## Key Features:

- **Public Registries**  
  → Anyone can pull (and sometimes push) images.  
  → Example: [Docker Hub](https://hub.docker.com/) — the default registry.

- **Private Registries**  
  → Only authorized users or systems can access images.  
  → Ideal for company apps, secrets, or internal tools.  
  → Examples: AWS ECR, Google Container Registry, Azure Container Registry, self-hosted Harbor.

---

✅ Use registries to:
- Share images with your team or the world.
- Deploy the same image across dev, staging, and production.
- Version and manage your containerised apps at scale.
