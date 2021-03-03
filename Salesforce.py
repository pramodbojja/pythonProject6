from selenium import webdriver

driver = webdriver.Chrome(executable_path = "C:\\chromedriver.exe")
driver.get("https://login.salesforce.com/?locale=ca")
print(driver.current_url)
print(driver.title)
#generate css from id - id is tagname#id
driver.find_element_by_css_selector("input#username").send_keys("pramod.nice@gmail.com")
#generate css from class = tagname.classname
driver.find_element_by_css_selector("input.password").send_keys("wndywydbw")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click() #link text only works if <a has a link
driver.find_element_by_xpath("//a[text()='Cancel']").click() #x path choosing text //tagname[text()='xxx], not dynmaic
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(1)").text)
#creating customized xpath - paraenttag/childtag
#creating customized css -parenttag space childtag
driver.find_element_by_xpath("//div[@id='signup']/a").click()
#select class provide methods to handle drop down
driver.back()
#below is customized css path
driver.set_page_load_timeout(30)
# what is absolute xpath - absolute xpath generate from the root of the begining tag
# what is relative xpath - it will directly targeting the locator
#assert method alwasys expect to be true
assert 2>3
