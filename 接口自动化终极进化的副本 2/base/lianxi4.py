#coding:utf-8
import smtplib
from email.mime.text import MIMEText
class SendEmail:
	global send_user
	global email_host
	global password
	email_host = "smtp.163.com"
	send_user = "18526141986@163.com"
	password = "wangshiyu123"
	def send_mail(self,user_list,sub,content):
		user = "Mushishi"+"<"+send_user+">"
		message = MIMEText(content,_subtype='plain',_charset='utf-8')
		message['Subject'] = sub
		message['From'] = user
		message['To'] = ";".join(user_list)
		server = smtplib.SMTP()
		server.connect(email_host)
		server.login(send_user,password)
		server.sendmail(user,user_list,message.as_string())
		server.close()
if __name__ =="__main__":
    sen = SendEmail()
    user_list = ['381213716@qq.com']
    sub = "这个是测试邮件"
    content = "这个是我们的第一峰测试邮件"
    sen.send_mail(user_list,sub,content)