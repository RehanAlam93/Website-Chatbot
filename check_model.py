import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

try:
  models = client.models.list()
  print("--- AVAILABLE MODELS FOR YOUR KEY ---")
  for m in models.data:
    print(m.id)
except Exception as e:
  print("Error:", e)