import requests
from bs4 import BeautifulSoup

target_url = "https://animex.my/anime/blue-box/"

try:
    response = requests.get(target_url)
    response.raise_for_status()
    html_content = response.text
except requests.exceptions.RequestException as e:
    print(f"Error occurred while fetching the webpage: {e}")
    exit(1)

soup = BeautifulSoup(html_content, "lxml")

links = soup.find_all("a", href=True)
for link in links:
    print(f"Link: {link['href']}")

apis = soup.find_all("a", href=lambda href: href and (href.endswith(".json")))
for api in apis:
    print(f"API: {api['href']}")

title = soup.title.string
print(f"Title of the webpage: {title}")

paragraphs = soup.find_all("p")
for i, p in enumerate(paragraphs, start=1):
    print(f"Paragraph {i}: {p.text.strip()}")
