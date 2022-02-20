from bs4 import BeautifulSoup
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
import lxml

#Opens a new window of Chrome
driver = webdriver.Chrome()
driver.get("https://www.amazon.in")
driver.maximize_window()

sleep(3)

search = driver.find_element_by_id("twotabsearchtextbox")
product = input("What product's data do you want?")
search.send_keys(product)
#wait to load and type
search.send_keys(Keys.ENTER)
sleep(3)

data = BeautifulSoup(driver,'lxml')
print(data)
