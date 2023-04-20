# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2019-12-08 17:50:29
# @Last Modified by:   Administrator
# @Last Modified time: 2019-12-09 14:31:52

import socket
import re
import select


def service_client(new_socket, request):
    '''为这个客户端返回数据'''

    # 接受浏览器发送过来的请求，http请求

    # request = new_socket.recv(1024)
    # print(request)
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    '''
        GET /index.html HTTP/1.1
    '''
    file_name = ""
    ret = re.match(r"[^/]+(/[^]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("./html" + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response = "\r\n"
        response = "....filr not found...."
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 返回http格式的数据f给浏览器
        # 准备要发送给浏览器的数据---header

            response_body = html_content

        response_header = "HTTP/1.1 404 NOT FOUND\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode('utf-8') + response_body
        response = "HTTP/1.1 200 OK"
        response += "\r\n"
        # 准备发送给浏览器的数据---body
        # response += "hhhhhhhh"
        new_socket.send(response)

    # 关闭套接字
    new_socket.close()


def main():
    # 创建套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 绑定
    tcp_server.bind(("", 8001))

    # 变为监听套接字
    tcp_server.listen(128)
    tcp_server.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()

    # 将监听套接字对应的fd注册到epoll中
    epl.register(tcp_server, socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()

    while True:

    	fd_event_list = epl.poll()  # 默认会堵塞，直到os检测到数据到来，通过事件通知方式程序，此时才会解堵塞塞

    	# [(fd,event),(套接字对应的文件描述符，这个文件描述符到底是什么事件 例如 可以调用recv接受等)]
    	for fd, event in fd_event_list:
        	# 等待新客户端的连接
        	if fd == tcp_server.fileno():
            	new_socket, client_addr = tcp_server.accept()
            	epl.register(new_socket.fileno(), select.EPOLLIN)
            	fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
            	# 判断已经链接的客户端是否有数据发送过来
            	recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
            	if recv_data:
            		service_client(fd_event_dict[fd], recv_data)
            	else:
        			fd_event_dict[fd].close()
        			epl.unregister(fd)
        			del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server.close()

if __name__ == "__main__":
    main()
