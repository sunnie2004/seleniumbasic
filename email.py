#############################################################################
#email.py
#author: xiaoqing sunny, date:2019-1-3
#function: send message in the email
#############################################################################
import secure_smtplib

email_user = "cjqing1993@gmail.com"
email_send = "cjqing1993@gmail.com"
server = secure_smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,'QAZ12#$wsx')

message = "hi"
server.sendmail(email_user,email_send,message)
server.quit()
