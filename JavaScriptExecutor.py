#JS DOM can access any elemnents on webpage just like selinium
#seleinium has a method to execute java script code in it
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

driver.find_element_by_name("name").send_keys("spacex")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value")) # get attribute("value") bring text present in box
print(driver.execute_script("return document.getElementsByName('name') [0].value")) # this the DOM module in java script
# make sure to write return statement
shop_button = driver.find_element_by_xpath("//a[text()='Shop']") # lets say if click button is not accessble
driver.execute_script("arguments[0].click();",shop_button)
# selenium doesnt know how to scroll down but java script knows how to do
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);") # (0, 500) is vertical and (500,0) is horizontal
#above document.body.scrollHieght is to scroll height