from apps import app


@app.task(name='test2')
def sub(x, y):
    return x - y
