import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

action = ActionChains(driver)
mouse_click =driver.find_element_by_id("double-click")
action.double_click(mouse_click).perform()
alert = driver.switch_to.alert
print(alert.text)
assert alert.text == "You double clicked me!!!, You got to be kidding me"
alert.accept()

action.context_click(mouse_click).perform()