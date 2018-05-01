#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys

#your username
my_sender='xxxxxxxx'
#your passwd
my_pass = 'xxxxxxxx'
#address you want to send to
my_receiver='xxxxxxxx'

#attachment name
filename="log."+sys.argv[1]+".out"
def mail():
	ret=True
	try:
		msg=MIMEMultipart()
		#from
		msg['From']=formataddr(["FromWhom",my_sender])  
		#to
		msg['To']=formataddr(["ToWhom",my_receiver])              
		#subject of your mail
		msg['Subject']="Training finished"
		#main text
		msg.attach(MIMEText('Training finished','plain','utf-8'))
		
		#attachment
		att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = ('attachment;filename="%s"'%filename)
		msg.attach(att1)
		
		#sending
		server=smtplib.SMTP_SSL("smtp.qq.com", 465)  
		server.login(my_sender, my_pass)  
		server.sendmail(my_sender,[my_receiver,],msg.as_string())  
		server.quit()
		
	except Exception:  
		ret=False
	return ret



ret=mail()
if ret:
	print("email success")
else:
	print("email fail")
