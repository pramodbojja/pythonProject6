import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://the-internet.herokuapp.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)

driver.find_element_by_link_text("Frames").click()
driver.find_element_by_link_text("Nested Frames").click()
driver.back()
driver.find_element_by_link_text("iFrame").click()
#devs inject code into frames that wont be recognize by selenium, tags are iframe, frame,frameset
# to handle code that is in frames you must switch to frames
frame_switch = driver.switch_to.frame("mce_0_ifr")
#above frame switch handle frame id, frame name,  index value
driver.find_element_by_css_selector("body[id='tinymce']").clear()
driver.find_element_by_css_selector("body[id='tinymce']").send_keys("I am a disco dancer")
# we are in frames now we need to switch back
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text )
