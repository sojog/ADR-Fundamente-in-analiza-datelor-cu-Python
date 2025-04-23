

## 1. Scraping a website

import requests
from bs4 import BeautifulSoup


URL = "https://www.cursbnr.ro/"

response = requests.get(URL)

print(response.text)

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# print(links)


# Gaseste valoare din /html/body/div[3]/div[1]/div/main/div[2]/div[1]/ul/li[1]/div[1]/div[1]
value_element = soup.find('div', class_='value')

if value_element:
    print(value_element.text)
else:
    print("Nu a fost găsit elementul cu clasa 'value'.")


# Gaseste valoare din <div class="value">1 EURO = 4.9774 Lei</div>
value_element = soup.find('div', class_='value')

if value_element:
    print(value_element.text)
else:
    print("Nu a fost găsit elementul cu clasa 'value'.")