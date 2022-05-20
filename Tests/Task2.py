import time

from selenium import webdriver
from selenium.webdriver import Keys
from webdriver_manager.chrome import ChromeDriverManager


class Test_Task2:
    baseurl="https://www.linkedin.com/"
    userNameInput ="//*[starts-with(@class,'sign-in-form__form-input-container')]/div[1]/input[1]";
    passwrdInput ="//*[starts-with(@class,'sign-in-form__form-input-container')]/div[2]/input[1]";
    signInBtn = "(//*[contains(text(),'Sign in')])[2]"
    searchInput = "//*[@Placeholder='Search']"
    autodsLink="(//*[starts-with(@class,'search-nec__hero')])/a"

    def test_Linkedin_Login(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.find_element_by_xpath(self.userNameInput).send_keys("yourid")
        self.driver.find_element_by_xpath(self.passwrdInput).send_keys("yourpass")
        self.driver.find_element_by_xpath(self.signInBtn).click()
        self.driver.find_element_by_xpath(self.searchInput).send_keys("autods")
        self.driver.find_element_by_xpath(self.searchInput).send_keys(Keys.ENTER)
        time.sleep(5)
        autods = self.driver.find_element_by_xpath(self.autodsLink)
        self.driver.execute_script("arguments[0].click();", autods)
        self.driver.quit()





