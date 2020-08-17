
'''
a. Open "google.com" in Chromebrowser and check page is loaded (response code, base page elements)
b. Search after "selenium python"
c. Check first search result is "Selenium WebDriver" with url = https://selenium-python.readthedocs.io/
d. Click on the first link and check same page from c. is displayed.
'''

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

driver.quit()

#if __name__ == "__main__":

