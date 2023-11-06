import smtplib

to = input("Enter Email Address of the receiver")

message = input("Enter the Maeesage :-")
def sendEmail(to , message):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login("senderemail","password")
    server.sendmail(senderemail, to, message)
    server.close()
    
sendEmail(to , message)