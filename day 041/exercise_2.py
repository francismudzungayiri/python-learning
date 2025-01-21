from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys




chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

chrome_driver_path = '/Users/mbuluundi/Documents/Developments/chromedriver'
chrome_service = Service(executable_path= chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

driver.get('https://en.wikipedia.org/wiki/Main_Page')

article_count = driver.find_elements(By.CSS_SELECTOR,'#articlecount ul li a')
articles = [article.text for article in article_count]
print(articles[1])


#clicks
article_count[1].click() 

#log_in = driver.find_element(By.LINK_TEXT,'log in')
#log_in.click()

#automatic typing
search = driver.find_element(By.CLASS_NAME, 'cdx-text-input__input')
search.send_keys('Python')
search.send_keys(Keys.ENTER)




#driver.quit()

