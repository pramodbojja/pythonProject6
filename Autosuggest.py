import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
print(driver.current_url)
print(driver.title)

driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(1)
countries = driver.find_elements_by_css_selector("li[class='ui-menu-item'] a")
print(len(countries))
for country in countries:
    if country.text =="India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
#.text doesnt bring any text because the there is no page refresh
#instead we use attribute
print(driver.find_element_by_id("autosuggest").get_attribute("value"))
#Value will store whatever info got selected
assert driver.find_element_by_id("autosuggest").get_attribute("value") == 'India'