import time
import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import Readconfig
from utilities.customLogger import LogGen
from utilities import XLUtils


class Test_002_DDT_Login:
    baseurl = Readconfig.get_application_url()
    path = ".//TestData/loginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("********** verifying login test ************")
        self.driver = setup
        self.driver.get(self.baseurl)

        self.lp = LoginPage(self.driver)

        self.rows = XLUtils.getRowCount(self.path, 'Sheet1')
        print("Numbers Of Row in Sheet1 in a Excel:", self.rows)

        lst_status = []

        for r in range(2, self.rows+1):
            self.user = XLUtils.readData(self.path, 'Sheet1', r, 1)
            self.password = XLUtils.readData(self.path, 'Sheet1', r, 2)
            self.exp = XLUtils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"
            if act_title == exp_title:
                if self.exp == "pass":
                    self.logger.info("*** Passed ***")
                    self.lp.clickLogout()
                    lst_status.append("pass")
                elif self.exp == "fail":
                    self.logger.info("*** Failed ***")
                    self.lp.clickLogout()
                    lst_status.append("fail")
            elif act_title != exp_title:
                if self.exp == 'pass':
                    self.logger.info("*** Failed ***")
                    lst_status.append("fail")
                elif self.exp == "fail":
                    self.logger.info("*** Passed ***")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("**** Login DDT test passed ***")
            self.driver.close()
            assert True
        else:
            self.logger.info("*** Login DDT test failed ***")
            self.driver.close()
            assert False

        self.logger.info("***** End of Login DDT Test *****")
        self.logger.info(" Test Complete")




