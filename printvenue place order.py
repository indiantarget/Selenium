from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os


#The web browser to open (IE, Firefox, Chrome)
chromedriver = "/usr/lib/chromium-browser/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)


# Go to printvenue.com
driver.get('http://www.printvenue.com/customize/photo-mugs/ev-val-a22-cm-psd')
time.sleep(3)

# Click on Ok button
driver.find_element_by_id('safearea-ok-close').click()

# Select quantity
driver.find_element_by_xpath("/html/body/div[5]/form/div[1]/div[3]/div[3]/div[1]/div/select/option[3]").click()
time.sleep(3)

# Add To cart
driver.find_element_by_id('buy').click()
time.sleep(5)

# Click on Approve
driver.find_element_by_id("confirm-approval").click()
time.sleep(5)

# Click on Buy
driver.find_element_by_xpath("/html/body/div[13]/div/div/div/div/table/tfoot/tr/td/button").click()
time.sleep(5)

# Apply voucher
voucher = driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/form/div[2]/input[1]")
voucher.send_keys("FLT150")
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[1]/form/div[2]/input[2]").click()
time.sleep(2)

# Proceed to checkout
driver.find_element_by_xpath("/html/body/div[3]/div/div/div/div[1]/div/div/div[2]/div[2]/div[7]/a").click()

# Login Details
email = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/div[1]/fieldset/div[2]/input")
email.send_keys("rahul.mehta@printvenue.com")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/div[1]/fieldset/div[3]/input[1]").click()
password = driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/div[1]/fieldset/div[3]/div[2]/input")
password.send_keys("123456789")
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/div[1]/fieldset/div[4]/input").click()
time.sleep(10)

# Add address
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[1]/div[1]/div[1]/fieldset[2]/div/div/input").click()
time.sleep(5)

# Place Order
driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/form/div[2]/div/div[2]/div[2]/div[9]/div[2]/button").click()

