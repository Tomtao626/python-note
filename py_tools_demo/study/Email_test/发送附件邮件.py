from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr,parseaddr
import smtplib

def _format_addr(s):
    name,addr = parseaddr(s)
    return formataddr((Header(name,'utf-8').encode(),addr))
from_addr = input("From:")
password = input("Password:")
to_addr = input("To_addr:")
smtp_server = input("SMTP_Server:")
#邮件对象
msg = MIMEMultipart('send with file..','plain','utf-8')
msg['From'] = _format_addr('Python爱好者 <%s> ' % from_addr)
msg['To'] = _format_addr('管理员 <%s> ' % to_addr)
msg['Subject'] = Header('来自SMTP的问候..','utf-8').encode()
#邮件正文是MIMEText
msg.attach(MIMEText('send with file...','plain','utf-8'))

#加上一个MIMEBase，从本地读取一个图片
with open('E:/test.jpg','rb') as f:
    #设置附件的MIME和文件名
    mime = MIMEBase('image','jpg',filename='test.jpg')
    #加上必要的头信息
    mime.add_header('Content-Disposition','Attachment',filename='test.jpg')
    mime.add_header('Content-ID','<0>')
    mime.add_header('X-Attachment-ID','0')
    #把图片读进去
    mime.set_payload(f.read())
    #编码
    encoders.encode_base64(mime)
    #添加到Multipart
    msg.attach(mime)
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

