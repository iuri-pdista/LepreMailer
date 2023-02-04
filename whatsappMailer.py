from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import time

def cria_lista_telefones(cadastros):
    pessoas = {}
    for cadastro in cadastros:
        if cadastro:
            nome, telefone = cadastro.split(",")[0], cadastro.split(",")[1]
            pessoas[nome] = telefone
    return pessoas

def coleta_telefones(nomeDoArquivo):
    with open(nomeDoArquivo, 'r') as cadastros:
        return cria_lista_telefones(cadastros.read().split("\n")) 

def espera_pagina_carregar():
    while len(navegador.find_elements(By.ID, 'pane-side')) < 1: 
        time.sleep(1)
    time.sleep(7)

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com")
espera_pagina_carregar()
cadastros = coleta_telefones("Planilha.csv")
for pessoa in cadastros:
    try:    
        telefone = cadastros.get(pessoa)
        texto = f"Ola, {pessoa}. Mensagem de lembrete padrao"
        texto = urllib.parse.quote(texto)
        link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
        navegador.get(link)
        espera_pagina_carregar() 
    
        navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
    except:
        print(f"Mensagem para {pessoa} nao enviada")
    time.sleep(10)
