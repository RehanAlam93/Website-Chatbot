from bs4 import BeautifulSoup
import requests

# Target website URL
url = "https://en.wikipedia.org/wiki/Artificial_intelligence"

# Add headers to mimic a real browser and bypass 403 Forbidden error
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
}


def scrape_website_data(target_url):
  try:
    # Send an HTTP GET request with headers
    response = requests.get(target_url, headers=headers)

    # Check if the request was successful
    if response.status_code == 200:
      # Parse the HTML content using BeautifulSoup
      soup = BeautifulSoup(response.text, "html.parser")

      # Extract text from key structural elements (headings, paragraphs, lists)
      extracted_texts = []
      for element in soup.find_all(["h1", "h2", "h3", "h4", "p", "li", "span"]):
        text = element.get_text(strip=True)
        if text:  # Avoid empty strings
          extracted_texts.append(text)

      # Save the extracted text to a file for the GenAI / RAG pipeline
      output_filename = "Artificial_intelligence.txt"
      with open(output_filename, "w", encoding="utf-8") as file:
        file.write("\n".join(extracted_texts))

      print(
          f"Data successfully extracted and saved to '{output_filename}'! Total"
          f" lines: {len(extracted_texts)}"
      )
    else:
      print(f"Failed to fetch the website. Status code: {response.status_code}")

  except Exception as e:
    print(f"An error occurred: {e}")


# Run the scraper function
scrape_website_data(url)