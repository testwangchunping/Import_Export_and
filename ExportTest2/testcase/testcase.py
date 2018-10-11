#coding=utf-8

import unittest
from ExportTest.data_process.read_new_export import Read_New_Export
from ExportTest.data_process.read_new_import import Read_New_Import
from ExportTest.data_process.read_old_export import Read_Old_Export
from ExportTest.data_process.read_old_import import Read_Old_Import
from ExportTest.frame.browser_engine import BrowserEngine
from ExportTest.frame.logger import Logger
from ExportTest.service.login import Test_Login

class Import_and_Export(unittest.TestCase):
    #打开url
    @classmethod
    def setUpClass(cls):
        cls.driver=BrowserEngine().get_browser()
        cls.logger=Logger(logger='Import_and_Export').getlog()
        Test_Login(cls.driver,cls.logger).test_login()

    @classmethod
    def tearDownClass(cls):
        pass
        cls.driver.quit()

    def test_old_export(self):
        #旧的模块导出
        Read_Old_Export(self.driver,self.logger).test_old_export()

    def test_new_export(self):
        #重构模块的导出
        Read_New_Export(self.driver,self.logger).test_new_export()

    def test_old_import(self):
        Read_Old_Import(self.driver,self.logger).test_old_import()

    def test_new_import(self):
        Read_New_Import(self.driver,self.logger).test_new_import()

    if __name__=='__main__':
        unittest.main



