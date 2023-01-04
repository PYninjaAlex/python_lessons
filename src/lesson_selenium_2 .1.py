from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium import webdriver


ser = Service('.\chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=op)

driver.get('https://skysmart.ru/programmirovanie-dlya-detej')
div = driver.find_elements(by=By.CLASS_NAME, value='school-achievement-number')

students, projects = div[0].text, div[2].text
print(f'Количество студентов: {students}')
print(f'Количество проектов: {projects}')