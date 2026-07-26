from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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
class TaskCreate(BaseModel):
    title: str
# GET ALL TASKS
@app.get("/tasks")
def get_tasks():
    return tasks    
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    if task.title.strip() == "":
        raise HTTPException(
            status_code=400,
            detail="Title cannot be empty"
        )

    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "done": False
    }

    tasks.append(new_task)

    return new_task