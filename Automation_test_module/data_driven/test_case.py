import time
from selenium import webdriver
class Login(object):
    def __init__(self):
        self.driver=webdriver.Firefox()
        self.driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/login/index')
        self.driver.maximize_window()
        self.driver.implicitly_wait(4)
    def user_login(self,company,account,password):
        self.driver.find_element_by_name('company').send_keys(company)
        self.driver.find_element_by_name('account').send_keys(account)
        self.driver.find_element_by_name('pass').send_keys(password)
        self.driver.find_element_by_class_name('login_btn').click()
