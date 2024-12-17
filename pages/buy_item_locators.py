import datetime
import os
import time

from selenium.webdriver.common.by import By

class BuyItemLocators:
    def __init__(self, driver):
        self.driver = driver

    computers="//ul[@class='list']//a[@href='/computers']"
    desktop= "//ul[@class='list']//a[@href='/desktops']"
    items_list = "//div[@class='product-grid']//h2/a"
    add_to_cart="//input[@value ='Add to cart']"
    add_to_cart2="//div[@class='add-to-cart']//input[2]"
    Shopping_Cart="Shopping cart"
    term_Condition="termsofservice"
    checkout="checkout"


    def computer(self):
        self.driver.find_element(By.XPATH,self.computers).click()

    def desktops(self):
        self.driver.find_element(By.XPATH,self.desktop).click()

    def select_item(self, iname):

        item_list = self.driver.find_elements(By.XPATH,self.items_list)
        for item in item_list:
            item_name = item.text
            if item_name == iname:
                self.driver.find_element(By.XPATH,self.add_to_cart).click()
                break

    def addto_cart2(self):
        self.driver.find_element(By.XPATH,self.add_to_cart2).click()

    def Shopping_Carts(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,self.Shopping_Cart).click()

    def term_Conditions(self):
        self.driver.find_element(By.ID,self.term_Condition).click()

    def checkouts(self):
        self.driver.find_element(By.ID,self.checkout).click()

    def buy_item(self, iname):
        self.computer()
        self.desktops()
        self.select_item(iname)
        self.addto_cart2()
        self.Shopping_Carts()
        self.term_Conditions()
        self.checkouts()
