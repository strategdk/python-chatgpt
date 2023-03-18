"""
Write python code for 
extract all html headers from a web page, 
translate to Spanish and save the result into an html file. Provide code only. No comments.
"""


import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Get the web page content
LANG = 'da'
URL = 'https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths'
page = requests.get(URL, timeout=None)

# Parse the HTML
soup = BeautifulSoup(page.content, 'html.parser')

# Extract all the headers from the page
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Initialize the translator
translator = Translator()

# Translate all the headers to Spanish
spanish_headers = []
for header in headers:
    translate_result = {
        "text": translator.translate(header.text, dest=LANG).text,
        "name": header.name
    }
    spanish_headers.append(translate_result)

# Create the HTML file
html_file = open(f'{LANG}_headers.html', 'w', encoding='UTF-8')

# Write the translated headers to the HTML file
html_file.write('<html><head><title>Translated Headers</title></head><body>')
for header in spanish_headers:
    html_file.write(f'<{header["name"]}>{header["text"]}</{header["name"]}>')
html_file.write('</body></html>')

# Close the HTML file
html_file.close()
