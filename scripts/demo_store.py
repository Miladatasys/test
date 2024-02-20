import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

url = 'http://demo-store.seleniumacademy.com/'

path_driver = r'C:\Projects\test\drivers\chromedriver.exe'

service = Service(executable_path=path_driver)

driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get(url)

text_1 = driver.find_element(By.XPATH, '//nav/ol/li/a[contains(text(), "Women")]')
print(text_1.text)


texts_2 = driver.find_elements(By.XPATH, '//nav/ol/li/a')
for i in texts_2:
    print(i.text)


account = driver.find_element(By.XPATH,'//span[contains(text(), "Account")]')
account.click()

register = driver.find_element(By.XPATH,'//li/a[@title="Register"]')
register.click()

# Rellenar formulario
first_name = driver.find_element(By.XPATH, '//input[@id="firstname"]')
first_name.send_keys('Camila')

middle_name = driver.find_element(By.XPATH, '//input[@id="middlename"]')
middle_name.send_keys('Cami')

last_name = driver.find_element(By.XPATH, '//input[@id="lastname"]')
last_name.send_keys('Morales')


email_address = driver.find_element(By.XPATH, '//input[@id="email_address"]')
email_address.send_keys('Cmorales@gmail.com')

password = driver.find_element(By.XPATH, '//input[@id="password"]')
password.send_keys('123456.')

password_confirmation = driver.find_element(By.XPATH, '//input[@id="confirmation"]')
password_confirmation.send_keys('123456.')

check_input = driver.find_element(By.XPATH, '//input[@type="checkbox"]')
check_input.click()

register = driver.find_element(By.XPATH, '//button[@title="Register"]')
register.click()

time.sleep(10)

driver.quit()