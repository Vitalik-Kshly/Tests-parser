import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

options = webdriver.ChromeOptions()
options.add_argument('headless')


# def get_html(url):
	# r = requests.get(url).text
	# #print (r.text)

#executable_path = 'Complete E:/phantomjs-2.1.1-windows/bin'

URL = "https://vstup.edbo.gov.ua/offer/611171/"
# URL = 'https://selenium-python.readthedocs.io/locating-elements.html'

def main():

	driver = webdriver.Chrome()
	driver.get(URL)
	a = input()
	# WebDriverWait(driver, 10000)
	divPriorClass = 'request-status-5'
	# Elem = driver.find_element_by_id('searchbox')
	# priorList = HTML.find('div', class_ = 'offer-requests').findAll('div', class_ = 'divPriorClass')
	#priorList = HTML.find_element_by_class(class_ = "divPriorClass")
	# print(Elem)
	driver.close()




main()