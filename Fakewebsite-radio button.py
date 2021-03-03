import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://www.rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(1)

checkboxes = driver.find_elements_by_css_selector("input[type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value") =="option2":
        checkbox.click()
        assert checkbox.is_selected() #this will check if check box are selected or not

radiobutton=driver.find_elements_by_name("radioButton")
for button in radiobutton:
    if button.get_attribute("Value") =="radio3":
        button.click()
        break



time.sleep(3)
driver.close()