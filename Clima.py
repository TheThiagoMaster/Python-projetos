from bs4 import BeautifulSoup
import requests

# Carregar a página com informações sobre o clima #
html = requests.get("").content #Colocar o endereço dentro destas aspas

# Fazer PARSER no HTML5 #
soup = BeautifulSoup(html, 'html.parser')

# Captura de dados #
resume = soup.find(class_='-gray -line-height-24 _center')
tempMin = soup.find(id='min-temp-1')
tempMax = soup.find(id='max-temp-1')

# resultados #
print('\n Resumo: ' + resume.text)
print(' Temp. Mínima: ' + tempMin.string)
print(' Temp. Máxima: ' + tempMax.string)