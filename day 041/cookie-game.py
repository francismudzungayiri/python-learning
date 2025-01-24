from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True) 

    webdriver_path = '/Users/mbuluundi/Documents/Developments/chromedriver'
    chrome_servicce = Service(executable_path= webdriver_path)

    driver = webdriver.Chrome(service= chrome_servicce, options= options)
    driver.get('https://orteil.dashnet.org/cookieclicker/')
    
    return driver




play = open_browser()
cookie = play.find_element(By.ID, 'bigCookie')
cookie.click()



