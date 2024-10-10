# Todo FastAPI Application

This is a simple Todo application built with FastAPI.

## Live Demo

You can access the live API at the following link:

- [Todo API](https://web-production-4da0.up.railway.app)

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
