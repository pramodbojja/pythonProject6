import time

from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
driver.implicitly_wait(3)
action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
child_link =driver.find_element_by_link_text("Top")
action.move_to_element(child_link).click().perform() #.perform is must
child_link2 = driver.find_element_by_xpath("//a[text()='Reload']")
action.move_to_element(child_link2).click().perform()

assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()

