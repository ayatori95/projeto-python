# importante : atualizar a biblioteca BeautifulSoup atravez do pip3 install --upgrade beautifulsoup4
# importante : atualizar a biblioteca requests atravez do pip install requests
import re
import requests
from bs4 import BeautifulSoup as bs
import sys
#-------------------------------------------------------------------#
#------Desenvolvido por Lorena Buriti e Ana Beatriz Tavares---------#
#-------------------------------------------------------------------#

inicio = "Sim"
while inicio == "Sim" :
  url = input("Endereco do link:\n>>> ")
  page = requests.get (url) 
  if page.status_code == 200 : # informa se o web scraping foi bem sucessdido : se aparecer 200 foi.  
   denovo = "Sim"
   while denovo == "Sim" :
    nav = input("Selecione o item que deseja : \n 1)  Listar os topicos do ındice do artigo \n 2) Listas todos os nomes de arquivos de imagens presentes no artigo; \n 3) Listas todas as referencias bibliograficas disponıveis na pagina; \n 4) Listar todos os links para outros artigos da Wikipedia que sao citados no conteudo do artigo \n >>")
    if nav =="1":
     soup = bs(page.content, 'html.parser')
     aEles = soup.findAll('li', class_='toclevel-1')
     texts = '\n'.join(i.text for i in aEles if i.text != '')
     print(texts)
     denovo = input('Deseja retornar ao menu? (Sim/Não)')
    elif nav =="2":
     soup = bs(page.content, 'html.parser')
     aEles = soup.findAll('img')
     # texts = '\n'.join(i.text for i in aEles if i.text != '')
     print(aEles)
     denovo = input('Deseja retornar ao menu? (Sim/Não)')
    elif nav =="3":
     soup = bs(page.content, 'html.parser')
     aEles = soup.findAll('span', class_="reference-text")
     texts = '\n'.join(i.text for i in aEles if i.text != '')
     print(texts)
     denovo = input('Deseja retornar ao menu? (Sim/Não)')
    elif nav =="4":
     soup = bs(page.content, 'html.parser')
     aEles = soup.findAll('li', class_='toclevel-1')
     texts = '\n'.join(i.text for i in aEles if i.text != '')
     print(texts)
     denovo = input('Deseja retornar ao menu? (Sim/Não)') 
    else :
     nav = None
     print ("Valor invalido, digite um valor válido para navegar.")
     
     
  else :
     print ("Sua url contem algum erro.")
     inicio = input("Deseja voltar ao início? (Sim/Não)")
