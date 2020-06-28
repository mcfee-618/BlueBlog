# -*- coding: utf-8 -*-

##TODO 定时备份数据库脚本同时发邮件
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
from dotenv import load_dotenv


load_dotenv()


os.system("sh backup.sh")



sender= os.getenv("email_address")

from_addr = os.getenv("email_address")
password = os.getenv("password")
print(password)
receivers = [os.getenv("email_address")]  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
 
#创建一个带附件的实例
message = MIMEMultipart()
message['From'] = Header("菜鸟教程", 'utf-8')
message['To'] =  Header("测试", 'utf-8')
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')
 
#邮件正文内容
message.attach(MIMEText('这是菜鸟教程Python 邮件发送测试……', 'plain', 'utf-8'))
 
# 构造附件1，传送当前目录下的 test.txt 文件
att1 = MIMEText(open('/tmp/blogfei.sql', 'rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
att1["Content-Disposition"] = 'attachment; filename="blogfei.sql"'
message.attach(att1)
  
try:
    server = smtplib.SMTP_SSL()
    server.connect("smtp.163.com",465)
    # 登录发信邮箱
    server.login(from_addr, password)
    server.sendmail(sender, receivers, message.as_string())
    print ("邮件发送成功")
except smtplib.SMTPException:
    print ("Error: 无法发送邮件")
