from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from db import get_all_tasks, get_task_by_id, create_task, update_task

app = FastAPI()


class TaskCreate(BaseModel):
    title: str
    done: bool = False


class TaskUpdate(BaseModel):
    title: str
    done: bool


# GET ALL TASKS
@app.get("/tasks")
def get_tasks():
    return get_all_tasks()


# CREATE NEW TASK
@app.post("/tasks")
def add_task(task: TaskCreate):

    task_id = create_task(task.title, int(task.done))

    return {
        "id": task_id,
        "title": task.title,
        "done": task.done
    }


# GET TASK BY ID
@app.get("/tasks/{id}")
def get_task(id: int):

    task = get_task_by_id(id)

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return task

@app.put("/tasks/{id}")
def update_task_endpoint(id: int, task: TaskUpdate):

    updated = update_task(
        id,
        task.title,
        int(task.done)
    )

    if updated == 0:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )

    return get_task_by_id(id)


# DELETE TASK
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