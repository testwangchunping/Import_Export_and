from ExportTest.configure.read_config_file import ReadConfigFile
from ExportTest.frame.logger import Logger
from ExportTest.page.login_page import Login_Page
class Test_Login(object):
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
    def test_login(self):
        login_Page=Login_Page(self.driver,self.logger)
        login_Page.input_company()
        login_Page.input_account()
        login_Page.input_password()
        login_Page.click_login()
        login_Page.login_wait()

