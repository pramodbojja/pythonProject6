from selenium import webdriver

webdriver

#driver = webdriver.Firefox(executable_path ="C:\\geckodriver.exe")
#driver = webdriver.Ie(executable_path ="C:\\IEDriverServer.exe")

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
#driver.get("https://google.com")
#print(driver.title)
#print(driver.current_url)
#driver.close()
driver.get("https://www.binance.com/en/markets")
driver.maximize_window()
driver.back()
#driver.refresh()
#driver.close()
