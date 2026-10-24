import os
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import requests

# Set headers to mimic a real browser request and avoid 403 Forbidden errors
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def scrape_and_save(target_url):
  """Scrapes text content from a given URL and saves it as a .txt file

  inside the uploads directory using the domain name.
  """
  try:
    # Send HTTP GET request to target URL
    response = requests.get(target_url, headers=HEADERS, timeout=10)
    if response.status_code != 200:
      return {
          "success": False,
          "error": f"Failed to fetch URL. Status code: {response.status_code}",
      }

    # Parse HTML response
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract text from main structural tags only (avoiding junk/spans)
    extracted_texts = []
    for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li"]):
      text = element.get_text(strip=True)
      if text:
        extracted_texts.append(text)

    if not extracted_texts:
      return {"success": False, "error": "No valid text content found."}

    # Generate a clean filename from the website domain name
    parsed_url = urlparse(target_url)
    domain_name = parsed_url.netloc.replace(".", "_")
    if not domain_name:
      domain_name = "website_data"

    # Ensure uploads directory exists
    upload_dir = "uploads"
    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(upload_dir, f"{domain_name}.txt")

    # Save extracted text to file with UTF-8 encoding
    with open(file_path, "w", encoding="utf-8") as file:
      file.write("\n".join(extracted_texts))

    return {"success": True, "filename": f"{domain_name}.txt", "path": file_path}

  except Exception as e:
    return {"success": False, "error": str(e)}