from datetime import datetime, time, timedelta
from uuid import UUID

from fastapi import FastAPI, Path, Body
import uvicorn
from pydantic import BaseModel, Field
from typing import Set, List

"""
一般对于request body不会通过get方式提交，对于get提交的参数一般是称为查询参数，
如果是post/put等方式提交的参数，一般是放到request body请求体中 再提交到后端
对于如何接收和校验请求体，fastapi推荐使用 from pydantic import BaseModel
"""

app = FastAPI()


# 1-request body
class Item(BaseModel):
    name: str
    desc: str = None
    price: float
    tax: float = None


class User(BaseModel):
    username: str
    fullname: str = None


@app.post('/items/')
async def create_item(item: Item):
    return item


# 2-request body 和 Path/Query
@app.put('/items/{item_id}')
async def update_item(*, item_id: int = Path(..., title='the Id of the item to get', ge=0, le=1000), q: str = None,
                      item: Item = None):
    result = dict(item_id=item_id)
    if q:
        result.update(dict(q=q))
    if item:
        result.update(dict(item=item))
    return result


# 3-多个request body提交
"""{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    }
}"""


@app.put('/items2/{item_id}')
async def update_item2(*, item_id: int, item: Item, user: User):
    result = dict(item_id=item_id, item=item, user=user)
    return result


# 更复杂的业务其实会存在多体的Boay的提交，之前做的商城下单里面，客户端有可能就会同时提交多个实体的对象信息到后端，如订单实体，地址实体，商品信息实体等
# 其实就是客户端提交多个实体对象。那可以定义多个模型对象即可。fastapi它会自动帮你处理提取信息。
"""{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    },
    "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
    },
    "importance": 5
}"""


@app.put('/items3/{item_id}')
async def update_item3(*, item_id: int, item: Item, user: User, important: int = Body(..., gt=0)):
    # async def update_item(*, item_id: int, item: Item, user: User):
    result = dict(item_id=item_id, item=item, user=user, important=important)
    return result


# 客户端提交的是一个单体对象内嵌的话，我们需要怎么处理
"""{
    "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
    }
}"""


# FastAPI提供了一个：item: Item = Body(..., embed=True)
@app.put('/items4/{item_id}')
async def update_item4(*, item_id: int, item: Item = Body(..., embed=True)):
    result = dict(item_id=item_id, item=item)
    return result


# 如果另外再假设,客户端提交一个更复杂的嵌套模型的话，嵌套里面有列表有实体。
"""
{
    "name": "Foo",
    "description": "The pretender",
    "price": 42.0,
    "tax": 3.2,
    "tags": ["rock", "metal", "bar"],
    "image": {
        "url": "http://example.com/baz.jpg",
        "name": "The Foo live"
    }
}
"""


# Item5里面包含了Image，也包含了，tags类型的列表定义
# 子内嵌
class Image(BaseModel):
    url: str
    name: str


class Item5(BaseModel):
    name: str
    desc: str = None
    price: float
    tax: float = None
    tags: Set[str] = None
    image: Image = None


@app.put('/items5/{item_id}')
async def update_item5(*, item_id: int, item: Item5):
    result = dict(item_id=item_id, item=item)
    return result


"""
{
    "name":"Foo",
    "description":"The pretender",
    "price":42,
    "items":[
        {
            "name":"Foo",
            "description":"The pretender",
            "price":42,
            "tax":3.2,
            "tags":[
                "rock",
                "metal",
                "bar"
            ],
            "image":{
                "url":"http://example.com/baz.jpg",
                "name":"The Foo live"
            }
        },
        {
            "name":"Foo2",
            "description":"The 2",
            "price":422,
            "tax":3.2,
            "tags":[
                "rock",
                "metal",
                "bar"
            ],
            "image":{
                "url":"http://example.com/baz.jpg",
                "name":"The Foo live"
            }
        }
    ]
}
"""


# 嵌套层级更深的结构 更复杂的结构
# 只需要定义好对应的对象即可
class Item6(BaseModel):
    name: str
    desc: str = None
    price: int
    tax: float = None
    tags: Set[str] = None
    image: Image


class AllItem(BaseModel):
    name: str
    desc: str = None
    price: int
    tax: float = None
    items: List[Item6]


@app.put('/items6/{item_id}')
async def update_item6(*, item_id: int, item: AllItem):
    result = dict(item_id=item_id, item=item)
    return result


# Request Body的Field
# Field字段的意思其实就是类似上面Query, Path，也同样给Body内的字段的信息添加相关的校验。通过Field来规范提交的Body参数信息。

class Item7(BaseModel):
    name: str
    desc: str = Field(None, title='标题', description="错误描述信息", max_length=300)
    price: float = Field(..., gt=0, description="错误描述信息")
    tax: float = None

@app.put('/items7/{item_id}')
async def update_item7(*, item_id: int, item: Item7 = Body(..., embed=True)):
    result = dict(item_id=item_id, item=item)
    return result

"""
对于数据格式的校验，通常，我们不止于

int
float
str
bool

但是提交参数不止于上述的几种格式，有时候比如是对手机号码的校验，有些时候是时间类型的校验等
其他类型：
其他数据类型¶
以下是您可以使用的一些其他数据类型（来自官方文档）：

UUID:

一个标准的“通用唯一标识符”，在许多数据库和系统中常见于ID。
在请求和答复中，将表示为str.


datetime.datetime:

一只Pythondatetime.datetime.
在请求和答复中，将表示为str采用ISO 8601格式，如：2008-09-15T15:53:00+05:00.


datetime.date:

Pythondatetime.date.
在请求和答复中，将表示为str采用ISO 8601格式，如：2008-09-15.


datetime.time:

一只Pythondatetime.time.
在请求和答复中，将表示为str采用ISO 8601格式，如：14:23:55.003.


datetime.timedelta:

一只Pythondatetime.timedelta.
在请求和答复中，将表示为float总秒数。
Pydantic还允许将其表示为“ISO 8601时间差异编码”，有关更多信息，请参阅文档。.


frozenset:

在请求和答复中，将其视为set:
在请求中，将读取列表，消除重复，并将其转换为set.
在答复中，set将转换为list.
生成的架构将指定set值是唯一的(使用JSONSchema的uniqueItems).


bytes:

标准Pythonbytes.
在请求和答复中将被视为str.
生成的架构将指定它是str带着binary“格式”。


Decimal:

标准PythonDecimal.
在请求和响应中，处理方式与float.
"""
# 也可以用其他类型来检验
@app.put("/items8/{item_id}")
async def read_items8(
    item_id: UUID,
    start_datetime: datetime = Body(None),
    end_datetime: datetime = Body(None),
    repeat_at: time = Body(None),
    process_after: timedelta = Body(None),
):
    start_process = start_datetime + process_after
    duration = end_datetime - start_process
    return {
        "item_id": item_id,
        "start_datetime": start_datetime,
        "end_datetime": end_datetime,
        "repeat_at": repeat_at,
        "process_after": process_after,
        "start_process": start_process,
        "duration": duration,
    }

if __name__ == "__main__":
    uvicorn.run(app='main:app', host='127.0.0.1', port=8088, debug=True, reload=True)
