"""
Go to https://selenium-python.readthedocs.io/ page
From left menu click on “WebDriver API”
Click on ‘Alerts’
Check Alerts section of the page is visible
Try to scroll down the page using selenium methods and go to the bottom of the page.
Check if bottom was reached
"""

import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/andrei.stan/upskilling/upskilling/lib/python3.8/site-packages/selenium/webdriver/chromedriver")
driver.maximize_window()
driver.get('http://www.google.com/');
time.sleep(2)
search_box = driver.find_element_by_name('q')
search_box.send_keys('selenium python')
search_box.submit()
driver.find_element_by_partial_link_text("Selenium with Python — Selenium Python Bindings 2 ...").click()
assert "Selenium with Python" in driver.title
time.sleep(2)
driver.find_element_by_partial_link_text("7. WebDriver API").click()
assert "7. WebDriver API" in driver.title
driver.find_element_by_partial_link_text("7.3. Alerts").click()
assert "7.3. Alerts" in driver.page_source
time.sleep(2)
driver.execute_script("window, scrollBy(0,document.body.scrollHeight)")
time.sleep(4)
assert "Sphinx 1.7.9" in driver.page_source
driver.quit()

#if __name__ == "__main__":