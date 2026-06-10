from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": os.getenv("APPLICATION_NAME"),
        "environment": os.getenv("ENVIRONMENT"),
        "status": "healthy"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })

@app.route("/incidents")
def incidents():
    return jsonify([
        {
            "id": 1,
            "title": "High CPU Usage",
            "status": "OPEN"
        }
    ])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)