from fastapi import FastAPI


app = FastAPI()


@app.get('/')
async def hello():
    return {"text": "hello world!"}

