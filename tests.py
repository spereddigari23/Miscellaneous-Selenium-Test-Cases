from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver=webdriver.Chrome()
def test_login_page():
    driver.get("https://saucedemo.com")
    assert driver.find_element(By.CSS_SELECTOR,"#user-name")
    driver.find_element(By.CSS_SELECTOR,"#user-name").send_keys("standard_user")
    assert driver.find_element(By.CSS_SELECTOR,"#password")
    driver.find_element(By.CSS_SELECTOR,"#password").send_keys("secret_sauce")
    assert driver.find_element(By.CSS_SELECTOR,".btn_action")
    driver.find_element(By.CSS_SELECTOR,".btn_action").click()
    assert driver.current_url != "https://saucedemo.com"
    assert driver.find_element(By.CSS_SELECTOR,".shopping_cart_link")
    
def test_order_of_items():
    str_=".product_sort_container"
    assert driver.find_element(By.CSS_SELECTOR,str_)
    x=Select(driver.find_element(By.CSS_SELECTOR,str_))
    x.select_by_value("za")
    assert driver.find_element(By.CLASS_NAME,"inventory_item_label")
    if "Test.allTheThings() T-Shirt" != driver.find_element(By.CLASS_NAME,"inventory_item_label"):
        print("Error, sort from Z-A is invalid")
    x=Select(driver.find_element(By.CSS_SELECTOR,str_))
    x.select_by_value("az")  
    if "Sauce Labs Backpack" != driver.find_element(By.CLASS_NAME,"inventory_item_label"):
        print("Error, sort from A-Z is invalid")
    x=Select(driver.find_element(By.CSS_SELECTOR,str_))
    x.select_by_value("lohi")
    if "Sauce Labs Onesie" != driver.find_element(By.CLASS_NAME,"inventory_item_label"):
        print("Error, Low to High sort is invalid")
    x=Select(driver.find_element(By.CSS_SELECTOR,str_))
    x.select_by_value("hilo")
    if "Sauce Labs Fleece Jacket" != driver.find_element(By.CLASS_NAME,"inventory_item_label"):
        print("Error, High to Low sort is invalid")
        
test_login_page()
test_order_of_items()

def test_valid_checkout():
    assert driver.find_element(By.ID,"#inventory_container")
    assert driver.find_element(By.CLASS_NAME,"#add-to-cart-sauce-labs-backpack")
    driver.find_element(By.CLASS_NAME, "#add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.CLASS_NAME,"#shopping_cart_container")
    driver.find_element(By.CLASS_NAME,"#shopping_cart_container").click()
    assert driver.find_element(By.CLASS_NAME,"#checkout")
    driver.find_element(By.CLASS_NAME,"#checkout").click()
    assert driver.find_element(By.CLASS_NAME,"#first-name")
    driver.find_element(By.CLASS_NAME,"#first-name").send_keys("FirstName")
    driver.find_element(By.CLASS_NAME,"#last-name").send_keys("LastName")
    driver.find_element(By.CLASS_NAME,"#postal-code").send_keys("00000")
    driver.find_element(By.CLASS_NAME,"#continue").click()
    driver.find_element(By.CLASS_NAME,"#finish").click()
    if driver.find_element_by_link_text("THANK YOU FOR YOUR ORDER", "h2"):
        print("Successful Order")
test_valid_checkout()

def test_invalid_checkout():
    assert driver.find_element(By.ID,"#inventory_container")
    assert driver.find_element(By.CLASS_NAME,"#shopping_cart_container")
    driver.find_element(By.CLASS_NAME,"#shopping_cart_container").click()
    assert driver.find_element(By.CLASS_NAME,"#checkout")
    driver.find_element(By.CLASS_NAME,"#checkout").click()
    assert driver.find_element(By.CLASS_NAME,"#first-name")
    driver.find_element(By.CLASS_NAME,"#first-name").send_keys("FirstName")
    driver.find_element(By.CLASS_NAME,"#last-name").send_keys("LastName")
    driver.find_element(By.CLASS_NAME,"#postal-code").send_keys("00000")
    driver.find_element(By.CLASS_NAME,"#continue").click()
    driver.find_element(By.CLASS_NAME,"#finish").click()
    if driver.find_element_by_link_text("THANK YOU FOR YOUR ORDER", "h2"):
        print("Error, no items in cart: invalid order")
        
def test_invalid_name(fname,lname,zip):
    assert driver.find_element(By.ID,"#inventory_container")
    assert driver.find_element(By.CLASS_NAME,"#add-to-cart-sauce-labs-backpack")
    driver.find_element(By.CLASS_NAME, "#add-to-cart-sauce-labs-backpack").click()
    assert driver.find_element(By.CLASS_NAME,"#shopping_cart_container")
    driver.find_element(By.CLASS_NAME,"#shopping_cart_container").click()
    assert driver.find_element(By.CLASS_NAME,"#checkout")
    driver.find_element(By.CLASS_NAME,"#checkout").click()
    assert driver.find_element(By.CLASS_NAME,"#first-name")
    if fname=="":
        print("Error: Invalid name argument")
        driver.quit()
    driver.find_element(By.CLASS_NAME,"#first-name").send_keys(fname)
    driver.find_element(By.CLASS_NAME,"#last-name").send_keys(lname)
    driver.find_element(By.CLASS_NAME,"#postal-code").send_keys(zip)
    driver.find_element(By.CLASS_NAME,"#continue").click()
    driver.find_element(By.CLASS_NAME,"#finish").click()
    if driver.find_element_by_link_text("THANK YOU FOR YOUR ORDER", "h2"):
        print("Successful Order")