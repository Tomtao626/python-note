from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.middleware('http')
async def log_request(request, call_next):
    """
    :param request:
    :param call_next:
    :return:
    """
    print("请求开始前我可以处理的事情11111")
    response = await call_next(request)
    print("请求开始后我可以处理的事情33333")
    return response


@app.get('/')
async def not_timed():
    print("请求开始后我可以处理的事情22222")
    return dict(msg="你好")

if __name__ == "__main__":
    uvicorn.run(app="main:app", host='127.0.0.1', port=5000, debug=True, reload=True)
