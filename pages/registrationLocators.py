import time

import pytest
from selenium.webdriver.common.by import By

# Registration Page Locators
class RegistrationLocators:
    def __init__(self, driver):
        self.driver = driver

    #locators
    reg_button = "//a[text()='Register']"
    gender1 = "gender-male"
    first_name = "FirstName"
    last_name = "LastName"
    email = "Email"
    password = "Password"
    conf_pass = "ConfirmPassword"
    register = "register-button"
    continue_button = "//input[@value='Continue']"
    logout = "Log out"

    def first_register(self):
        self.driver.find_element(By.XPATH,self.reg_button).click()
    def gender(self):
        self.driver.find_element(By.ID,self.gender1).click()
    def fname(self,fname):
        self.driver.find_element(By.ID,self.first_name).send_keys(fname)
    def lname(self,lname):
        self.driver.find_element(By.ID,self.last_name).send_keys(lname)
    def emails(self,emails):
        self.driver.find_element(By.ID,self.email).send_keys(emails)
    def passwords(self,passwords):
        self.driver.find_element(By.ID,self.password).send_keys(passwords)
    def conf_passw(self,conf_passw):
        self.driver.find_element(By.ID, self.conf_pass).send_keys(conf_passw)
    def register1(self):
        self.driver.find_element(By.ID,self.register).click()
    def continue_button1(self):
        self.driver.find_element(By.XPATH,self.continue_button).click()
    def logout1(self):
        self.driver.find_element(By.LINK_TEXT,self.logout).click()


    def registration(self,fname="",lname="",emails="",passwords="",conf_passw="",):
        time.sleep(2)
        self.first_register()
        self.gender()
        self.fname(fname)
        self.lname(lname)
        self.emails(emails)
        self.passwords(passwords)
        self.conf_passw(conf_passw)
        self.register1()
        self.continue_button1()
        self.logout1()

