import pytest

from pages.buy_item_locators import BuyItemLocators
from pages.checout_locators import CheckOutLocators
from pages.login_locators import LoginLocators
from pages.registrationLocators import RegistrationLocators
from packageutilities.BaseClass import BaseClass

class TestCompleteFlow(BaseClass):

    def test_valid_reg(self):
        rg = RegistrationLocators(self.driver)
        rg.registration("Gaurav", "chaurasiya", "gcdemo@mail.com", "gaurav@123", "gaurav@123")

    def test_log_in(self):
        lg = LoginLocators(self.driver)
        lg.log_in("gcdemo@mail.com", "gaurav@123")

    def test_item_buy(self):
        bi = BuyItemLocators(self.driver)
        bi.buy_item("Build your own cheap computer")

    def test_checkout(self):
        co = CheckOutLocators(self.driver)
        co.check_out("India", "Indore","Test001", "Test002","452002","989898989")



