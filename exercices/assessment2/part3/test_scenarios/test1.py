"""
Steps test 1:
Go to https://selenium-python.readthedocs.io/ page
search for “locating elements”
Check if first element retrieved by search is highlighted and contains both searching elements.
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
search_box = driver.find_element_by_name('q')
search_box.send_keys('locating elements')
search_box.submit()
assert "Search" in driver.title
driver.find_element_by_partial_link_text("Locating").click()
assert "Locating Elements" in driver.title
time.sleep(2)
driver.quit()

#if __name__ == "__main__":