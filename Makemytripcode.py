import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")


driver.find_element_by_id("fromCity").click()

driver.find_element_by_xpath("//input[@placeholder='From']").send_keys("Del")

time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")

for city in cities:
    if city.text == "Delhi, India":
        city.click()
        break

driver.find_element_by_css_selector("input[placeholder='To']").send_keys("Kol")
time.sleep(2)
fromcity = driver.find_elements_by_css_selector("p[class*='blackText']")

for cit in fromcity:
    if cit.text == "Kolhapur, India":
        cit.click()
        break