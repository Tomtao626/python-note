from fastapi import FastAPI, Query, Path
import uvicorn
from typing import Optional, List
from enum import Enum

app = FastAPI()


# 1-路径参数和查询参数的必选和可选
@app.get('/item2/{item_id}')
async def read_user_item1(item_id: int, needy: str):
    item = {'item_id': item_id, 'needy': needy}
    return item


# 定义可选参数和必选的参数的提交类型： 其中还可以使用Optional来定义需要提交的数据类型
# 把查询参数limit规定为了int类型，但是它是可选的的参数，设置为了None:
@app.get('/item2/{item_id}')
async def read_user_item2(item_id: str, limit: Optional[int] = None):
    return {'item_id': item_id, 'limit': limit}


# 2-路径参数的枚举
class ModelName(str, Enum):
    resent = 'resent'
    current = 'current'
    alexresent = 'alexresent'


@app.get('/model/{model_name}')
def get_model_name(model_name: ModelName):
    if model_name == ModelName.resent:
        return {'model_name': model_name, 'desc': 'ggggg'}
    if model_name == ModelName.alexresent:
        return {'model_name': model_name, 'desc': 'hhhhh'}
    return {'model_name': model_name, 'desc': 'fffff'}


# 3-查询参数query的参数校验
@app.get('/users/')
async def read_users(q: str = Query(None, min_length=5, max_length=20), regex="^fixedquery$"):
    result = dict(items=[dict(item_id=123, ), dict(item_id=222)])
    if q:
        result.update(dict(q=q))
    return result


# 4-查询参数query参数多值列表
@app.get('/goods/')
async def read_goods(q: List[str] = Query(['foo', 'bar'])):
    query_goods = dict(q=q)
    return query_goods


# 5-路径参数的其他校验方式
# 对于查询参数可以通过Query，同样对于路径参数也可以使用Fastapi自带的Path来进行校验。
# 路径参数是路径的一部分，所以它是必需的，通过"..."将其标记为必需参数，即使默认值给的是None依然是必需参数。可以通过查看Path方法查看传递的更多参数
@app.get('/goods/{goods_id}')
async def read_goods(q: str, goods_id: int = Path(..., title='the Id of the goods to get')):
    result = dict(goods_id=goods_id)
    if q:
        result.update(dict(q=q))
    return result


# 对于路径参数校验中，还可以对item_id进行大于或等于的校验
# 当ge = 1时，goods_id必须是整数 goods_id大于或等于1”
@app.get('/goods/{goods_id}')
async def read_goods(q: str, goods_id: int = Path(..., title='the Id of the goods to get'), ge=1):
    result = dict(goods_id=goods_id)
    if q:
        result.update(dict(q=q))
    return result



if __name__ == "__main__":
    uvicorn.run(app='main:app', host="127.0.0.1", port=8088, reload=True, debug=True)
