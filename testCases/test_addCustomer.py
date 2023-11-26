import time

import pytest
from selenium.webdriver.common.by import By

from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
import string
import random



class Test_003_AddCustomer:
    baseURL = Readconfig.get_application_url()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self, setup):
        self.logger.info("*** Test_003_AddCustomer ***")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        self.logger.info("*** Login Successfully")
        self.logger.info("*** Starting Add Customer Test ***")

        self.addcust = AddCustomer(self.driver)
        time.sleep(1)
        self.addcust.clickOnCustomersMenu()
        time.sleep(1)
        self.addcust.clickOnCustomersMenuItems()

        self.addcust.clickOnAddnew()

        self.logger.info("*** Providing Customer Info ***")

        self.email = random_generator() + "@gmail.com"
        time.sleep(1)
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        time.sleep(3)
        self.addcust.setCustomerRoles("Vendors")
        time.sleep(1)
        self.addcust.setManagerOfVendor("Vendor 2")
        self.addcust.setGender("Male")
        self.addcust.setFirstName("Umesh")
        self.addcust.setLastName("Tester")
        time.sleep(1)
        self.addcust.setDob("04/20/1996")
        self.addcust.setCompanyName("busyQA")
        self.addcust.setAdminContent("This is For Testing .. .. ..")
        time.sleep(1)
        self.addcust.clickOnSave()

        self.logger.info("*** Saving Customer Info ***")
        self.logger.info("*** Add Customer Validation Started ***")
        self.msg = self.driver.find_element(By.TAG_NAME, "body").text
        print(self.msg)

        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("*** Add Customer Test Passed ***")

        else:
            self.driver.save_screenshot(".\\Screenshots\\test_addCustomer_scr.png")
            self.logger.error("*** Add Customer Test Failed ***")
            assert True == False

        self.driver.close()
        self.logger.info("*** Ending Add Customer Test ***")

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))



