from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db import get_all_tasks, get_task_by_id

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

class TaskUpdate(BaseModel):
    title: str
    done: bool
# GET ALL TASKS
@app.get("/tasks")
def get_tasks():
    return get_all_tasks()   
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
@app.get("/tasks/{id}")
def get_task(id: int):

    task = get_task_by_id(id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )

    
@app.delete("/tasks/{id}", status_code=204)
def delete_task(id: int):

    for task in tasks:

        if task["id"] == id:

            tasks.remove(task)

            return

    raise HTTPException(
        status_code=404,
        detail="Task not found"
    )