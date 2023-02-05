import email
# import os
from email.message import EmailMessage
import ssl
import smtplib

# "financeiro.leprechauns.rugby@gmail.com"
# senha = os.environ.get(LEPRESENHA)
def envia_email(destinatario):
    try:
        email = EmailMessage()
        email['From'], email['To'] = "correaiuri86@gmail.com", destinatario[1]
        email['Subject'] = "Lembrete do pagamento da mensalidade"
        email.set_content(f"""
            Bom dia, {destinatario[0]}.
             Gostaríamos, em nome do financeiro do lepre, de lembrá-lo de realizar o pagamento da sua mensalidade no valor de R$30
        """)
        senha = "zyixpaabciohafkg"
        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = ssl.create_default_context()) as smtp_con:
            smtp_con.login(email['From'], senha)
            smtp_con.sendmail(email['From'], email['To'], email.as_string())
        return 1
    except:
        print("Email para o destinatario: {destinatario[0]} nao enviado")
        return 0

def envia_emails(pessoas):
    for nome in pessoas:
        email = pessoas.get(nome)
        try:
            if (nome and email and "@" in email):
                envia_email([nome, email])
        except:
            print("Registro Invalido")