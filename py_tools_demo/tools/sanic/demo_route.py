from sanic import Sanic
from sanic import request
from sanic.response import text, json

app = Sanic(__name__)


@app.route("/")
async def request_demo(request):
	return json({"test": "tomtao626"})


@app.route("/tag/<tag>")
async def request_type_demo(request, tag):
	return json({f"{tag}-test": tag})


@app.route("person/<tag:number>")
async def request_deme2(request, tag):
	return json({"tes": tag})


@app.route("get")
async def get_handler(request):
	return text(request.json)


# add_route
async def add_route_demo(request, name):
	return json({"test": f"sdfsdfsdfsd--{name}"})


async def add_route_demo2(request, name):
	return jsonp({"test2": f"jdjsjdsbjsbcjcdj---{name}"})


@app.websocket('/feed')
async def feed(request, ws):
	try:
		while True:
			data = 'hello!'
			print('Sending: ' + data)
			await ws.send(data)
			data = await ws.recv()
			print('Received: ' + data)
	except Exception as e:
		print(e)


app.add_route(add_route_demo, '/route_demo/<name>', methods=['GET'])
app.add_route(add_route_demo2, '/route2/<name:[A-z]>')
if __name__ == '__main__':
	app.run(access_log=True, debug=True)
