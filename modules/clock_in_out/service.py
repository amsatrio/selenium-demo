import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import driver_config
from config.environment_config import get_env
from modules.logger.service import loge, logi


def _clock_in_out(message: str):
    
    logi(f"clock_in_out({message}) start")
    env = get_env()
    
    # initialize
    driver = driver_config.get_driver(driver_config.BrowserType.CHROME, True)
    driver.get(env.url)
    
    wait = WebDriverWait(driver, env.wait_time * 3)

    # login process
    username_input_element = wait.until(EC.visibility_of_element_located((By.ID, "txtusername")))
    password_input_element = wait.until(EC.visibility_of_element_located((By.ID, "txtpassword")))
    login_button_element = wait.until(EC.visibility_of_element_located((By.ID, "btnsubmit")))

    username_input_element.send_keys(env.username)
    password_input_element.send_keys(env.password)

    login_button_element.click()

    # clock in/out
    comment_input_element = wait.until(EC.visibility_of_element_located((By.ID, "txtRaComment")))
    submit_button_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//i[@data-bind=\"click:function(data, event) { ManualSwipe.PerformAction('SWAP'); }\"]")))
    
    comment_input_element.send_keys(message)
    
    submit_button_element.click()
    
    time.sleep(env.wait_time)
    
    logi(f"clock_in_out({message}) finish")
    
    driver.quit()

def clock_in():
    _clock_in_out("clock in")
def clock_out():
    _clock_in_out("clock out")