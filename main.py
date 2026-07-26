from fastapi import FastAPI, HTTPException

app = FastAPI()

tasks = [
    {
        "id": 1,
        "title": "Study FastAPI",
        "done": False
    },
    {
        "id": 2,
        "title": "practise fastapi",
        "done": True
    },
    {
        "id": 3,
        "title": "complete assigmant",
        "done": False
    }
]
@app.get("/tasks/{id}")
@app.get("/tasks/{id}")
def get_task(id: int):

    for task in tasks:
        if task["id"] == id:
            return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )