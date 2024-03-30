from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time

# uni_roll = input("Enter the University Roll Number: ")

Firefox_options = Options()
Firefox_options.add_argument('--disable-blink-features=AutomationControlled') # error mili thi urllib3.exceptions.MaxRetryError: toh uske liye
Firefox_options.add_argument('--headless')  # Runs headless mode means you will not see the browser opening
Firefox_options.add_argument('--disable-gpu')  # Disables GPU hardware acceleration
Firefox_options.add_argument('--no-sandbox')  # Bypasses OS security model ( aise he lagaa diya kyunki dusre laptop pe kaam nahi kar rha tha)

browser = webdriver.Firefox(options = Firefox_options) # new firefox webdriver instance created successfully

def function():
    counter = 0 # counter for while loop
    while counter < 6:
        url = "https://erp.psit.ac.in/"
        browser.get(url) # receives url

        username_input = browser.find_element(By.NAME, 'username') # login button find using the name attribute
        password_input = browser.find_element(By.NAME, 'password') # password button find using the name attribute

        username_input.send_keys('2201640100114') #Value that needs to be inside the username field
        password_input.send_keys('845135688525') #value for password field

        login_button = browser.find_element(By.CLASS_NAME, 'btn-lg')# Locate and click the "Log in" button by Class Name attribute because only name attribute was not found
        login_button.click()

        time.sleep(3) # thodi der ruk jaane ke liye
        counter += 1


def run_every_15_minutes():
    while True:
        # Call your function
        function()

        # Pause the execution for 15 minutes
        time.sleep(16 * 60)  # 15 minutes * 60 seconds/minute = 900 seconds

browser.quit() #quits the instance

