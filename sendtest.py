#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.utils import formataddr
import sys

 
my_sender='xxxxxxxx'    
my_pass = 'xxxxxxxx'             
my_receiver='xxxxxxxx'      
filename="log."+sys.argv[1]+".out"
def mail():
	ret=True
	try:
		msg=MIMEMultipart()
		msg['From']=formataddr(["FromWhom",my_sender])  
		msg['To']=formataddr(["ToWhom",my_receiver])              
		msg['Subject']="Training finished"
		msg.attach(MIMEText('Training finished','plain','utf-8'))
		att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
		att1["Content-Type"] = 'application/octet-stream'
		att1["Content-Disposition"] = ('attachment;filename="%s"'%filename)
		msg.attach(att1)
		server=smtplib.SMTP_SSL("smtp.qq.com", 465)  
		server.login(my_sender, my_pass)  
		server.sendmail(my_sender,[my_user,],msg.as_string())  
		server.quit()
		
	except Exception:  
		ret=False
	return ret



ret=mail()
if ret:
	print("email success")
else:
	print("email fail")
