# Task API

## Description

This is a simple CRUD API built using FastAPI. It allows users to create, read, update, and delete tasks. The project stores data in memory and provides interactive API documentation using Swagger UI.

---

## Technologies Used

- Python 3
- FastAPI
- Uvicorn
- Git
- GitHub

---

## Installation

### Clone the repository

```bash
git clone https://github.com/sanjureddy17/task-api.git
```

### Move into the project

```bash
cd task-api
```

### Install dependencies

```bash
pip install fastapi uvicorn
```

### Run the application

```bash
python -m uvicorn main:app --reload
```

The server will start at:

```
http://127.0.0.1:8000
```

---

## Swagger Documentation

Open:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | / | Home |
| GET | /health | Health Check |
| GET | /tasks | Get all Tasks |
| GET | /tasks/{task_id} | Get Task by ID |
| POST | /tasks | Create a Task |
| PUT | /tasks/{task_id} | Update a Task |
| DELETE | /tasks/{task_id} | Delete a Task |

---

## Sample cURL Command

```bash
curl -X GET http://127.0.0.1:8000/tasks
```

Example Response:

```json
[
  {
    "id": 1,
    "title": "Study Python",
    "done": false
  }
]
```

---

## Swagger Screenshot

Add a screenshot of your Swagger UI here.

Example:

![Swagger UI](swagger.png)

---
## API Test Example

GET /tasks executed successfully using Swagger UI.
![GET Tasks](get-tasks.png)

## Author

Sanjana