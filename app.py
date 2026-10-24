import os
from dotenv import load_dotenv
from extract_data import scrape_and_save
from flask import Flask, jsonify, render_template, request
from flask_cors import CORS
from groq import Groq

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Store the active file path globally for chat context
ACTIVE_FILE_PATH = None


@app.route("/")
def home():
  """Renders the main frontend interface."""
  return render_template("index.html")


@app.route("/scrape", methods=["POST"])
def scrape_url():
  """Receives URL, triggers scraper, and saves data in uploads/."""
  global ACTIVE_FILE_PATH
  data = request.get_json()
  url = data.get("url", "").strip()

  if not url:
    return jsonify({"error": "URL is required"}), 400

  # Execute scraping and saving
  result = scrape_and_save(url)

  if result["success"]:
    ACTIVE_FILE_PATH = result["path"]
    return jsonify({
        "message": "Website data extracted successfully!",
        "filename": result["filename"],
    })
  else:
    return jsonify({"error": result["error"]}), 500


@app.route("/chat", methods=["POST"])
def chat_with_bot():
  """Handles user chat queries using the currently active scraped file context."""
  global ACTIVE_FILE_PATH

  if not ACTIVE_FILE_PATH or not os.path.exists(ACTIVE_FILE_PATH):
    return (
        jsonify({"error": "No website data loaded. Please submit a URL first."}),
        400,
    )

  try:
    data = request.get_json()
    user_message = data.get("message", "").strip()

    if not user_message:
      return jsonify({"error": "Message is required"}), 400

    # Read context from the active uploaded file
    with open(ACTIVE_FILE_PATH, "r", encoding="utf-8") as file:
      website_context = file.read()[:4000]

    system_prompt = f"""
        You are an intelligent AI assistant.
        Answer user queries based strictly on the provided context below.

        Context:
        {website_context}
        """

    # Call Groq API safely
    chat_completion = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ],
        temperature=0.7,
    )

    bot_reply = chat_completion.choices[0].message.content
    return jsonify({"reply": bot_reply})

  except Exception as error:
    # Catches API errors cleanly and prevents NameError
    return jsonify({"error": str(error)}), 500


if __name__ == "__main__":
  app.run(debug=True, port=5000)