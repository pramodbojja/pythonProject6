import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://www.yatra.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
time.sleep(1)
driver.execute_script('el = document.elementFromPoint(0, 10); el.click();')
driver.find_element_by_id("BE_flight_origin_city").click()
driver.find_element_by_xpath("//label[@for='BE_flight_arrival_city']//input").send_keys("Mum")
cities = driver.find_elements_by_xpath("//p[@class='ac_cityname']//div")

time.sleep(1)
print(len(cities))
for city in cities:
    print(city)
    if city.text =="Mumbai " or city.text=="BOM" or city.text=="Chhatrapati Shivaji International":
        city.click()
        break

time.sleep(1)
cities = driver.find_elements_by_xpath("//p[@class='ac_cityname']//div")
print(len(cities))
for city in cities:
    if city.text =="Bangalore  " or city.text=="BLR" or city.text=="Kempegowda International":
        city.click()
        break




