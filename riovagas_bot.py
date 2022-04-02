# enconding utf-8

from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
# options.add_argument("--headless")
driver = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))
driver.maximize_window()

title = []
data = []
link = []

url = "https://riovagas.com.br/tag/rio-de-janeiro/page/"
numpage = 1
driver.get(url+str(numpage))
print("====== Bot startado ======")
pag_final = int(input("Página Final:"))

while numpage < pag_final:
    driver.get(url+str(numpage))
    titles = driver.find_elements(By.CLASS_NAME, 'entry-title')
    datas = driver.find_elements(By.CLASS_NAME, 'updated')
    links = driver.find_elements(By.XPATH, '//h2[@class]/a[@href]')

    for i in titles:
        title1 = (i.text)
        title.append(title1)

    for i in datas:
        data1 = (i.text)
        data.append(data1)

    for i in links:
        link1 = (i.get_attribute('href'))
        link.append(link1)

    numpage = int(numpage)+1
dados = list(zip(title, link, data))  # zipa as lista
df = pd.DataFrame(data=dados, columns=[
                  'Título', 'Link', 'Data'])  # Cria DataFrame

# --Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter('pandas_simple.xlsx', engine='xlsxwriter')
# Convert the dataframe to an XlsxWriter Excel object.
df.to_excel(writer, sheet_name='Sheet1')

# --Close the Pandas Excel writer and output the Excel file.
writer.save()

# --Carrega o arquivo do pandas_simple.xlsx
df = pd.read_excel('pandas_simple.xlsx')


'''
    ---Modo Iterativo
    python -i .\main.py  


    '''
