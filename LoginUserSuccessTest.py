#encoding: utf-8
import os 
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginUserSuccessTest(unittest.TestCase):
	"""Проверка логина обычного юзера"""

	def setUp(self):
		#chromedriver_path = "chromedriver"
		chromedriver_path = "/Users/apple/workspace/chromedriver"
		os.environ["webdriver.chrome.driver"] = chromedriver_path
		self.driver = webdriver.Chrome(chromedriver_path)
		self.url = "https://test.new.snob.ru/"
		self.driver.implicitly_wait(10) 

	def test_correct_login_usual(self):
		print(u'Проверка логина с использованием корректного логина и пароля')
		driver = self.driver
		driver.get(self.url)
		self.assertIn(u'Сноб', driver.title)

		login_link = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='header']/ul[2]/li/div/a")))
		#login_link = driver.find_element_by_xpath("//*[@id='header']/ul[2]/li/div/a")
		login_link.click()

		login_input = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='loginModal']/div/div/div[2]/form/input[3]")))
		login_input.clear()
		login_input.send_keys("oiachmeneva")

		pwd_input = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='loginModal']/div/div/div[2]/form/input[4]")))
		pwd_input.clear()
		pwd_input.send_keys("LJ9ev36U")


		#login_btn = driver.find_element_by_xpath("//*[@id='loginModal']/div/div/div[2]/form/input[5]")
		login_btn = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='loginModal']/div/div/div[2]/form/input[5]")))
		login_btn.click()

		#username_link = driver.find_element_by_xpath("//*[@id='header']/ul[2]/li[2]/a")
		username_link = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='header']/ul[2]/li[2]/a")))
		
		self.assertEqual(username_link.text, u'Ольга Ячменева')

		driver.get(self.url + "news/157563")
		username_link_inner_page = WebDriverWait(driver, 20).until(
        	EC.element_to_be_clickable((By.XPATH, "//*[@id='header']/ul[2]/li[2]/a")))
		self.assertEqual(username_link_inner_page.text, u'Ольга Ячменева')

	def tearDown(self):
		self.driver.close()

unittest.main()