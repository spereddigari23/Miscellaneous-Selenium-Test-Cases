from selenium import webdriver
from selenium.webdriver.common.by import By

#Have specified driver installed to the current path or have the path specified.
#Testing the google login page

driver = webdriver.Chrome()
driver.get("https://google.com")
assert driver.find_element(By.XPATH,"//*[@id='gb']/div/div[2]/a")
driver.find_element(By.XPATH,"//*[@id='gb']/div/div[2]/a").click()
assert driver.find_element(By.XPATH,"//*[@id='identifierId']")
driver.find_element(By.XPATH,"//*[@id='identifierId']").send_keys("emailid@gmail.com")
assert driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button")
driver.find_element(By.XPATH,"//*[@id='identifierNext']/div/button").click()
assert driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/inputf")
driver.find_element(By.XPATH,"//*[@id='password']/div[1]/div/div[1]/input").send_keys("gmailpassword")
assert driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button")
driver.find_element(By.XPATH,"//*[@id='passwordNext']/div/button").click()
# check if error message pops up
# if so then invalid username/password
assert not driver.find_element(By.XPATH,"//*[@id='view_container']/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[2]/div[2]/span")