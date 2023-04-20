import time
from celery import Celery

app = Celery("celery_test", broker="redis://localhost:6379/1", backend="redis://localhost:6379/2")


@app.task()
def hello(name):
    time.sleep(5)
    print(f"hello world---{name}")
    return f"hello world---{name}"


@app.task()
def add_task(x, y):
    print(x + y)
    return x + y
