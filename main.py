from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from contextlib import asynccontextmanager
from database import create_db_and_tables, get_session
from sqlmodel import select
from models import Task

@asynccontextmanager
async def lifespan(app: FastAPI):
    create_db_and_tables()

    with get_session() as session:
        existing_tasks = session.exec(select(Task)).first()

        if existing_tasks is None:
            sample_tasks = [
                Task(title="Study Python", done=False),
                Task(title="Complete Assignment", done=False),
                Task(title="Go for Walk", done=True)
            ]

            session.add_all(sample_tasks)
            session.commit()

    yield

app = FastAPI(lifespan=lifespan)

class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1)

class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=1)
    done: bool

@app.get("/")
def home():
    return {
        "name": "Task API",
        "version": "1.0",
        "endpoints": ["/tasks"]
    }

@app.get("/health")
def health():
    return {
        "status": "ok"
    }

@app.get("/tasks")
def get_tasks():
    with get_session() as session:
        tasks = session.exec(select(Task)).all()
        return tasks

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    with get_session() as session:
        task = session.get(Task, task_id)

        if task:
            return task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):

    new_task = Task(
        title=task.title,
        done=False
    )

    with get_session() as session:
        session.add(new_task)
        session.commit()
        session.refresh(new_task)

    return new_task

@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskUpdate):

    with get_session() as session:
        db_task = session.get(Task, task_id)

        if db_task:
            db_task.title = task.title
            db_task.done = task.done

            session.add(db_task)
            session.commit()
            session.refresh(db_task)

            return db_task

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )

@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):

    with get_session() as session:
        task = session.get(Task, task_id)

        if task:
            session.delete(task)
            session.commit()
            return

    raise HTTPException(
        status_code=404,
        detail=f"Task {task_id} not found"
    )