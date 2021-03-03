import time

from selenium import webdriver
from selenium.webdriver import ActionChains
action = ActionChains(driver)



chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") # --start-maximized this is to maximize browser
chrome_options.add_argument("--headless") # this is to make faster execution with less memory. this wont open browser
chrome_options.add_argument("--ignore-certificate-errors") # to clear certificate errors n execute


driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe",options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

shop_button = driver.find_element_by_xpath("//a[text()='Shop']").click()
driver.execute_script("args[0].click();",shop_button)
phones = driver.find_elements_by_css_selector("button[class*='btn btn-info']")
print(len(phones))
assert int(phones) == 4
for phone in phones:
    if phone.text == "Blackberry":


