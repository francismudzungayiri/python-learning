from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def open_broweser():
    
    #Chrome options made my broswer window remain open since
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    
    chrome_driver_path = '/Users/mbuluundi/Documents/Developments/chromedriver'
    chrome_service = Service(executable_path= chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get('https://www.amazon.com')
    
    return driver


open_broweser()
     