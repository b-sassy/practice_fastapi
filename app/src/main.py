from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv


URL_DEFINITIONS = "https://wordsapiv1.p.rapidapi.com/words/{word}/definitions"
URL_SYNONYMS = "https://wordsapiv1.p.rapidapi.com/words/{word}/synonyms"

load_dotenv()

APK = os.environ["API_KEY"]
APH = os.environ["API_HOST"]

headers = {"X-RapidAPI-Key": APK, "X-RapidAPI-Host": APH}


app = FastAPI()

@app.get("/")
def hello_world():
    return {"message": "Hello World"}

@app.post("/echo/")
def echo(message: str):
    return {"content": message}

@app.get("/hoge/")
def hoge():
    with open("./hoge.txt") as f:
        content = f.read()
    return {"content": content}

def get_definition(word: str):
    res_definition = []
    response = requests.get(URL_DEFINITIONS.format(word=word), headers=headers)
    data = response.json()
    print(data)
    res_definitions = data["definitions"]
    for data in res_definitions:
        print(data["definition"])
        # for i in data["definition"]:
        res_definition.append(data["definition"])
    return res_definition
    print(res_definitions)
    return res_definitions

def get_synonyms(word: str):
    response = requests.get(URL_SYNONYMS.format(word=word), headers=headers)
    data = response.json()
    print(data)
    res_synonyms = data["synonyms"]
    return res_synonyms

@app.get("/word/{search_english_word}/")
def word(search_english_word):
    res_definitions = get_definition(word=search_english_word)
    res_synonyms = get_synonyms(word=search_english_word)
    english_word = f"{search_english_word}"
    english_definition = res_definitions
    english_synonyms = res_synonyms
    return {
            "word": english_word,
            "definition": english_definition,
            "synonyms": english_synonyms
            }
