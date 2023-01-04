from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


driver = webdriver.Chrome(service_log_path=os.devnull)
driver.set_window_position(0, 0)
driver.implicitly_wait(15)

driver.get('https://klik-test.ru/schetchik-klikov')
a = driver.find_element(By.ID, 'click-plus')
for clicks in range(10):
    a.click()
    time.sleep(0.5)

os.system('cls')
time.sleep(1)
driver.quit()
input()
