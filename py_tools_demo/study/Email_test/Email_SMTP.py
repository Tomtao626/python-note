#构造一个文本邮件
from email.mime.text import MIMEText
msg = MIMEText("hello,this email is send by Python..",'plain','utf-8')
#构造MIMEText对象时，第一个参数为邮件正文，第二个参数是MIME的subtype,'plain'表示纯文本，即'text/plain','utf-8'保证多语言兼容性
#SMTP发送
#首先输入Email地址和指令
'''
from_addr = input('From:')
password = input('Password:')
#输入收件人地址
to_addr= input('To:')
#输入SMTP服务器地址
smtp_server = input('SMTP server:')
import smtplib
server = smtplib.SMTP(smtp_server,25)#SMTP协议默认端口是25
server.set_debuglevel(1)#打印和SMTP服务器交互的所有信息
server.login(from_addr,password)#登录SMTP服务器
#发邮件，由于可以一次发给多人，所以传入一个list,邮件正文是一个str，as_string()把MIMEText对象变成str
server.sendmail(from_addr,[to_addr],msg.as_string())
server.quit()
'''
# 输入Email地址和口令:
from_addr = input('From: ')
password = input('Password: ')
# 输入收件人地址:
to_addr = input('To: ')
# 输入SMTP服务器地址:
smtp_server = input('SMTP server: ')
import smtplib
server = smtplib.SMTP(smtp_server, 25) # SMTP协议默认端口是25
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr,[to_addr], msg.as_string())
server.quit()