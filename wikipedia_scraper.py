import requests
from bs4 import BeautifulSoup
import csv

# URL of the Wikipedia page about "Python (programming language)"
URL = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(URL)
soup = BeautifulSoup(response.content, 'html.parser')

data = []

# Extract the title of the page
title = soup.find('h1', {'id': 'firstHeading'}).text # type: ignore
data.append(['Title', title])

# Extract the main introductory paragraph
intro_paragraph = soup.find('p').text # type: ignore
data.append(['Introduction', intro_paragraph])

# Save the extracted data to a CSV file
with open('output.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    
print("Data has been saved to output.csv")