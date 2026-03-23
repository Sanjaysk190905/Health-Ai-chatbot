from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# -----------------------------
# HOME ROUTE
# -----------------------------
@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "StudyMate AI (Ollama) Running 🚀"})

# -----------------------------
# CHECK API
# -----------------------------
@app.route("/check", methods=["POST"])
def check():
    try:
        data = request.get_json()

        if not data or "symptoms" not in data:
            return jsonify({"error": "No input provided"}), 400

        user_input = data["symptoms"]

        # 🧠 PROMPT
        prompt = f"""
You are a medical AI assistant.

Give answer STRICTLY in this format:

Fever

Possible Condition:
...

Advice:
- point 1
- point 2

Precautions:
- point 1
- point 2

Rules:
- Each section must be in new line
- Do NOT write paragraph format
- Keep it short and clean

Symptom: {user_input}
"""

        # 🤖 OLLAMA API CALL
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        answer = result.get("response", "No response from model")

        return jsonify({"result": answer})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# -----------------------------
# RUN SERVER
# -----------------------------
if __name__ == "__main__":
    print("🚀 Flask + Ollama running on http://127.0.0.1:5000")
    app.run(debug=True)