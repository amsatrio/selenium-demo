
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from enum import Enum
from model.webdriver import BrowserType
    
def _driver_firefox(headless: bool):
    if (headless == False):
        return webdriver.Firefox()
    firefox_options = FirefoxOptions()
    firefox_options.add_argument("--headless")
    firefox_options.add_argument("--width=1920")
    firefox_options.add_argument("--height=1080")
    return webdriver.Firefox(options=firefox_options)

def _driver_chrome(headless: bool):
    if (headless == False):
        return webdriver.Chrome()
    
    chrome_options = ChromeOptions()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

def get_driver(type: BrowserType, headless: bool):
    if(type == BrowserType.FIREFOX):
        return _driver_firefox(headless)
    if(type == BrowserType.CHROME):
        return _driver_chrome(headless)
    raise Exception(f"browser '{type}' doesn't supported")