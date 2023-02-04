from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib
import time
import os

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

navegador = webdriver.Firefox()
navegador.get("https://web.whatsapp.com")
while len(navegador.find_elements(By.ID, 'side')) < 1: 
    time.sleep(1)
time.sleep(2)

cadastros = coleta_telefones("Planilha.csv")
for pessoa in cadastros:
    telefone = cadastros.get(pessoa)
    texto = f"Ola, {pessoa}. Mensagem de lembrete padrao"
    texto = urllib.parse.quote(texto)
    link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements(By.ID, 'side')) < 1: 
        time.sleep(1)
    time.sleep(2) 
    
