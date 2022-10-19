from flask import Flask, request,render_template
from geventwebsocket.websocket import WebSocket
from gevent.pywsgi import WSGIServer
from geventwebsocket.handler import WebSocketHandler

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'upload/'

user_socket_list = []
@app.route("/my_socket")
def my_socket():
    # 获取当前客户端与服务器的Socket连接
    user_socket = request.environ.get("wsgi.websocket")  # type:WebSocket
    if user_socket:
        user_socket_list.append(user_socket)
        print(len(user_socket_list),user_socket_list)
        # 1 [<geventwebsocket.websocket.WebSocket object at 0x000001D0D70E1458>]
        print(user_socket,"OK 连接已经建立好了，接下来发消息吧")
    user_socket.send("3")
    while True:
        # 等待前端将消息发送过来
        print("前端消息！")
        msg = user_socket.receive()
        print(msg)
        user_socket.send(msg)



if __name__ == '__main__':
    #app.run(host='10.1.6.29', port=7708)
    http_serv = WSGIServer(("127.0.0.1",8009),app,handler_class=WebSocketHandler) # 这种启动方式和app.run()不冲突,该启动方式发什么请求都可以接受到
    http_serv.serve_forever()
