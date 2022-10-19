import time

import uvicorn
from fastapi import FastAPI, status, HTTPException, Request
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.responses import JSONResponse, PlainTextResponse
from fastapi.exceptions import RequestValidationError

app = FastAPI()


@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


@app.exception_handler(RequestValidationError)
async def validationerror_exception_handler(request, exc):
    return JSONResponse(dict(msg=f"触发了RequestValidationError错误, 错误信息{str(exc)}"))


@app.get('/items/{item_id}')
async def read_item(item_id: int):
    return dict(item_id=item_id)


@app.middleware('http')
async def add_process_time(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers['X-Process-Time'] = str(process_time)
    return response


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8088, reload=True, debug=True)
