import smtplib, ssl

host = "smtp.gmail.com"
port = 465

#username = "theo.reznaugad@gmail.com"
username = "oldmcdonnell@gmail.com"
password = "tqba yvlt vgqw xoym"

receiver = "oldmcdonnell@gmail.com"
context = ssl.create_default_context()

message = """
Hi,
How Are You?
Goodbye"""
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
