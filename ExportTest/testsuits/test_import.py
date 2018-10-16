#coding=utf-8
import unittest

from ExportTest.data_process.read_new_import import Read_New_Import
from ExportTest.data_process.read_old_import import Read_Old_Import
from ExportTest.frame.browser_engine import BrowserEngine
from ExportTest.frame.logger import Logger
from ExportTest.service.login import Test_Login


class Test_Import_Suit(unittest.TestCase):
    """
    导入用例
    """
    @classmethod
    def setUpClass(cls):
        cls.driver=BrowserEngine().get_browser()
        cls.logger = Logger(logger='Import').getlog()
        Test_Login(cls.driver,cls.logger).test_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.realse()

    def test_old_import(self):
        """
        未重构模块导入
         """
        Read_Old_Import(self.driver,self.logger).test_old_import()

    def test_new_import(self):
        """
        重构模块导入
        """
        Read_New_Import(self.driver, self.logger).test_new_import()

    if __name__=='__main__':

        unittest.main


