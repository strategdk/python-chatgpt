"""
Automating Python with ChatGPT
TechWorld with Nana

export OPENAI_API_KEY=

python3 code_chatgpt.py "print hello world" "hello_world.py"
python3 code_chatgpt.py "print todays date" "todays_date.py"
python3 code_chatgpt.py "create a HelloWorld class to print hello world" "HelloWorld.java

python3 code_chatgpt.py "extract all html headers from a web page, translate to Danish and save the result as a html file" "extract-translate-headers.py"
https://www.techworld-with-nana.com/post/is-devops-profession-right-for-me-13-points-to-consider
"""
import argparse
import os
import requests

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
    DOCSTRING=False
else:
    PROGRAMMING_LANGUAGE="python"
    DOCSTRING=True

CODE_ONLY = " Provide code only. No comments."
PROMPT = f"Write {PROGRAMMING_LANGUAGE} code for " +  args.prompt + CODE_ONLY

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
        if DOCSTRING:
            file.write(f'"""\n{PROMPT}\n"""\n{response_text}\n')
        else:
            file.write(f'{response_text}\n')
else:
    print(f"Request failed with status code: {str(response.status_code)}")