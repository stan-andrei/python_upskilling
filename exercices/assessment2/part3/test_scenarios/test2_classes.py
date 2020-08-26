from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import unittest


class SecAss2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("/Users/andrei.stan/upskilling/upskilling/exercices/assessment2/part2/venv-upskilling/lib/python3.8/site-packages/selenium/webdriver/chromedriver")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def test_selenium_page(self):
        driver = self.driver
        self.driver.get('http://www.google.com/')
        self.search_box = driver.find_element_by_name('q')
        self.search_box.send_keys('selenium python')
        self.search_box.submit()
        self.driver.find_element_by_partial_link_text("Selenium with Python — Selenium Python Bindings 2 ...").click()
        assert "Selenium with Python" in driver.title
        self.driver.find_element_by_partial_link_text("7. WebDriver API").click()
        assert "7. WebDriver API" in driver.title
        self.driver.find_element_by_partial_link_text("7.3. Alerts").click()
        assert "7.3. Alerts" in driver.page_source
        self.driver.execute_script("window, scrollBy(0,document.body.scrollHeight)")
        assert "Sphinx 1.8.5" in driver.page_source

    def tearDown(self):
        self.driver.quit()
        print("Test Completed")

if __name__ == "__main__":
    unittest.main()