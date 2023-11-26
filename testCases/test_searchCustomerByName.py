import time
import pytest
from pageObjects.LoginPage import LoginPage
from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_SearchCustomerByName_005:
    baseURL = Readconfig.get_application_url()
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("************* SearchCustomerByName_005 **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("************* Login succesful **********")

        self.logger.info("******* Starting Search Customer By Name **********")

        self.addcust = AddCustomer(self.driver)
        self.addcust.clickOnCustomersMenu()
        self.addcust.clickOnCustomersMenuItems()

        self.logger.info("************* searching customer by Name **********")
        searchcust = SearchCustomer(self.driver)
        searchcust.setFirstName("John")
        searchcust.setLastName("Smith")
        searchcust.clickSearch()
        time.sleep(5)
        status = searchcust.searchCustomerByName("John Smith")
        self.driver.close()
        assert True == status
        self.logger.info("***************  TC_SearchCustomerByName_005 Finished  *********** ")