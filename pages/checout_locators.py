from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import datetime
import os
import time

class CheckOutLocators:
    def __init__(self, driver):
        self.driver = driver

    country = "//select[@name='BillingNewAddress.CountryId']"
    city = "BillingNewAddress_City"
    add_1 = "//input[@name='BillingNewAddress.Address1']"
    add_2 = "//input[@name='BillingNewAddress.Address2']"
    zip_code = "//input[@name='BillingNewAddress.ZipPostalCode']"
    phone = "//input[@name='BillingNewAddress.PhoneNumber']"
    billing_address = "//div[@id='billing-buttons-container']/input"
    shipping_address = "//div[@id='shipping-buttons-container']/input"
    shipping_method = "//div[@id='shipping-method-buttons-container']/input"
    payment_method = "//div[@id='payment-method-buttons-container']/input"
    payment_info = "//div[@id='payment-info-buttons-container']/input"
    confirm_order = "//div[@id='confirm-order-buttons-container']/input"


    def enter_country(self,countryname):
        country1 = self.driver.find_element(By.XPATH,self.country)
        sel = Select(country1)
        sel.select_by_visible_text(countryname)

    def enter_city(self,enter_city):
        self.driver.find_element(By.ID,self.city).send_keys(enter_city)

    def address1(self,address1):
        self.driver.find_element(By.XPATH,self.add_1).send_keys(address1)

    def address2(self,address2):
        self.driver.find_element(By.XPATH,self.add_1).send_keys(address2)

    def zip(self,zip):
        self.driver.find_element(By.XPATH,self.zip_code).send_keys(zip)

    def phoneno(self,phoneno):
        self.driver.find_element(By.XPATH,self.phone).send_keys(phoneno)

    def billing_addresss(self):
        self.driver.find_element(By.XPATH,self.billing_address).click()

    def shipping_addresss(self):
        self.driver.find_element(By.XPATH,self.shipping_address).click()

    def shipping_methods(self):
        self.driver.find_element(By.XPATH,self.shipping_method).click()

    def payment_methods(self):
        self.driver.find_element(By.XPATH,self.payment_method).click()

    def payment_infos(self):
        self.driver.find_element(By.XPATH,self.payment_info).click()

    def confirm_orders(self):
        self.driver.find_element(By.XPATH,self.confirm_order).click()


    def check_out(self, countryname, enter_city, address1, address2, zip, phoneno):
        self.enter_country(countryname)
        self.enter_city(enter_city)
        self.address1(address1)
        self.address2(address2)
        self.zip(zip)
        self.phoneno(phoneno)
        self.billing_addresss()
        self.shipping_addresss()
        self.shipping_methods()
        self.payment_methods()
        self.payment_infos()
        self.confirm_orders()
        time.sleep(5)
        timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        screenshot_name = os.path.join("D:\Work Data\Python Automation\Code file\DemoWebShop-main\screenshots_{timestamp}.png")
        self.driver.save_screenshot(screenshot_name)
        print(f"Screenshot saved as {screenshot_name}")

