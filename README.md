# python-chatgpt

Nana python-chatgpt

Modified so desired programming language can be selected with parameter.

Based on 
TechWorld with Nana
Python Automation with ChatGPT

## Usage

### OpenAI API Key

Set environment variable with API key.

```
export OPENAI_API_KEY=
```

### Run Python script

````
usage: code_chatgpt.py [-h] [-pl PROGRAMMING_LANGUAGE] prompt file_name

positional arguments:
  prompt                The prompt to send to the OpenAi API
  file_name             Name of the file to save the code

options:
  -h, --help            show this help message and exit
  -pl PROGRAMMING_LANGUAGE, --programming_language PROGRAMMING_LANGUAGE
                       Programming Language
````

## Examples

````
python3 code_chatgpt.py "print hello world" "hello_world.py"
python3 code_chatgpt.py "print todays date" "todays_date.py"
python3 code_chatgpt.py "create a HelloWorld class to print hello world" "HelloWorld.java

python3 code_chatgpt.py "extract all html headers from a web page, translate to Danish and save the result as a html file" "extract-translate-headers.py"


python code_chatgpt.py "translate text to danish and print it using googletrans" "translate.py"


https://www.techworld-with-nana.com/post/is-devops-profession-right-for-me-13-points-to-consider


 File "/home/codespace/.python/current/lib/python3.10/site-packages/googletrans/gtoken.py", line 62, in _update
    code = self.RE_TKK.search(r.text).group(1).replace('var ', '')
AttributeError: 'NoneType' object has no attribute 'group'

````

## googletrans issue

https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group#52456197

```
pip install googletrans==4.0.0-rc1
```
