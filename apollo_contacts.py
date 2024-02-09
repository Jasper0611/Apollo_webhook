from flask import Flask, request, jsonify
import requests
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def web_hook():
    return 'Hello'
