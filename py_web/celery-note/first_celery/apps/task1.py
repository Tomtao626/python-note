from apps import app


@app.task(name='test1')
def add(x, y, name):
    print(name)
    return x + y
