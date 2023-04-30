from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/login")
time.sleep(5)
email = driver.find_element_by_id("username")
email.send_keys("your_email_address")
time.sleep(5)
password = driver.find_element_by_id("password")
password.send_keys("your_password")
time.sleep(5)
password.send_keys(Keys.RETURN)
time.sleep(5)
