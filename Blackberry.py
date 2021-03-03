from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument("headless")
from selenium.webdriver import ActionChains
driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe",options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
action = ActionChains(driver)
driver.find_element_by_name("name").send_keys("spacex")
print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value")) # get attribute("value") bring text present in box
print(driver.execute_script("return document.getElementsByName('name') [0].value")) # this the DOM module in java script
# make sure to write return statement
shop_button = driver.find_element_by_xpath("//a[@href='/angularpractice/shop']").click() # lets say if click button is not accessble
    # driver.execute_script("arguments[0].click();",shop_button)
    #//div[@class='card h-100']

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name =product.find_element_by_xpath("div/h4/a").text #// not required in the middel
    if product_name == "Blackberry":
        #now we need to add products to cart
        product.find_element_by_xpath("div[2]/button").click()
driver.find_element_by_css_selector("a[class*='btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("Ind")
wait = WebDriverWait(driver,7)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India"))) # explicit wait 2 brackets(())
driver.find_element_by_link_text("India").click()
driver.find_element_by_css_selector("label[for='checkbox2']").click()
driver.find_element_by_css_selector("input[type='submit']").click()
success_text =driver.find_element_by_css_selector("div[class*='alert-success']").text
assert "Success! Thank you!" in success_text
#driver.get_screenshot_as_file("screenshot.png") # add a screen short when there is a failure
driver.close()