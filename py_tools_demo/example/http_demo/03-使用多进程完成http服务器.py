#coding:utf-8
import socket
import re
import multiprocessing

def service_client(new_socket):
    '''为这个客户端返回数据'''

    # 接受浏览器发送过来的请求，http请求
    
    request = new_socket.recv(1024)
    # print(request)
    request_lines = request.splitlines()
    print("")
    print(">"*20)
    print(request_lines)

    '''
        GET /index.html HTTP/1.1
    '''
    file_name = ""
    ret = re.match(r"[^/]+(/[^]*)",request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"
        


    
    try:
        f = open("./html"+file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 返回http格式的数据f给浏览器
        # 准备要发送给浏览器的数据---header
        response = "HTTP/1.1 200 OK"
        response += "\r\n"
        # 准备发送给浏览器的数据---body
        # response += "hhhhhhhh"
        new_socket.send(response.encode("utf-8"))
        new_socket.send(html_content)

    
    new_socket.close()

def main():
    #创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)

    #绑定
    tcp_server.bind(("",8001))
    
    #变为监听套接字
    tcp_server.listen(128)
    
    while True:
        #等待新客户端的连接
        new_socket, client_addr = tcp_server.accept()

        p = multiprocessing.Process(target=service_client, args=(new_socket,))
        p.start()
        new_socket.close()

        #为这个客户端服务
        service_client(new_socket)
    # 关闭监听套接字
    tcp_server.close()

if __name__ == "__main__":
    main()
