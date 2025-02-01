from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

@app.route('/solve', methods=['POST'])
def solve_equation():
    data = request.json
    equation = data.get('equation')
    if not equation:
        return jsonify({"error": "No equation provided"}), 400

    wolfram_alpha_app_id = os.getenv("WOLFRAM_ALPHA_APP_ID")
    url = f"http://api.wolframalpha.com/v2/query?input={equation}&appid={wolfram_alpha_app_id}&output=json"
    response = requests.get(url)
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch solution from Wolfram Alpha"}), 500

    result = response.json()
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
