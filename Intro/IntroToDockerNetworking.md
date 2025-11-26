
# Basic Networking Concepts in Docker

Docker provides three main networking modes for containers:

## 1. Bridge
- **Default network mode** for containers.
- Creates a **private internal network** on the host.
- Containers communicate through a **virtual bridge**.
- Useful for **isolating containers** while allowing controlled communication.

## 2. Host
- Removes network isolation between container and host.
- Container uses the **host’s network stack** directly.
- No separate IP for the container; it shares the host’s IP.
- Good for **performance**, but **less isolation**.

## 3. None
- Disables networking for the container.
- No external or internal network access.
- Useful for **security-sensitive tasks** or when networking is not required.
