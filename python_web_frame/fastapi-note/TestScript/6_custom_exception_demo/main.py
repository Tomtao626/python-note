import uvicorn
from fastapi import FastAPI, HTTPException, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse, JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()


# @app.exception_handler(StarletteHTTPException)
# async def http_exception_handler(request, exc):
#     return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def vailidation_exception_handler(request, exc):
    # return JSONResponse(dict(msg=f"触发了RequestValidationError错误, 错误信息{str(exc)}"))
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

@app.get('/items/{item_id}')
async def read_item(item_id: int):
    if item_id == 3:
        raise HTTPException(status_code=status.HTTP_418_IM_A_TEAPOT, detail="又是什么错误呀，谁让你传3的!")
    return dict(item_id=item_id)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8088, reload=True, debug=True)