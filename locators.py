from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/angularpractice/")
print(driver.current_url)
print(driver.title)

driver.find_element_by_name("name").send_keys("pramod")
driver.find_element_by_name("email").send_keys("namesh@gmail.com")
driver.find_element_by_id("exampleInputPassword1").send_keys("vignesh")
driver.find_element_by_id("exampleCheck1").click()
driver.find_element_by_xpath("//input[@id='inlineRadio1']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
#print(driver.find_element_by_class_name("alert-success").text)

#for css tag name is optional
# customized css sytax
#tagname[attribute='value'] here tag name is optional

#customized xpath syntax
#//tagname[@attribute='value']
#//tagname[contains@attribute='value'] if u wnat to few line
#//*[contains@attribute='value'] #u can put * instead of tag name
#//*[text()='sometext']

#print(driver.find_element_by_css_selector("[class*='alert-success']").text)
message = (driver.find_element_by_xpath("//*[contains(@class,'alert-success')]")).text
assert "successdfdsac" in message # this is to check message. this is to check substring
#assert "success"==message this is to check entire string

#select calss can only be used when the tag name says select
"""dropdown =Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Male")
dropdown.select_by_index(1)
# dropdown.select_by_value() apply this if there is any value
driver.close()
"""

