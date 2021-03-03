import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(1)
valid_text = "reshme"
driver.find_element_by_css_selector("input[placeholder='Enter Your Name']").send_keys("reshme")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
alert_text=alert.text
assert valid_text in alert_text
alert.accept() #This is to press ok

Validated_text = "padma"
driver.find_element_by_css_selector("input[placeholder='Enter Your Name']").send_keys("padma")
driver.find_element_by_id("confirmbtn").click()
alerts=driver.switch_to.alert
alert.dismiss()