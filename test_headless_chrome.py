"""
Headless Browsing using Chrome - Fetch Title and URL
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class HeadlessChrome:

    def __init__(self, web_url):
        self.url = web_url

        # code for headless browsing in chrome
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')

        # chrome webdriver 
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # start_automation method, to launch the browser in headless mode
    def start_automation(self):
        self.driver.get(self.url)
        sleep(3)
        # printing in the console for confirmation
        print("PROCESS-1 : Google Chrome Browser is working")
        return True
    
    # shut down method, to properly close the browser in headless mode
    def shutdown(self):
        print("PROCESS-2 : Headless Automation Closed")
        self.driver.close()
    
    # fetch_url method, to fetch the current url of the website
    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return False
    
    # fetch_title method, to fetch the title of that website
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False
        
# create an object and call the methods
url = "https://www.guvi.in/courses/"
chrome_automation = HeadlessChrome(url)
chrome_automation.start_automation()
print(chrome_automation.fetch_url())
print(chrome_automation.fetch_title())
chrome_automation.shutdown()

