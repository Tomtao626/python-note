from fastapi import FastAPI, HTTPException, status, Request, responses
import uvicorn

app = FastAPI()

items = dict(foo="the foo ttt fff")


# HTTPException捕获异常信息
@app.get('/items/{item_id}')
async def read_items(item_id: str):
    if item_id not in items:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Item not found',
                            headers={"X-Error": "There goes my error"})
    return dict(item=items[item_id])


# 自定义HTTPException异常信息
class UnicornException(Exception):
    def __init__(self, name: str):
        self.name = name


@app.exception_handler(UnicornException)
async def unicorn_exception_handler(request: Request, exc: UnicornException):
    """
    :param request:
    :param exc:
    :return:
    """
    return responses.JSONResponse(status_code=status.HTTP_408_REQUEST_TIMEOUT,
                                  content=dict(message=f"Oops! {exc.name} did something. There goes a rainbow..."))


@app.get("/unicorn/{name}")
async def read_unicorn(name: str):
    """
    :param name:
    :return: dict
    """
    if name == "yolo":
        raise UnicornException(name=name)
    return dict(unicorn_name=name)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8088, reload=True, debug=True)
