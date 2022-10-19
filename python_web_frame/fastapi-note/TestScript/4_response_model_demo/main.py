from typing import Dict

import uvicorn
from fastapi import FastAPI, status
from pydantic import BaseModel

app = FastAPI()


# 1-使用response_model定义
# 请求一个接口返回来我们客户端可见的东西都是所谓的响应报文，如响应头，响应码，响应内容等。
class UserIn(BaseModel):
    username: str
    password: str
    email: str
    full_name: str = None


class UserOut(BaseModel):
    username: str
    email: str
    full_name: str = None


# 关于响应状态码status_code
# @app.post('/users/', response_model=UserOut, status_code=200)
@app.post('/users/', response_model=UserOut, status_code=status.HTTP_201_CREATED)
async def create_user(*, user: UserIn):
    return user


# 通常再定义我们的API返回响应的时候，一般是返回固定JSON格式的，所以可以直接使用定义response_model为一个字典
@app.get('/keyword_weights/', response_model=Dict[str, float])
async def read_keyword_weights():
    return dict(foo=2.3, ggg=1.4)


if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8088, reload=True, debug=True)
