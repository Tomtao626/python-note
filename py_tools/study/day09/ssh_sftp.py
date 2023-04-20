import paramiko
transport = paramiko.Transport(('192.168.144.137',22))
transport.connect(username = 'taopeng',password='7518')
sftp = paramiko.SFTPClient.from_transport(transport)
#将location.py上传至服务器 /tmp/test.py
#sftp.put('123.html','/tmp/test_from_win')
#将remove_path下载到local_path
sftp.get('/home/taopeng/examples.desktop','fromlinux.txt')

transport.close()