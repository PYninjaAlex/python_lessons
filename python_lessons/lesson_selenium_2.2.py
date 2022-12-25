import time
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from random import randint
from selenium.webdriver import ActionChains


def rand():
    time.sleep(randint(1,3))

ser = Service('.\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://skysmart.ru/programmirovanie-dlya-detej')

rand()
div = driver.find_element(by=By.CLASS_NAME, value='form')
rand()
inputs = div.find_elements(by=By.TAG_NAME, value='input')
rand()
div_button = driver.find_element(by=By.TAG_NAME, value='skysmart-button')
rand()
button = div_button.find_element(by=By.CLASS_NAME, value='-primary-blue')


name = 'Alex'
phone = '89213234845'
email = 'tdffdsfsd@mail.ru'

rand()
inputs[0].send_keys(name)
rand()
inputs[1].send_keys(phone)
rand()
inputs[2].send_keys(email)
rand()
ActionChains(driver).click(button).perform()


print('Finished!')
input()