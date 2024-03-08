from fastapi import FastAPI
import os
import requests
from dotenv import load_dotenv

URL = "https://wordsapiv1.p.rapidapi.com/words/{word}/{mode}"

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


def get_definition(word: str, mode: str):
    res_definition = []
    response = requests.get(URL.format(word=word, mode=mode), headers=headers)
    data = response.json()
    res_definitions = data["definitions"]
    for data in res_definitions:
        res_definition.append(data["definition"])
    return res_definition


def get_synonyms(word: str, mode: str):
    response = requests.get(URL.format(word=word, mode=mode), headers=headers)
    data = response.json()
    res_synonyms = data["synonyms"]
    return res_synonyms


@app.get("/word/{word}/")
def word(word):
    res_definitions = get_definition(word=word, mode="definitions")
    res_synonyms = get_synonyms(word=word, mode="synonyms")
    english_word = f"{word}"
    english_definition = res_definitions
    english_synonyms = res_synonyms
    return {
        "word": english_word,
        "definition": english_definition,
        "synonyms": english_synonyms,
    }
