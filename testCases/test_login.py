import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    useremail=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    def test_homepageTitle(self,setup):

        self.logger.info("**************** Test_001_Login *************")
        self.logger.info("****************Verifying Home Page Title *************")

        self.driver= setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("**************** Home Page Title Test is Passed *************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("**************** Home Page Title Test is Failed *************")

            assert False

    def test_login(self,setup):
        self.logger.info("**************** Veryfying Login Test *************")

        self.driver=setup
        self.driver.get(self.baseURL)
        self.lp=LoginPage(self.driver)
        self.lp.setUserEmail(self.useremail)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("****************  Login Test is Passed *************")

        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("****************  Login Test is Failed *************")
            assert False


