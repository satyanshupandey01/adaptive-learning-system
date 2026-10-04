from fastapi import FastAPI
from backend.database import get_connection

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Adaptive Learning System Backend is running!"}


@app.get("/questions")
def get_questions():
    connection = get_connection()

    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT id, question_text, topic, difficulty
            FROM questions
            ORDER BY id;
            """
        )

        rows = cursor.fetchall()

    connection.close()

    questions = []

    for row in rows:
        questions.append({
            "id": row[0],
            "question": row[1],
            "topic": row[2],
            "difficulty": row[3]
        })

    return questions