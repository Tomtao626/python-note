import socket
client = socket.socket()
client.connect(('localhost',9999))

while True:
    cmd = input('>>>:').strip()
    if len(cmd) == 0:
        continue
    client.send(cmd.encode('utf-8'))
    cmd_res_size = client.recv(1024)  #接受命令结果的长度
    print("指令结果大小：",cmd_res_size)
    recv_size = 0
    recv_data = b''
    while recv_size < int(cmd_res_size.decode()):
        data = client.recv(1024)
        recv_size += len(data)  #每次收到的有可能小于1024，所以必须用len（）判断
        #print(data.decode())
        recv_data += data
    else:
        print("cmd_res received done",recv_size)
    #cmd_res = client.recv(1024)

        print(recv_data.decode())
client.close()
