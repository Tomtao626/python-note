# -*- coding: utf-8 -*-
# @Author: Administrator
# @Date:   2019-12-08 17:08:31
# @Last Modified by:   Administrator
# @Last Modified time: 2019-12-08 18:18:29

import socket
import re


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

    client_socket_list = list()

    while True:
        # 等待新客户端的连接
        try:
            new_socket, client_addr = tcp_server.accept()
        except Exception as e:
            pass
        else:
        new_socket.setblocking(False)
        client_socket_list.append(new_socket)

        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as e:
                pass
            else:
                if recv_data:
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)

    # 关闭监听套接字
    tcp_server.close()


if __name__ == "__main__":
    main()
