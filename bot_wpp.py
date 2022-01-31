from selenium import webdriver
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
#Navegar até o wpp web
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://web.whatsapp.com/')
time.sleep(30)
#Definir contatos e grupos e mensagem a ser enviada
contatos = ['Teste', 'Amorzinho']
mensagem = 'Mensagem enviada atraves de BOT'
def buscar_contato(contato):
    campo_pesquida = driver.find_element_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    time.sleep(3)
    campo_pesquida.click()
    campo_pesquida.send_keys(contato)
    campo_pesquida.send_keys(Keys.ENTER)


def enviar_mensagem(mensagem):
    campo_mensagem = driver.find_elements_by_xpath('//div[contains(@class,"copyable-text selectable-text")]')
    campo_mensagem[1].click()
    time.sleep(3)
    campo_mensagem[1].send_keys(mensagem)
    campo_mensagem[1].send_keys(Keys.ENTER)



for contato in contatos:
    buscar_contato(contato)
    enviar_mensagem(mensagem)
# Buscar contatogrupos
# Campo de pesquisa: copyable-text selectable-text" 
#Campo de mandar mensagem: <div <div role="textbox" class="_13NKt copyable-text selectable-text" contenteditable="true" data-tab="9" dir="ltr" spellcheck="true"></div>