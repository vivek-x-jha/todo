# task_api

A tiny FastAPI project for managing tasks with plain Python code. It keeps everything in memory (a simple list), so it is easy to read and understand.

## What is an API?

An API is a way for a program to expose features over the web. Instead of clicking buttons, you send a request to a URL and get back JSON data. Think of it like calling a Python function, but through the browser.

## The Task class

This project uses one custom class, `Task`, to represent a single task. Each task has:

- `id` (int)
- `title` (str)
- `done` (bool)

The class has a `to_dict()` method so it can be returned as JSON.

## How to run the server

1) Clone the project:

```
git clone <your-repo-url>
cd todo
```

2) Install dependencies from the lockfile (or resolve them if no lockfile exists):

```
uv sync
```

3) Start the server:

```
uv run uvicorn main:app --reload
```

4) Open your browser at:

```
http://127.0.0.1:8000
```

## How to test the API

### In the browser

- `GET /` shows a hello message.
- `GET /tasks` shows all tasks.
- `POST /tasks?title=Buy%20milk` creates a task.
- `POST /tasks/1/done` marks task 1 as done.

You can type these URLs into the browser for the `GET` endpoints. For `POST`, the browser address bar does not send POST requests, so use the docs page below.

### Using the docs UI

FastAPI provides an interactive page at:

```
http://127.0.0.1:8000/docs
```

You can click an endpoint, fill in values, and press **Execute** to send requests.

## Mental model

"Python function → URL → JSON response"

Each FastAPI function maps to a URL. When you visit that URL, the function runs and returns JSON.
