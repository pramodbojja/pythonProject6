import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://www.makemytrip.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

driver.execute_script('el = document.elementFromPoint(0, 10); el.click();')
time.sleep(5)
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del rio")
time.sleep(2)
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
print(len(cities))
for city in cities:
    print(city.text)
    if city.text == "Del Rio, United States":
        city.click()
        break