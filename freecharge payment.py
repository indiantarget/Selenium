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

# Go to Website
driver.get('https://www.freecharge.in/mobile/recharge/prepaid')

# Recharge Details
mobile_number = driver.find_element_by_id("serviceNumber")
mobile_number.send_keys("User Mobile Number")
amount = driver.find_element_by_id("amount")
amount.send_keys("Amount")
driver.find_element_by_id("rechargeBtn").click()

# Login Details
email = driver.find_element_by_id("userMail")
email.send_keys("User Mail Address")
password = driver.find_element_by_id("password")
password.send_keys("User Password")
driver.find_element_by_css_selector(".loginBtn.btn").click()

# Payment Option NetBanking
driver.find_element_by_xpath("/html/body/div[2]/header/nav/ul/li[3]/a").click()
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[5]/div/div/select/option[2]").click()

# Voucher Details
# voucher = find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[8]/div/input[1]").click()
# voucher.send_keys("voucher_code")
# driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/div/form/div[8]/div/input[2]").click() 

# Proceed Payment
driver.find_element_by_css_selector(".payment-btn.btn").click()





