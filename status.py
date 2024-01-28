import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from auth import AuthBackend
from bs4 import BeautifulSoup

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=1920x1080") 

# Specify the path to chromedriver
chrome_driver_path = "/usr/bin/chromedriver"

try:
    #AUTH
    # Use the service argument to set the path
    chrome_service = Service(chrome_driver_path)

    # # Get the current script's directory
    script_directory = os.path.dirname(os.path.realpath(__file__))

    # Construct the path to cookies.txt in the script's directory
    cookies_file_path = os.path.join(script_directory, 'cookies.txt')

    # Initialize AuthBackend with cookies file path
    auth_backend = AuthBackend(cookies=cookies_file_path)

    # Authenticate using the provided WebDriver
    driver = auth_backend.authenticate_agent(webdriver.Chrome(service=chrome_service, options=chrome_options))

    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    # Now, you can use the authenticated WebDriver to perform actions on the TikTok website
    # For example, opening the TikTok website again:
    driver.get("https://www.tiktok.com/@divoke_prase")

    time.sleep(15)

    # Take a screenshot after waiting
    screenshot_path = os.path.join(script_directory, 'status.png')
    driver.save_screenshot(screenshot_path)
    print(f"Screenshot saved to: {screenshot_path}")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the WebDriver to release resources
    driver.quit()


#NOT WORKING CAUSE TIKTOK CAPTCHA!
