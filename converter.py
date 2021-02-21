import requests
from bs4 import BeautifulSoup

url = 'https://kurs.com.ua/gorod/2331-chernovcy'

source = requests.get(url)
main_text = source.text

soup = BeautifulSoup(main_text , 'html.parser')

#info = input("Курс якої валюти ви хочете дізнатись?(Введіть значення яке знаходиться  в лапках : Доллар - 'doll', Евро - 'euro', Рубль - 'rub': ")

table = soup.find('table', {'class' : 'table-course'})

doll = table.find_all('td', {'class' : 'td-green'})[0]
doll = doll.text
doll = doll[:6]

euro = table.find_all('td', {'class' : 'td-green'})[1]
euro = euro.text
euro = euro[:6]

rub = table.find_all('td', {'class' : 'td-green'})[2]
rub = rub.text
rub = rub[:5]
rub = rub + ' ГРН'
"""
while True:
	if info == 'doll':
		print(doll)
		break
	elif info =='euro':
		print(euro)
		break
	elif info =='rub':
		print(rub)
		break
	else:
		info = input("Введено неправилььний знак валюти, будь-ласка повторіть споробу?(Введіть значення яке знаходиться  в лапках : Доллар - 'doll', Евро - 'euro', Рубль - 'rub':" )


"""