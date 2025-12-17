from flask import Flask, request, redirect
from datetime import datetime
import requests

app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "YOUR_WEBHOOK_URL_HERE"

    data = {
        "embeds": [
            {
                "title": ip,
                "description": date
            }
        ]
    }

    try:
        requests.post(webhook_url, json=data, timeout=3)
    except requests.exceptions.RequestException as e:
        print("Webhook failed:", e)


@app.route("/")
def index():
    ip = request.environ.get("HTTP_X_FORWARDED_FOR", request.remote_addr)
    date = datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    return "hello world"

if __name__ == "__main__":
    import os

app.run(
    host="0.0.0.0",
    port=int(os.environ.get("PORT", 5000))
)

