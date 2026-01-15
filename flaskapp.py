from flask import Flask
import redis

app = Flask(__name__)

# Connect to Redis using the service name
redis_client = redis.Redis(
    host="redis",
    port=6379,
    decode_responses=True
)

@app.route("/")
def home():
    return "Hello! Flask is running inside a Docker container."

@app.route("/count")
def count():
    visits = redis_client.incr("visits")
    return f"Visit count: {visits}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

