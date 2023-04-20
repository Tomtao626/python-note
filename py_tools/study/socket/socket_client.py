import socket
    #客户端
client = socket.socket()
client.connect(('localhost',9999))
while True:
    msg = input("-->：").strip()
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print("recv:",data.decode())

client.close()