from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
import schedule
import os
from dotenv import load_dotenv

load_dotenv()
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')
url = os.getenv('URL')
wait_time = 10

def get_driver(headless: bool):
    if (headless == False):
        return webdriver.Chrome()
    
    chrome_options = Options()
    chrome_options.add_argument("--headless=new") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage") 
    chrome_options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(options=chrome_options)

def clock_in_out(message: str):
    
    # initialize
    driver = get_driver(True)
    driver.get(url)

    # login process
    username_input_element = driver.find_element(By.ID, "txtusername")
    password_input_element = driver.find_element(By.ID, "txtpassword")
    login_button_element = driver.find_element(By.ID, "btnsubmit")

    username_input_element.send_keys(username)
    password_input_element.send_keys(password)

    login_button_element.click()

    # clock in/out
    wait = WebDriverWait(driver, wait_time * 3)
    submit_button_element = wait.until(
            EC.visibility_of_element_located(By.XPATH, "//i[@data-bind=\"click:function(data, event) { ManualSwipe.PerformAction('SWAP'); }\"]")  
            )
    comment_input_element = driver.find_element(By.ID, "txtRaComment")
    
    comment_input_element.send_keys(message)
    submit_button_element.click()

    time.sleep(wait_time)

    driver.quit()

def schedule_clock_in():
    clock_in_out("clock in")
def schedule_clock_out():
    clock_in_out("clock out")


if __name__ == "__main__":
    
    schedule.every().monday.at("09:25").do(schedule_clock_in)
    schedule.every().tuesday.at("07:58").do(schedule_clock_in)
    schedule.every().wednesday.at("07:57").do(schedule_clock_in)
    schedule.every().thursday.at("07:59").do(schedule_clock_in)
    schedule.every().friday.at("07:56").do(schedule_clock_in)

    schedule.every().monday.at("17:01").do(schedule_clock_out)
    schedule.every().tuesday.at("17:00").do(schedule_clock_out)
    schedule.every().wednesday.at("17:03").do(schedule_clock_out)
    schedule.every().thursday.at("17:02").do(schedule_clock_out)
    schedule.every().friday.at("17:02").do(schedule_clock_out)
    
    try:
        while True:
            schedule.run_pending()
            time.sleep(10)
    except KeyboardInterrupt:
        print("\nScheduler stopped by user.")
    except Exception as e:
        print(f"An error occurred: {e}")
