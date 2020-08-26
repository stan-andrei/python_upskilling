from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class SecAss(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(
            "/Users/andrei.stan/Downloads/chromedriver")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 30)

    def test_selenium_page(self):
        driver = self.driver
        driver.get("https://selenium-python.readthedocs.io/")

        SEARCH_INPUT = "q"
        SEARCH_BY = "locating elements"
        SELENIUM_LOGO = "indices-and-tables"
        SELENIUM_URL = "https://selenium-python.readthedocs.io/locating-elements.html?highlight=locating%20elements"

        self.wait.until(EC.visibility_of_element_located((By.ID, SELENIUM_LOGO)))
        searchInput = driver.find_element(By.NAME, SEARCH_INPUT)
        searchInput.clear()
        searchInput.send_keys(SEARCH_BY)
        searchInput.send_keys(Keys.RETURN)

        firstElementFromList = driver.find_element_by_css_selector("#search-results > ul > li:nth-child(1) > a")
        attribute_of_the_first_element = firstElementFromList.get_property("href")
        assert (SELENIUM_URL == attribute_of_the_first_element), "They match"

    def tearDown(self):
        self.driver.quit()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main()
