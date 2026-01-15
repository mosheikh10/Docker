# Flask + Redis (Docker Compose)

This project is a simple multi-container application consisting of:
- A Python Flask web application
- A Redis database

The Flask app stores and retrieves a visit counter from Redis.

## Services

### Flask
- Exposes a web server on port 5000
- Provides two routes:
  - `/` → Welcome message
  - `/count` → Increments and displays a visit count stored in Redis

### Redis
- Acts as a key-value store
- Used by Flask to persist the visit count

## How to Run

From the `project` directory:

```bash
docker compose up --build

