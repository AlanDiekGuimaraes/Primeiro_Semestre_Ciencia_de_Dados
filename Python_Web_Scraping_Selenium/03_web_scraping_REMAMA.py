'''
Instalar as bibliotecas:
    pip install webdriver-manager
    pip install selenium
    pip install pandas as pd
    pip install openpyxl
    
'''
import pandas as pd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

url = 'https://www.instagram.com'

navegador.get(url)

# Carregar o arquivo Excel com os dados de logim e senha
caminho_arquivo = 'C:/Users/84284528572/OneDrive/Documentos/GitHub/Python_Web_Scraping_Selenium/Codigos/Login_e_senha.xlsx'
dados_excel = pd.read_excel(caminho_arquivo)

# Extrair os valores das células A2 = Login e B2 = Senha
valor_celula_A2 = dados_excel.iloc[0, 0]  # Índice 0 para a linha 1, índice 0 para a coluna A = Login
valor_celula_B2 = dados_excel.iloc[0, 1]  # Índice 0 para a linha 1, índice 1 para a coluna B = Senha


# Login no instagram
time.sleep(5)

navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys(valor_celula_A2) # Inseri o E-mail no comboBox
time.sleep(5)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys(valor_celula_B2) # Inseri a Senha no ComboBox
time.sleep(5)
navegador.find_element('xpath', '//*[@id="loginForm"]/div/div[3]').click() # Clica no botão para efetuar o login
time.sleep(5)

''' 
navegador.find_element(By.CLASS_NAME, '_ac8f').click() # Clica no botão "Agora não" sobre Salvar suas informações de login
time.sleep(2)
navegador.find_element('xpath', '/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]').click() # Clica no botão de ativar notificações 
time.sleep(2)
'''
navegador.get('https://www.instagram.com/remamadragaorosa/') # Entrando no instagram do REMAMA. 
time.sleep(2)
#qtd_publicacoes = navegador.find_elements(By.CLASS_NAME, '_ac2a')[0].text # Pegando a quantidade de publicações
#qtd_seguidores = navegador.find_elements(By.CLASS_NAME, '_ac2a')[1].text # Pegando a quantidade de seguidores
#qtd_seguindo = navegador.find_elements(By.CLASS_NAME, '_ac2a')[2].text # Pegando a quantidade de seguindo 

print()
print(50*'=')
print()
time.sleep(2)

link_postagem = navegador.find_element(By.CLASS_NAME, "_ac7v.xzboxd6.xras4av.xgc1b0m") # Pega a CLASS_NAME da primeira postagem
link_postagem.find_element(By.TAG_NAME, "a").click() # Clica na primeira postagem do remama

botao = navegador.find_element(By.CLASS_NAME, "_abm0") # Pega a CLASE onde está o botão de AVANÇAR e VOLTAR

reels = 0
post = 0
contador = 0
while True:
    # Capturando os dados 
    print(f'POSTAGEM {contador + 1}')
    try:
        titulo_postagem = navegador.find_elements(By.CLASS_NAME, '_a9zs')[0].text
    except:
        print('Sem titulo')
  
    print(f'Titulo da postagem: {titulo_postagem}')

    data_postagem = navegador.find_element(By.CLASS_NAME, 'x1p4m5qa').text
    print(f'Data da postagem: {data_postagem}')
    
    try:
        rell = navegador.find_element(By.TAG_NAME, "video")
        if rell:
            reels += 1
            print('Rells')
    except NoSuchElementException:
        post += 1
        print('Post')
    try:
        botao = navegador.find_element(By.CSS_SELECTOR, "svg[aria-label='Avançar']")
        if botao:
            botao.click()
            time.sleep(0.3)
    except NoSuchElementException:
        time.sleep(4)
        break
    
    #qtd_curtidas = navegador.find_elements(By.CLASS_NAME, 'html-span')[4].text
    try:
       qtd_curtidas_visualizacoes= navegador.find_elements(By.CLASS_NAME, '_aauw')[0].text
       print(f'Quantidade de visualizações: {qtd_curtidas_visualizacoes}') 
    except:
       qtd_curtidas_visualizacoes = navegador.find_element(By.CSS_SELECTOR, 'body > div.x1n2onr6.xzkaem6 > div.x9f619.x1n2onr6.x1ja2u2z > div > div.x1uvtmcs.x4k7w5x.x1h91t0o.x1beo9mf.xaigb6o.x12ejxvf.x3igimt.xarpa2k.xedcshv.x1lytzrv.x1t2pt76.x7ja8zs.x1n2onr6.x1qrby5j.x1jfb8zj > div > div > div > div > div.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe.x1qjc9v5.xjbqb8w.x1lcm9me.x1yr5g0i.xrt01vj.x10y3i5r.xr1yuqi.xkrivgy.x4ii5y1.x1gryazu.x15h9jz8.x47corl.xh8yej3.xir0mxb.x1juhsu6 > div > article > div > div.x1qjc9v5.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x78zum5.xdt5ytf.x1iyjqo2.x5wqa0o.xln7xf2.xk390pu.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x65f84u.x1vq45kp.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x11njtxf > div > div > div.x78zum5.xdt5ytf.x1q2y9iw.x1n2onr6.xh8yej3.x9f619.x1iyjqo2.x18l3tf1.x26u7qi.xy80clv.xexx8yu.x4uap5.x18d9i69.xkhd6sd > section.x12nagc.x182iqb8.x1pi30zi.x1swvt13 > div > div > span > a > span').text
       print(f' Quantidade de curtidas: {qtd_curtidas_visualizacoes}')
    contador+=1
    time.sleep(0.5)
    botao = navegador.find_element(By.CSS_SELECTOR, "svg[aria-label='Avançar']")  # Clica no botão de AVANÇAR para ir pra proxima publicação
    botao.click()
    print()
    print(50*'=')
    print()

print(f'Quantidade de Publicações: {qtd_publicacoes}')
print(f'Total de Rells: {reels}')
print(f'Total de Posts: {post}')
print(f'Quantidade de seguidores: {qtd_seguidores}')
print(f'Quantidade que estão seguindo: {qtd_seguindo}')



