from selenium import webdriver
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from time import sleep

class HeadlessEdge:

    def __init__(self, web_url):
        self.url = web_url

        # code for headless browser in Edge
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument('--headless')

        # Edge Driver
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()), options=edge_options)

    
    def start_automation(self):
        self.driver.get(self.url)
        sleep(3)
        print("PROCESS 1 - Edge Headless browser is working")
        return True
    
    def shutdown(self):
        print("PROCESS 2 - Automation Closed")
        self.driver.close()

    def fetch_url(self):
        if self.start_automation():
            return self.driver.current_url
        else:
            return True
    
    def fetch_title(self):
        if self.start_automation():
            return self.driver.title
        else:
            return False
        
# create the object from class Headless Edge
url = "https://www.guvi.in/courses/"
edge_automation = HeadlessEdge(url)
edge_automation.start_automation()
print(edge_automation.fetch_title())
print(edge_automation.fetch_url())
edge_automation.shutdown()

