"""
Headless Browsing - Firefox - Fetch Title and URL
"""
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

class HeadlessFirefox:

    def __init__(self, web_url):
        self.url = web_url

        # code for headless browsing using firefox
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--headless')

        # Firefox driver
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=firefox_options) 

    def start_automation(self):
        self.driver.get(self.url)
        sleep(3)
        print("PROCESS 1 : Headless firefox browser is working")
        return True
    
    def shutdown(self):
        print("PROCESS 2 : Automation Closed")
        self.driver.close()

    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return False
    
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False
        
# create an object from class HeadlessFirefox
url = "https://www.guvi.in/courses/"
firefox_automation = HeadlessFirefox(url)
firefox_automation.start_automation()
print(firefox_automation.fetch_title())
print(firefox_automation.fetch_url())
firefox_automation.shutdown()