import os
from email.message import EmailMessage
import ssl
import smtplib

# remetente = "financeiro.leprechauns.rugby@gmail.com"
# senha = os.environ.get(LEPRESENHA)
def manda_email():
    email = EmailMessage()
    email['From'], email['To'] = "correaiuri86@gmail.com", "iuricorrea05@gmail.com"
    email.set_content("FALA PUTA")
    senha = "zyixpaabciohafkg"
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl.create_default_context()) as smtp_con:
        smtp_con.login(email['From'], senha)
        smtp_con.sendmail(email['From'], email['To'], email.as_string())



