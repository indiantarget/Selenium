from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

#The web browser to open (IE, Firefox, Chrome)
chromedriver = "/usr/lib/chromium-browser/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)

# Go To paytm Website
driver.get("https://paytm.com")

# Click on Login/Signup 
driver.find_element_by_xpath("/html/body/div[3]/div[1]/div/div[2]/div/div[3]/div[3]/div/span/a[1]").click()

# Login Mobile Number
login = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/form/div/md-content/md-input-container[1]/input")
login.send_keys("User Mobile number")

# Login password
password = driver.find_element_by_xpath("/html/body/div[1]/div/div[3]/div[2]/form/div/md-content/md-input-container[2]/input")
password.send_keys("User Password")

# Enter mobile number
mob_number = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/ul/li[1]/md-input-container/input")
mob_number.send_keys("Recharge number")

# Enter amount
amount = driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div[1]/ul/li[4]/md-input-container/input")
amount.send_keys("Amount")

# Proceed to Recharge
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div[1]/div[2]/div/div/div[2]/button").click()
time.sleep(3)

# Enter promo code
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/a").click()
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/md-input-container/input").send_keys("Voucher Code")
# driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[1]/div/md-input-container/div/a").click()

# Proceed To pay
driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div[1]/div[2]/div/ul/li[3]/button").click()
time.sleep(5)

