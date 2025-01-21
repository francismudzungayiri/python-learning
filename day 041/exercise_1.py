from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By




def open_browser():
    
    #Chrome options made my broswer window remain open since
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('detach', True)
    
    chrome_driver_path = '/Users/mbuluundi/Documents/Developments/chromedriver'
    chrome_service = Service(executable_path= chrome_driver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

    driver.get('https://www.python.org/')
    
    return driver



chromeDriver = open_browser()

#getting all events
event_name = chromeDriver.find_elements( By.CSS_SELECTOR,'.event-widget .menu li a')
all_events = [ev.text for ev in event_name]
print(all_events)


#getting all the dates
event_date = chromeDriver.find_elements(By.CSS_SELECTOR, '.event-widget .menu li time')
all_dates = [d.text for d in event_date]
print(all_dates)

python_events = {}

for n in range(len(all_dates)):
    python_events[n] = {
        'time': all_dates[n],
        'name': all_events[n]
    }
    
print(python_events)



chromeDriver.quit()
    