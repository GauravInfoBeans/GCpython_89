import time

from selenium.webdriver.common.by import By

class LoginLocators:
    def __init__(self, driver):
        self.driver = driver

    #locators
    login='Log in'
    email_id="Email"
    Passwords="Password"
    submit="//input[@value='Log in']"

    def logins(self):
        self.driver.find_element(By.LINK_TEXT,self.login).click()

    def emails(self,emails):
        self.driver.find_element(By.ID,self.email_id).send_keys(emails)

    def Passwrd(self,Passwrd):
        self.driver.find_element(By.ID,self.Passwords).send_keys(Passwrd)

    def submit1(self):
        self.driver.find_element(By.XPATH,self.submit).click()

    def log_in(self,emails="", Passwrd=""):
        time.sleep(2)
        self.logins()
        self.emails(emails)
        self.Passwrd(Passwrd)
        self.submit1()