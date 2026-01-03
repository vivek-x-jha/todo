from fastapi import FastAPI

app = FastAPI()


class Task:
    def __init__(self, task_id: int, title: str, done: bool) -> None:
        self.id = task_id
        self.title = title
        self.done = done

    def to_dict(self) -> dict[str, object]:
        return {'id': self.id, 'title': self.title, 'done': self.done}


tasks: list[Task] = []


@app.get('/')
def read_root() -> dict[str, object]:
    return {'message': 'Hello from FastAPI'}


@app.get('/tasks')
def get_tasks() -> dict[str, object]:
    return {'tasks': [task.to_dict() for task in tasks]}


@app.post('/tasks')
def add_task(title: str) -> dict[str, object]:
    task_id = len(tasks) + 1
    task = Task(task_id, title, False)
    tasks.append(task)
    return task.to_dict()


@app.post('/tasks/{task_id}/done')
def mark_task_done(task_id: int) -> dict[str, object]:
    for task in tasks:
        if task.id == task_id:
            task.done = True
            return task.to_dict()
    return {'error': 'Task not found'}
