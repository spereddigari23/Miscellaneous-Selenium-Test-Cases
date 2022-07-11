from selenium import webdriver
from selenium.webdriver.common.by import By as b
from selenium.webdriver.support.select import Select as s

driver=webdriver.Chrome()
driver.get("https://youtube.com")
assert driver.find_element(b.CLASS_NAME,"#yt-simple-endpoint style-scope ytd-button-renderer")
driver.find_element(b.CLASS_NAME,"#yt-simple-endpoint style-scope ytd-button-renderer").click()
assert driver.find_element(b.CLASS_NAME,"#whsOnd zHQkBf")
driver.find_element(b.CLASS_NAME,"#whsOnd zHQkBf").send_keys("Gmail@gmail.com")
driver.find_element(b.CLASS_NAME,"#VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 qIypjc TrZEUc lw1w4b").click()
assert driver.find_element(b.CLASS_NAME,"#whsOnd zHQkBf")
driver.find_element(b.CLASS_NAME,"#whsOnd zHQkBf").send_keys("gmailpassword")
driver.find_element(b.XPATH,"#//*[@id='passwordNext']/div/button").click()
assert driver.find_element(b.CLASS_NAME,"#ytd-searchbox")
driver.find_element(b.CLASS_NAME,"#ytd-searchbox").send_keys("opkey")
driver.find_element(b.CLASS_NAME,"#style-scope ytd-searchbox").click()
assert driver.find_element(b.CLASS_NAME,"#cstyle-scope ytd-channel-name")
driver.find_element(b.CLASS_NAME,"#cstyle-scope ytd-channel-name").click()
driver.find_element(b.XPATH,"#//*[@id='tabsContent']/tp-yt-paper-tab[2]/div").click()
driver.find_element(b.XPATH,"#//*[@id='details']").click()
driver.find_element(b.XPATH,'#//*[@id="button"]').click()
