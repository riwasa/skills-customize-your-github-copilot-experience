# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using the FastAPI framework. You'll create a small web service with CRUD-style endpoints, explore automatic API docs, and run the app locally using Uvicorn.

## 📝 Tasks

### 🛠️	Build a Basic FastAPI Service

#### Description
Create a FastAPI application that exposes endpoints to create, read, update, and delete simple in-memory items. Use Pydantic models for request/response validation.

#### Requirements
Completed project should:

- Implement a FastAPI `app` with the following endpoints:
  - `GET /items` — return a list of items
  - `GET /items/{item_id}` — return a single item by id (404 if not found)
  - `POST /items` — create a new item and return it with an assigned id
  - `PUT /items/{item_id}` — update an existing item (404 if not found)
  - `DELETE /items/{item_id}` — delete an item (404 if not found)
- Use Pydantic models for request and response schemas.
- Store data in-memory (a Python list/dict is fine) so the app remains single-file and easy to run.
- Handle validation errors and return appropriate HTTP status codes.
- Include a short README section describing how to run the service locally.

### 🛠️	Explore Docs & Testing

#### Description
Use FastAPI's built-in OpenAPI docs and add a couple of simple tests or manual test instructions.

#### Requirements

- Verify that interactive docs are available at `/docs` (Swagger UI) and JSON schema at `/openapi.json`.
- Manually test the endpoints using curl, httpie, or a browser. Optionally add a couple of automated tests (pytest + httpx) for the core endpoints.

### ✨ Stretch Goals (optional)

- Add query parameters for filtering or pagination on `GET /items`.
- Add simple dependency-based authentication (API key header check).
- Persist data to a small JSON file between runs.

---

How to run (locally):

1. Create and activate a venv (recommended).
2. Install dependencies:

```
pip install -r requirements.txt
```

3. Start the app with Uvicorn:

```
uvicorn starter-code:app --reload
```

Open http://127.0.0.1:8000/docs to view the interactive API docs.

Files provided with this assignment:

- `starter-code.py` — minimal FastAPI app to use as a starting point.
- `requirements.txt` — Python dependencies to install.

Place any extra data files here if you implement persistence.
