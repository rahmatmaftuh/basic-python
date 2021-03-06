import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

sender_email = "rahmatmaftuhi@gmail.com"
rec_email = "rahardiangalih@yahoo.co.id"
subject = "Testing"
password = input(str("please input your password: "))

msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = rec_email
msg['Subject'] = subject

body = "Sorry for spamming. This message was sent by python and part of learning. If you have a dream, don't excuse. We can struggle together"
msg.attach(MIMEText(body,"plain"))

filename = "image.jpg"
attachment = open(filename,"rb")

part = MIMEBase("application","octet-stream")
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header("Content-Disposition", "attachment; filename= "+filename)

msg.attach(part) 
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender_email, password)
print("Login Success")
server.sendmail(sender_email, rec_email, text)
print ("Email has been sent to ", rec_email)

#i got the tutorial from https://www.youtube.com/watch?v=bXRYJEKjqIM. Cheers!