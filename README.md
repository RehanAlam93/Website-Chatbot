# Chat with Any Website (RAG-based Web App)

A lightweight Flask web application that allows users to input any website URL, automatically extracts its textual content, saves it into an organized directory, and lets you chat intelligently with an AI assistant based strictly on that website's content.

## 🚀 Features

- **Dynamic URL Scraping:** Enter any standard website URL to scrape and extract its core structural content (headings, paragraphs, lists) while bypassing standard access blocks.
- **Smart File Management:** Automatically cleans the website domain name (e.g., `en_wikipedia_org.txt`) and saves the extracted text inside an `uploads/` folder.
- **Conditional Chat Interface:** The chat widget remains hidden until the website data is successfully loaded and validated.
- **Context-Aware AI Assistant:** Powered by the **Groq API**, ensuring accurate responses grounded strictly in the scraped website text.
- **Clean UI:** Built with an integrated, responsive floating chat interface using modern HTML, CSS, and JavaScript.

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask, Flask-CORS, python-dotenv
- **Web Scraping:** BeautifulSoup4, Requests
- **AI / LLM:** Groq API
- **Frontend:** HTML5, CSS3, JavaScript (Fetch API)

---

## 📁 Project Structure

```text
website-chatbot/
│
├── uploads/              # Automatically stores scraped website .txt files
├── templates/
│   └── index.html        # Main frontend interface and integrated chat widget
├── .env                  # Environment variables (Groq API Key)
├── app.py                # Main Flask backend application and routes
├── extract_data.py       # Scraping and text parsing logic
└── requirements.txt      # Python dependencies