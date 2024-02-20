from selenium import webdriver
from selenium.webdriver.common.by import By

url = 'http://demo-store.seleniumacademy.com/'

class Store_Selenium(webdriver.Chrome):

    def __init__(self, path_driver = r'C:\Projects\test\drivers\chromedriver.exe', teardown = False):
        self.path_driver = path_driver
        self.teardown = teardown

        super(Store_Selenium, self).__init__()
        self.maximize_window()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    # Write methods
    def get_url(self):
        self.get(url)

    # Fill form
    
    def fill_form(self):

        account=self.find_element(By.XPATH,'//span[contains(text(), "Account")]')
        account.click()

        register=self.find_element(By.XPATH, '//li/a[@title="Register"]')
        register.click()

        first_name=self.find_element(By.XPATH,'//input[@id="firstname"]')
        first_name.send_keys('Camila')

        midle_name=self.find_element(By.XPATH,'//input[@id="middlename"]')
        midle_name.send_keys('cami')

        last_name=self.find_element(By.XPATH,'//input[@id="lastname"]')
        last_name.send_keys('Morales')

        email=self.find_element(By.XPATH,'//input[@id="email_address"]')
        email.send_keys('ejemplo@correo.com')

        password=self.find_element(By.XPATH,'//input[@id="password"]')
        password.send_keys('abc123')

        password_confirmation=self.find_element(By.XPATH,'//input[@id="confirmation"]')
        password_confirmation.send_keys('abc123')

        check_input=self.find_element(By.XPATH, '//input[@type="checkbox"]')
        check_input.click()

        registro=self.find_element(By.XPATH,'//button[@title="Register"]')
        registro.click()