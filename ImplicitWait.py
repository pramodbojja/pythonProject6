#implicit wait
#explicit wait

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(1)
driver.implicitly_wait(5)
driver.find_element_by_css_selector("input[type='search']").send_keys("be")
count =len(driver.find_elements_by_xpath("//div[@class='product']"))
time.sleep(3)

addcart =driver.find_elements_by_xpath("//div[@class='product-action']/button")
print(len(addcart))
time.sleep(3)
veg_list= []
for items in addcart:
    veg_list.append(items.find_element_by_xpath("parent::div/parent::div/h4").text)
    items.click()
print(veg_list)

driver.find_element_by_css_selector("a[class*='cart-icon'] img").click()
wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//button[text()='PROCEED TO CHECKOUT']")))


driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(3)
veggies = driver.find_elements_by_tag_name("p.product-name")
veg_list2 = []
for veg in veggies:
    veg_list2.append(veg.text)
print(veg_list2)
assert veg_list == veg_list2
total_amount =driver.find_element_by_tag_name("span.totAmt").text
print(total_amount)
driver.find_element_by_css_selector("input[class*='promoCode']").send_keys("rahulshettyacademy")
driver.find_element_by_class_name("promoBtn").click()
time.sleep(3)
after_discount =driver.find_element_by_tag_name("span.discountAmt").text
time.sleep(3)

print(after_discount)
assert int(total_amount)== int(after_discount)
values = driver.find_elements_by_xpath("//tr/td[5]/p")
sum = 0
for value in values:
    sum = sum+ int(value.text)
print(sum)
assert int(total_amount)== sum
print(driver.find_element_by_tag_name("span.promoInfo").text)
driver.find_element_by_xpath("//button[text()='Place Order']").click()
countries= driver.find_elements_by_css_selector("select[style*='width: 200px;'] option")
print(len(countries))
for country in countries:
    if country.get_attribute("value")=="Canada":
        country.click()
        break
driver.find_element_by_class_name("chkAgree").click()
driver.find_element_by_xpath("//button[text()='Proceed']").click()