#coding=utf-8
import unittest
from ExportTest.data_process.read_new_export import Read_New_Export
from ExportTest.data_process.read_old_export import Read_Old_Export
from ExportTest.frame.browser_engine import BrowserEngine
from ExportTest.frame.logger import Logger
from ExportTest.service.login import Test_Login
class Test_Export_Suit(unittest.TestCase):
    """
    导出用例
    """
    @classmethod
    def setUpClass(cls):
        cls.driver=BrowserEngine().get_browser()
        cls.logger=Logger(logger='Export').getlog()
        Test_Login(cls.driver,cls.logger).test_login()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        cls.logger.realse()


    def test_old_export(self):
        """
        旧的模块导出
        """
        Read_Old_Export(self.driver,self.logger).test_old_export()

    def test_new_export(self):
        """
        重构模块的导出
        """
        Read_New_Export(self.driver,self.logger).test_new_export()

    if __name__=='__main__':
        unittest.main



