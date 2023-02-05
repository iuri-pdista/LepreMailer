import lepreMailer as mailer
import whatsappMailer as wa

def tratar_arquivo(nomeDoArquivo):
    with open(nomeDoArquivo) as cadastros:
        original = cadastros.read()
        tratado = original.replace(" ","")
        tratado = tratado.replace(",,", ",-,")
        cadastros.close()
    cadastros = open(nomeDoArquivo, "w")
    cadastros.write(tratado)

def criar_lista(cadastros):
    telefones = {}
    emails = {}
    for pessoa in cadastros:
        if pessoa:
            dados = pessoa.split(",")
            nome, telefone = dados[0], dados[1]
            email = (dados[2] if len(dados) == 3 else "-")
            telefones[nome], emails[nome] = telefone, email
    return (telefones, emails)

def ler_planilha(nomeDoArquivo):
    with open(nomeDoArquivo) as cadastros:
        return criar_lista(cadastros.read().split("\n"))

tratar_arquivo("Planilha.csv")
listas = ler_planilha("Planilha.csv")
telefones, emails = listas[0], listas[1]
mailer.envia_emails(emails)
wa.envia_mensagens(telefones)
