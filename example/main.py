from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message" : "Let's study FastAPI"}

@app.get("/home")
def home():
    return {"message" : "Home"}

@app.get("/playground")
def play():
    return {"message" : "Here is our PlayGround !!"}
