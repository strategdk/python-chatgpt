"""
Automating Python and other programming languages with ChatGPT
"""
import argparse
import os
import requests

def split_text(text):
    """Forcing new lines to Strings over 100 characters"""
    result = ""
    line_length = 0
    for word in text.split():
        if line_length + len(word) > 80:
            result = result + "\n" + word
            line_length = len(word) + 1
        else:
            result = result + " " + word
            line_length = line_length + len(word) + 1
    return result[1:]

parser = argparse.ArgumentParser()
parser.add_argument("prompt", help="The prompt to send to the OpenAi API")
parser.add_argument("file_name", help="Name of the file to save the code")
parser.add_argument("-pl", "--programming_language", type=str, help='Programming Language',
                    required=False)
args = parser.parse_args()

API_ENDPOINT = "https://api.openai.com/v1/completions"
API_KEY = os.getenv("OPENAI_API_KEY")

if args.programming_language:
    PROGRAMMING_LANGUAGE=args.programming_language
    PYTHON_LANGUAGE=False
else:
    PROGRAMMING_LANGUAGE="python"
    PYTHON_LANGUAGE=True

CODE_ONLY = ". Provide code only. No comments."
PROMPT = f"Write {PROGRAMMING_LANGUAGE} code to " +  args.prompt + CODE_ONLY
if PYTHON_LANGUAGE:
    PROMPT = PROMPT + " Make code adhere to pylint with a maximum line length of 100."

request_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + API_KEY
}

request_data = {
    "model": "text-davinci-003",
    "prompt": PROMPT,
    "max_tokens": 500, 
    "temperature": 0.5,
}

response = requests.post(API_ENDPOINT, headers=request_headers, json=request_data, timeout=10000)

if response.status_code == 200:
    response_text = response.json()["choices"][0]["text"]
    with open(args.file_name, "w", encoding='utf-8') as file:
        if PYTHON_LANGUAGE:
            SCRIPT_DOCSTRING = split_text(PROMPT)
            file.write(f'"""\n{SCRIPT_DOCSTRING}\n"""\n{response_text}\n')
        else:
            file.write(f'{response_text}\n')
else:
    print(f"Request failed with status code: {str(response.status_code)}")
