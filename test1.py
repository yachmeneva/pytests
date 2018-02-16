import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chromedriver = "/Users/apple/workspace/chromedriver"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
#driver = webdriver.Firefox()
driver.get("https://www.python.org/")
assert "Python" in driver.title
elem = driver.find_element_by_name("q")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
driver.close()

