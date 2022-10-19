import uvicorn
from fastapi import FastAPI

app = FastAPI()


# 1-TestScript
@app.get('/')
def resp_json():
    json_dict = dict(msg="hello world")
    return json_dict


# 2-添加请求参数
@app.get('/item/{item_id}')
async def read_item(item_id: int):
    return dict(item_id=item_id)


# 3-路由
@app.get('/users/me')
async def read_user_me():
    return dict(user_id='the current user')


@app.get('/users/{user_id}')
async def read_user(user_id: str):
    return dict(user_id=user_id)


# 4-查询路径参数和参数校验
@app.get('/items/')
async def read_page_items(skip: int = 0, limit: int = 10):
    fake_data = [{"item_name": "Foo1"}, {"item_name": "Bar1"}, {"item_name": "Baz1"},
                 {"item_name": "Foo2"}, {"item_name": "Bar2"}, {"item_name": "Baz2"},
                 {"item_name": "Foo3"}, {"item_name": "Bar3"}, {"item_name": "Baz3"},
                 {"item_name": "Foo4"}, {"item_name": "Bar4"}, {"item_name": "Baz4"},
                 {"item_name": "Foo5"}, {"item_name": "Bar5"}, {"item_name": "Baz5"}]
    return fake_data[skip: skip + limit]


# 5-多路径和查询参数
@app.get('/users/{user_id}/items/{item_id}')
async def read_user_item(user_id: int, item_id: int, q: str = None, short: bool = False):
    item = {
        "item_id": item_id, "user_id": user_id
    }
    if q:
        item.update({"q": q})
    if not short:
        item.update({"desc": "This is an amazing item that has a long description"})
    return item


if __name__ == "__main__":
    uvicorn.run(app="main:app", host="127.0.0.1", port=8088, debug=True, reload=True)
