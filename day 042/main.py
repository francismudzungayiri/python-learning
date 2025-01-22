from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from dotenv import load_dotenv
import os

load_dotenv()
EMAIL = os.getenv('LINKEDIN_USERNAME')
PASSWORD = os.getenv('LINKEDIN_PASSWORD')

def open_browser():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('detach', True) 

    webdriver_path = '/Users/mbuluundi/Documents/Developments/chromedriver'
    chrome_servicce = Service(executable_path= webdriver_path)

    driver = webdriver.Chrome(service= chrome_servicce, options= options)
    driver.get('https://www.linkedin.com/')
    
    return driver


    
#open the linkedin website
sign_in_action = open_browser()

#sign in page automatic typing 
sign_in_email = sign_in_action.find_element(By.LINK_TEXT,'Sign in with email')
sign_in_email.click()

log_input = sign_in_action.find_element(By.ID, 'username')
log_input.send_keys(EMAIL)
password_input = sign_in_action.find_element(By.ID, 'password')
password_input.send_keys(PASSWORD)

#unchecking the checkbox
#checkbox = sign_in_action.find_element(By.ID,'rememberMeOptIn-checkbox')
#sign_in_action.execute_script("arguments[0].click();", checkbox)


#sign in button 
sign_in_button = sign_in_action.find_element(By.CLASS_NAME, 'btn__primary--large')
sign_in_button.click()

#jobs clicks
job_click = sign_in_action.find_element(By.CLASS_NAME, 'BdrTEAnueFGDkvgGoEtKMtaxyzMApdPnLs')
job_click.click()
