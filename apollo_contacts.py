from flask import Flask, request, jsonify
import requests
api_key="urLasOpQ9dxlUucvgcK_hw"
app = Flask(__name__)

@app.route("/webhook", methods=['POST'])
def app_():
    data = request.get_json()
    return data

if __name__=="__main__":
    app.run()