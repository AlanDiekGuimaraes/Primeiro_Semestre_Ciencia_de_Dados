import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from datetime import datetime


service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

URL = 'https://www.instagram.com/remamadragaorosa/reels/'

driver.get(URL)

time.sleep(5)
scroll_pause_time = 2  # pausa no tempo do scroll para acompanhar o processo
screen_height = driver.execute_script("return window.screen.height;")  # pega o tamanho da pagina
i = 1
links_set_reels = set()
descs_reels = []

while True:
  # desce a pagina no tamanho de uma tela por vez
  driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))
  i += 1
  time.sleep(scroll_pause_time)

  temp_links_reels = driver.find_elements(By.CSS_SELECTOR, "a[role='link'][href^='/reel/']")[:]

  for link_reel in temp_links_reels:
    links_set_reels.add(link_reel.get_attribute('href'))
  temp_links_reels.clear()

  # print(len(links_set_reels))

  # atualize a altura da rolagem sempre que rolar, pois a altura da rolagem pode mudar depois que rolamos a página
  scroll_height = driver.execute_script("return document.body.scrollHeight;")
  # interrompa o loop quando a altura que precisamos rolar for maior que a altura total da rolagem
  if (screen_height) * i > scroll_height:
    try:   
      login_modal = driver.find_element(By.CSS_SELECTOR, "div[role='dialog']")
      driver.execute_script("document.querySelector('body > div:nth-child(38) > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe > div > div._ab8w._ab94._ab99._ab9f._ab9m._ab9p._ab9z._aba9._abch._abck.x1vjfegm._abcm > div').click()")
      time.sleep(1)
    except NoSuchElementException as error:
      print('Fim dos reels!')
      break

links_reels = list(links_set_reels)

curtidas = []
comentarios = []
datas_publicacoes = []
legendas = []

print(f'Quantidade de reels: {len(links_reels)}')
n_reel = 1

for link in links_reels:
  driver.get(link)
  time.sleep(2)
  print(f'Reel {n_reel}')
  # Acessando as tags meta do DOM de cada reel do instagram do remama, onde contém as informações da publicação
  meta_reel_info = driver.find_element(By.NAME, 'description').get_attribute('content').split('-')
  meta_reel_numbers = meta_reel_info[0].split(',')

  # Extraindo separadamente informações de curtidas, comentários, legenda do post e data de publicação
  curtida = int(meta_reel_numbers[0].replace('likes',''))
  comentario = int(meta_reel_numbers[1].replace('comments ',''))
  data_publicacao = meta_reel_info[1].split(':')[0].split('em ')[1]
  # Formatando data da publicação para o formato correto
  data_formatada = datetime.strptime(data_publicacao, "%B %d, %Y").strftime("%d/%m/%Y")
  legenda = driver.find_element(By.CSS_SELECTOR, "meta[property='og:title']").get_attribute('content').replace('Remama Dragão Rosa Oficial no Instagram: ', '')

  # Adicionando informações do reel visitado nas listas
  curtidas.append(curtida)
  comentarios.append(comentario)
  datas_publicacoes.append(datas_publicacoes)
  legendas.append(legenda)

  n_reel += 1
  # Indo pro próximo reel
  driver.back()

dados_reels = pd.DataFrame({
  'Curtidas': curtidas,
  'Comentários': comentarios,
  'Datas de publicação': datas_publicacoes,
  'Legendas': legendas
})

dados_reels.to_excel('dados_reels_remama.xlsx')
