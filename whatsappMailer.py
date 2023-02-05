from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import urllib
import time

def espera_pagina_carregar(navegador):
    while len(navegador.find_elements(By.ID, 'pane-side')) < 1: 
        time.sleep(1)
    time.sleep(7)

def envia_mensagens(pessoas):
    navegador = webdriver.Firefox()
    navegador.get("https://web.whatsapp.com")
    espera_pagina_carregar(navegador)
    for pessoa in pessoas:
        if pessoas[pessoa] != "-":
            try:    
                telefone = pessoas.get(pessoa)
                texto = f"Ola, {pessoa}. Mensagem de lembrete padrao"
                texto = urllib.parse.quote(texto)
                link = f"https://web.whatsapp.com/send?phone={telefone}&text={texto}"
                navegador.get(link)
                espera_pagina_carregar(navegador) 
                navegador.find_element(By.XPATH,'/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div/span[2]/div/div[2]/div[2]/button').click()
            except:
                print(f"Mensagem para {pessoa} nao enviada")
            time.sleep(10)