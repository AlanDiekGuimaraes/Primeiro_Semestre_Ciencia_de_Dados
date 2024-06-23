from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By
import time

#from selenium.webdriver.chrome.by import By

service = Service() # É usada para instanciar o chrome webdriver
options = webdriver.ChromeOptions() # Definir preferencias do chrome
navegador = webdriver.Chrome(service=service, options=options)

url = "https://www.google.com.br/"

navegador.get(url)


navegador.find_element('xpath', '//*[@id="APjFqb"]').send_keys('Preta')
navegador.find_element('xpath', '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[2]').click()
navegador.find_element('xpath', '//*[@id="movie_player"]/div[8]/button').click()
