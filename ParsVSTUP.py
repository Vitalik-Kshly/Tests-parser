import requests
from bs4 import BeautifulSoup


URL = 'https://abit-poisk.org.ua/rate2019/direction/611171'

r = requests.get(URL).text
html = BeautifulSoup(r, 'lxml')

blocks = html.findAll('tr', class_ = 'application-status')

arrPrior1 = []
arrPrior2 = []

for block in blocks:
	name =  str(block.findAll('td')[1].text).replace(' ', '')
	try:	
		prior = int(str(block.findAll('td')[2].text).replace(' ', ''))
	except:
		prior = 0
	score = float((block.findAll('td')[3].text).replace(' ', ''))


	# print(name + ' ' + prior + ' ' + score)
	allInfo = (name, score)
	if prior == 1:
		arrPrior1.append(allInfo) 
	elif prior == 2:
		arrPrior2.append(allInfo)


def sSec(val):
	return val[1]

arrPrior1.sort(key = sSec, reverse = True)
arrPrior2.sort(key = sSec, reverse = True)

print(arrPrior1)
print(arrPrior2)

print(str(len(arrPrior1) + arrPrior2.index(('\n\r\nКошлайВ.В.\n', 184.62))))