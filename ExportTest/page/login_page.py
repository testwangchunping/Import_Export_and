from ExportTest.configure.read_config_file import ReadConfigFile
from ExportTest.frame.web_element_wait import Web_Element_Wait
from selenium.webdriver.common.by import By
class Login_Page(object):
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
    company_name='company'
    account_name='account'
    password='pass'
    login_button='login_btn'

    readConfig=ReadConfigFile()

    def input_company(self):
        self.driver.find_element_by_name(self.company_name).send_keys(self.readConfig.U_company)
    def input_account(self):
        self.driver.find_element_by_name(self.account_name).send_keys(self.readConfig.U_account)
    def input_password(self):
        self.driver.find_element_by_name(self.password).send_keys(self.readConfig.U_password)
    def click_login(self):
        self.driver.find_element_by_class_name(self.login_button).click()
    def login_wait(self):
        try:
            tips=Web_Element_Wait(self.driver).web_element_wait(5,1,By.CLASS_NAME,self.error_tips)
            self.logger.warning(tips)
        except:
            pass

