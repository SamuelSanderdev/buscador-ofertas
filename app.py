from selenium import webdriver
from selenium.webdriver.common.by import By
import openpyxl

# Acessar o site http://www.novaliderinformatica.com.br/computadores-gamers
driver = webdriver.Chrome()
driver.get('http://www.novaliderinformatica.com.br/computadores-gamers')

# Extrair todos os titulos
titulos = driver.find_elements(By.XPATH,"//a[@class='nome-produto']")

# Extrair todos os preços
precos = driver.find_elements(By.XPATH,"//strong[@class='preco-promocional']")

# Inserir os títulos e preços na planilha

# Criando a planilha
workbook = openpyxl.Workbook()
# Criando a página 'produtos'
workbook.create_sheet('produtos')
# Selecionando a página produtos
sheet_produtos = workbook['produtos']
# Nomeando a coluna Produtos
sheet_produtos['A1'].value = 'Produto'
sheet_produtos['B1'].value = 'Preço'

# Inserir os titulos e os preços na planilha
for titulo, preco in zip(titulos, precos):
    sheet_produtos.append([titulo.text,preco.text])

# Salvando a Planilha no formato .xlsx
workbook.save('produtos.xlsx')

# como entregar para o cliente