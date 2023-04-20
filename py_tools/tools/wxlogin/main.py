import hashlib
import uvicorn
import xmltodict
from fastapi import FastAPI, Query
from fastapi.responses import PlainTextResponse, JSONResponse

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    """
    say hello
    :param name:
    :return:
    """
    return {"message": f"Hello {name}"}


@app.get("/wechat/")
async def wechat_handler(signature: str = Query(...),
                         timestamp: str = Query(...),
                         nonce: str = Query(...),
                         echostr: str = Query(...)):
    """
    wx_login
    :param signature:
    :param timestamp:
    :param nonce:
    :param echostr:
    """
    if not signature:
        JSONResponse("tomtao626")
    token = "1qazxsw2"
    conf_list = [token, timestamp, nonce]
    conf_list.sort()
    # 加密
    info = "".join(conf_list)
    sha1 = hashlib.sha1()
    sha1.update(info.encode())
    sha1_sign = sha1.hexdigest()
    if signature != sha1_sign:
        return ""
    return PlainTextResponse(echostr)


@app.post("/subscribe/")
async def subscribe(request: Request):
    """
    关注订阅/取消订阅
    :param request:
    """
    req = await request.body()
    xmlmsg = xmltodict.parse(req)["xml"]["Event"]

    if xmlmsg == "SCAN":
        pass
    elif xmlmsg == "subscribe":
        pass
    else:
        pass
    return JSONResponse("success")

if __name__ == '__main__':
    uvicorn.run(app="main:app", host="0.0.0.0", port=8080, reload=True)
