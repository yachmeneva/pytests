#encoding: utf-8
import os 
import unittest
from selenium import webdriver

class LoginUserSuccessTest(unittest.TestCase):
	"""Проверка успешного логина обычного юзера"""

	def setUp(self):
		#chromedriver_path = "chromedriver"
		chromedriver_path = "/Users/apple/workspace/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver_path
		self.driver = webdriver.Chrome(chromedriver_path)
		self.url = "https://test.new.snob.ru/"

	def test_correct_login_usual(self):
		driver = self.driver
		driver.get(self.url)
		self.assertIn(u'Сноб', driver.title)
		login_link = driver.find_element_by_xpath("//*[@id='header']/ul[2]/li/div/a")
		login_link.click()

		login_input = driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div[2]/form/input[3]")
		pwd_input = driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div[2]/form/input[4]")

		driver.wait(3000)

		login_input.send_keys("oiachmeneva")
		pwd_input.send_keys("LJ9ev36U")

		login_btn = driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div[2]/form/input[5]")
		login_btn.click()

		username_link = driver.find_element_by_xpath("//*[@id='header']/ul[2]/li[2]/a")
		#username_link = driver.find_element_by_link_text(u'Ольга Ячменева')
		self.assertEqual(username_link.get_text(), u'Ольга Ячменева')

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
    unittest.main()