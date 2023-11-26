import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen


class Test_001_Login:
    baseurl = Readconfig.get_application_url()
    print(baseurl)
    username = Readconfig.getUseremail()
    password = Readconfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("********** Test001_Login ************")
        self.logger.info("********** verify home page title ************")
        self.driver = setup
        self.driver.get(self.baseurl)
        act_title = self.driver.title
        print("Homepage Title Is -: " + act_title)

        if act_title == "Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("********** Homepage title is pass ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_homepagetitle.png")
            self.driver.close()
            self.logger.error("********** Homepage title is fail ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self, setup):
        self.logger.info("********** verifying login test ************")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()

        act_title = self.driver.title
        print("Dashboard Title Is -: " + act_title)
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("********** Login Test is pass ************")
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_Dashboardtitle.png")
            self.driver.close()
            self.logger.error("********** Login Test is failed ************")
            assert False


