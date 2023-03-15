"""
Write python code for extract all html headers from a web page, 
translate to Danish and save the result into a html file.
Provide code only. No comments.
"""


import requests
from bs4 import BeautifulSoup
from googletrans import Translator

# Get the web page
URL = 'http://strateg.dk/'
response = requests.get(URL, timeout=None)

# Parse the HTML content
soup = BeautifulSoup(response.content, 'html.parser')

# Extract all HTML headers
headers = soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])

# Initialize the translator
translator = Translator()

# Translate the headers to Danish
danish_headers = []
for header in headers:
    danish_headers.append(translator.translate(header.text, dest='da').text)
#danish_headers = [translator.translate(str(header.text), dest='da').text for header in headers]

# Save the result into a HTML file
with open('danish_headers.html', 'w', encoding='utf-8') as f:
    f.write('<html>\n')
    f.write('<head>\n')
    f.write('<title>Danish Headers</title>\n')
    f.write('</head>\n')
    f.write('<body>\n')
    for header in danish_headers:
        f.write(f'<h1>{header}</h1>\n')
    f.write('</body>\n')
    f.write('</html>\n')
