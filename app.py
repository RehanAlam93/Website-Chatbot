import os
from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from groq import Groq

# Load environment variables from .env file
load_dotenv()

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable CORS for frontend and backend communication

# Initialize Groq client using the API key from environment variables
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Load the Artificial Intelligence context and truncate it to avoid Token limit (413 error)
try:
  with open("Artificial_intelligence.txt", "r", encoding="utf-8") as file:
    full_text = file.read()
    # Limit to first 3000 characters to stay well within the on_demand TPM limit (8000 tokens)
    website_context = full_text[:3000]
except FileNotFoundError:
  website_context = "No context available."


# Route to render the main website page
@app.route("/")
def home():
  return render_template("index.html")


# Define the chat endpoint to handle incoming user messages
@app.route("/chat", methods=["POST"])
def chat_with_bot():
  try:
    data = request.get_json()
    user_message = data.get("message", "")

    if not user_message:
      return jsonify({"error": "Message is required"}), 400

    system_prompt = f"""
        You are an intelligent AI assistant.
        Answer user queries based primarily on the provided context below.

        Context:
        {website_context}
        """

    # Call Groq API using the active model available for your key
    chat_completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",  # Active model from your account
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )

    bot_reply = chat_completion.choices[0].message.content
    return jsonify({"reply": bot_reply})

  except Exception as error:
    print(f"Error occurred: {error}")
    return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
  app.run(debug=True, port=5000)