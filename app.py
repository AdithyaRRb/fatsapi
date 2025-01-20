from fastapi import FastAPI
from transformers import pipeline

#create new fastapi app instance
app=FastAPI()

#initialize thetext generation pipeline
pipe = pipeline("text2text-generation", model="google/flan-t5-small")


@app.get("/")
def home():
    return {"message": "hello world"}

@app.get("/generate")
def generate(text:str):
    output=pipe(text)

    return {"output":output[0]['generated_text']}