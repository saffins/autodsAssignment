import time


from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from datetime import date


class Test_Task1:
    baseurl="https://www.amazon.in"
    searchBar ="twotabsearchtextbox";
    searchBtn = "nav-search-submit-button"
    primeItems = "//*[@aria-label='Amazon Prime']/parent::span/parent::span/following-sibling::span/span[2]"
    itemToSelect= "(//*[@aria-label='Amazon Prime']/parent::span/parent::span/parent::div/parent::div/parent::div/parent::div/div/h2/a)[index]"
    addToCartBtn= "add-to-cart-button"

    def test_search(self):
        self.driver=webdriver.Chrome(ChromeDriverManager().install())
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.find_element_by_id(self.searchBar).send_keys("Coffee cups")
        self.driver.find_element_by_id(self.searchBtn).click()
        items = self.driver.find_elements_by_xpath(self.primeItems)
        today = date.today().strftime("%d")

        itemIndex=0
        for elem in items:
            if(elem.text.split(" ")[0])=="Tomorrow,":
                elem.click()
                itemIndex+=1
                break

        self.driver.find_element_by_xpath(self.itemToSelect.replace("index",str(itemIndex))).click()
      #  self.driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
        chld = self.driver.window_handles[1]
        self.driver.switch_to.window(chld)
        addbtn =  self.driver.find_element_by_id(self.addToCartBtn)
        self.driver.execute_script("arguments[0].click();",addbtn)


        time.sleep(5)
        self.driver.quit()
