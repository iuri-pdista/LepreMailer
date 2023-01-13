import email
# import os
from email.message import EmailMessage
import ssl
import smtplib

# "financeiro.leprechauns.rugby@gmail.com"
# senha = os.environ.get(LEPRESENHA)
def envia_email(destinatario):
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

def coleta_emails(nomeDoArquivo):
    with open(nomeDoArquivo, 'r') as cadastros:
        return cria_lista_emails(cadastros.read().split("\n"))
        
def cria_lista_emails(cadastros):
    pessoas = {}
    for cadastro in cadastros:
        if cadastro:
            nome, email = cadastro.split(",")[0], cadastro.split(",")[1]
            pessoas[nome] = email
    return pessoas

def organiza_emails(pessoas):
    for pessoa in pessoas:
        if (pessoa[0] and pessoa[1] and "@" in pessoa[1]):
            envia_email(pessoa)
