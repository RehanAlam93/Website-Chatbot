#  Website RAG Chatbot with Flask & Groq AI

A fully functional, lightweight Retrieval-Augmented Generation (RAG) chatbot web application built using **Python (Flask)**, **BeautifulSoup** for web scraping, and **Groq AI** for lightning-fast LLM responses. This application allows users to scrape content from any website (such as Wikipedia) and chat intelligently with an AI assistant grounded in that specific context.

---

##  Features

* **Dynamic Web Scraping:** Automatically extracts structured content (headings, paragraphs, lists) from target websites using BeautifulSoup.
* **Context-Aware AI (RAG):** Feeds scraped website data into the system prompt so the LLM provides accurate answers specific to that source.
* **Groq API Integration:** Leverages high-performance LLMs via Groq for instant, intelligent responses.
* **Clean Web UI:** A modern, responsive chat interface (`templates/chatbot.html`) built with HTML/CSS/JavaScript.
* **Token-Optimized:** Includes built-in safeguards to truncate long contexts and prevent rate-limit (TPM/413) errors.

---

##  Project Structure

```text
Website Chatbot/
│                  # CSS and JavaScript files for frontend UI
├── templates/               # HTML template files (chatbot.html)
├── .env                     # Environment variables (Groq API Key)
├── app.py                   # Main Flask backend server and chat endpoint
├── extract_data.py          # Web scraping script to fetch and save website text
├── Artificial_intelligence.txt # Scraped context data file
├── requirements.txt         # Project dependencies
└── README.md                # Project documentation