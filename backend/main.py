from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Adaptive Learning System Backend is running!"}


@app.get("/questions")
def get_question():
    return {
        "id": 1,
        "question": "What is the time complexity of binary search?",
        "topic": "Searching",
        "difficulty": "Easy"
    }