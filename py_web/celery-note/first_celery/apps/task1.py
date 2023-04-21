from apps import app


@app.task(name='test1', bind=True)
def add(self, x, y, name):
	print(self)
	print(name)
	return x + y
