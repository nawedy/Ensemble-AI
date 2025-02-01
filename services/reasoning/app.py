from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/reason', methods=['POST'])
def reason_task():
    data = request.json
    prompt = data.get('prompt')
    if not prompt:
        return jsonify({"error": "No prompt provided"}), 400

    response = openai.Completion.create(
        engine="gpt-4",
        prompt=prompt,
        max_tokens=150
    )

    return jsonify(response.choices[0].text.strip())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
