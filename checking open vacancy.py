import io
import random
import datetime
from time import sleep
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


logs_file = './logs/logs_existing_QA_Automation_position.log'
f = open(logs_file, "w")
f.write(f"start, {datetime.datetime.now()}\n")
f.close()
f = open(logs_file, "a")


def browser():
    try:
        chrome_options = webdriver.ChromeOptions()
        driver_service = Service(executable_path="mac/chromedriver_mac64/chromedriver")
        driver_service = Service(executable_path=ChromeDriverManager().install())
        chrome = webdriver.Chrome(service=driver_service)
        chrome.maximize_window()
        chrome_options.set_capability('unhandledPromptBehavior', 'accept')
        return chrome
    except Exception as e:
        print(e)


def open_site(chrome):
    try:
        chrome.switch_to.window(chrome.window_handles[0])
        chrome.get('https://www.optimove.com/careers')
        chrome.implicitly_wait(10)
        f.write(f"site is opened, {datetime.datetime.now()}\n")
        print('site is opened')
        chrome.implicitly_wait(10)
        sleep(6)
        chrome.execute_script('''document.querySelector('div.container > div > div > div.select-dropdown.select-dropdown--job-locations').scrollIntoView()''')
        sleep(4)
        print('scrolled down')
        chrome.execute_script("document.querySelector('div.container > div > div > div.select-dropdown.select-dropdown--job-locations > div > div > div > div.selectric').click()")
        print('dropdown opened')
        sleep(2)
        chrome.execute_script("document.querySelector('div.container > div > div > div.select-dropdown.select-dropdown--job-locations > div > div > div > div.selectric-items > div > ul > li:nth-child(9)').click()")
        sleep(3)
        print('UKR selected')
        f.write(f"filter selected, {datetime.datetime.now()}\n")
        chrome.save_screenshot('./screenshots/App_positions_screenshot.png')
        sleep(2)
    except Exception as e:
        chrome.save_screenshot('./screenshots/error.png')
        f.write(f"Failed at process {e}, {datetime.datetime.now()}\n")
        print(e)

def find_QA_Automation_Engineer(chrome):
    try:
        sleep(2)
        WebDriverWait(chrome, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='QA Automation Engineer']")))
        print('Vacation is present')
    except:
        print('Vacation is missing')


def main():
    chrome = browser()
    open_site(chrome)
    find_QA_Automation_Engineer(chrome)


if __name__ == '__main__':
    main()