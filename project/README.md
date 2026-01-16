# Flask + Redis (Docker Compose)

This project is a simple multi-container application consisting of:
- A Python Flask web application
- A Redis database

The Flask app stores and retrieves a visit counter from Redis.

## Services

### Flask
- Exposes a web server on port 5001
- Provides two routes:
  - `/` → Welcome message
    <img width="2552" height="1020" alt="image" src="https://github.com/user-attachments/assets/6e59be72-be53-4405-a487-b05e410ee9ed" />

 

  - `/count` → Increments and displays a visit count stored in Redis
 
  <img width="1271" height="453" alt="Screenshot 2026-01-16 at 14 24 32" src="https://github.com/user-attachments/assets/5df48004-2ac0-4097-8a82-3146b20b1e16" />


### Redis
- Acts as a key-value store
- Used by Flask to persist the visit count

## How to Run

From the `project` directory:

```bash
docker compose up --build

