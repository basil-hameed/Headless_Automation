from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

class Data:
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    username = "Admin"
    password = "admin123"
    dashboard_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"

# Locators Class to store all the web locators
class Locators:
    username_input_box = "username" # Name Locator
    password_input_box = "password" # Name Locator
    login_button = '//*[@id="app"]/div[1]/div/div[1]/div/div[2]/div[2]/form/div[3]/button' # XPath Locator
    dashboard_text = '//*[@id="app"]/div[1]/div[1]/header/div[1]/div[1]/span/h6'

class DemoText:
    def __init__(self, url):
        self.url = url

    def validate_dashboard_text(self):
        # create driver
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(Data().url)
        sleep(5)

        self.driver.find_element(by=By.NAME, value=Locators().username_input_box).send_keys(Data().username)
        sleep(2)
        self.driver.find_element(by=By.NAME, value=Locators().password_input_box).send_keys(Data().password)
        sleep(2)
        self.driver.find_element(by=By.XPATH, value=Locators().login_button).click()
        sleep(5)

        text_element = self.driver.find_element(by=By.XPATH, value=Locators().dashboard_text).text
        print("Fetched Text is : ", text_element)
        if text_element == "Dashboard":
            return True
        else:
            return False
        
my_object = DemoText(Data().url)
print(my_object.validate_dashboard_text())

        
