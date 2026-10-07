from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Text(BaseModel):
    text:str
@app.post("/analyze_text")
def analyze_text(content:Text):
    try:
        text=content.text
        if not text:
            raise ValueError("text cannot be empty")
        characters=len(text)
        word=text.split()
        word_count=len(word)
        unique_words=set(word)
        unique_words_count=len(unique_words)
        sentences=text.split(".")
        sentences_count=len(sentences)-1
        average_word_length=characters/word_count
        uppercase_text=text.upper()
        lowercase_text=text.lower()
        return{
        "characters":characters,
        "word_count":word_count,
        "unique_words":unique_words,
    "unique_words_count":unique_words_count,
    "sentences_count":sentences_count,
    "average_word_length":average_word_length,
    "uppercase_text":uppercase_text,
    "lowercase_text":lowercase_text
    }
    except Exception as e:
        return {"error":str(e)}



