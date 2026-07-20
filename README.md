# Task API - FastAPI + SQLite

A simple backend task management API built using FastAPI and SQLite.

## Tech Stack

- Python
- FastAPI
- SQLModel
- SQLite
- Uvicorn

## Features

- Create tasks
- View all tasks
- View task by ID
- Update tasks
- Delete tasks
- SQLite database storage

## Run Project

Install dependencies:

pip install -r requirements.txt

Run server:

uvicorn main:app --reload

API Documentation:

http://127.0.0.1:8000/docs

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | /tasks | Get all tasks |
| GET | /tasks/{id} | Get single task |
| POST | /tasks | Create task |
| PUT | /tasks/{id} | Update task |
| DELETE | /tasks/{id} | Delete task |