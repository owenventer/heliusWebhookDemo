from flask import Flask, request, jsonify, send_from_directory
import os
app = Flask(__name__)

# This will store the latest webhook data
latest_data = {}

@app.route('/webhook', methods=['POST'])
def webhook():
    global latest_data
    latest_data = request.json
    return '', 200

@app.route('/latest', methods=['GET'])
def get_latest():
    return jsonify(latest_data)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)