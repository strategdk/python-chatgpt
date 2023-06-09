# code-chatgpt

Nana python-chatgpt

Modified so desired programming language can be selected with parameter.

Also, for Python script a docstring is added for generated script as wells as some extra prompt instructions to ensure conformity to pylint.

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

python3 code_chatgpt.py "print todays date" "todays-date.groovy" -pl Groovy

python3 code_chatgpt.py "create a HelloWorld class to print hello world" "HelloWorld.java" -pl Java

python3 code_chatgpt.py "set environment variable in full script" "set-api-key.sh" -pl "schell script"

python3 code_chatgpt.py "list all files in directory to a csv file with one line per file displaying name, path and size in bytes. use os.walk." "new_directory01.py"

python3 code_chatgpt.py "list files in current directory to csv file, one line per file with name, path and size in bytes" "list_files_csv.py"
python3 list_files_csv.py
cat files.csv

python3 code_chatgpt.py "list files in directory of the script file to csv file, one line per file with name, path and size in bytes" "list_files_csv.py"

python3 code_chatgpt.py "extract all html headers from a web page, translate to Danish and save the result into a html file" "extract_translate_headers.py"
````

### Blog post

https://www.techworld-with-nana.com/post/a-guide-of-how-to-get-started-in-it-in-2023-top-it-career-paths

````
python3 code_chatgpt.py "extract all html headers from a web page, translate to Spanish and save the result into an html file" "extract_translate_headers.py"
````

### Clean downloads
```
python3 code_chatgpt.py "go through files in Downloads folder, check their dates and if they are older than 30 days, move them to folder called to_delete" "clean_downloads.py"
```

## googletrans issue

https://stackoverflow.com/questions/52455774/googletrans-stopped-working-with-error-nonetype-object-has-no-attribute-group#52456197

```
pip3 uninstall googletrans
pip3 install googletrans==3.1.0a0
```
