from flask import Flask, request, jsonify
from webhook_handler import process_webhook

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    result = process_webhook(data)
    return jsonify(result), 200
