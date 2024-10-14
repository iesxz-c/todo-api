# Todo FastAPI Application

This is a simple Todo application built with FastAPI.

## API Endpoints

### Get All Todos
- **Endpoint:** `GET /todos/`
- **Description:** Retrieve a list of all todos.

### Create a Todo
- **Endpoint:** `POST /todos/`
- **Request Body:**
  ```json
  {
    "title": "Task Title",
    "description": "Task Description"
  }
