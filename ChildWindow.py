import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

driver.find_element_by_xpath("//a[text()='Multiple Windows']").click()
driver.find_element_by_link_text("Click Here").click()
#below switching to another window
child_window = driver.window_handles[1] #this method is used for muliple tabs
#grab handles and switch
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
parent_window = driver.window_handles[0]
driver.switch_to.window(parent_window)
print(driver.find_element_by_tag_name("h3").text)
driver.quit()
