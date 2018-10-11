#coding=utf-8
import csv
import os

from ExportTest.configure.read_config_file import ReadConfigFile
from ExportTest.data_process.js_rows_process import Js_Rows_Process
from ExportTest.data_process.juge_old_export import Juge_Old_Export
from ExportTest.data_process.os_rows_process import Os_Rows_Process


class Read_Old_Export(object):
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
    readConfig=ReadConfigFile()
    def test_old_export(self):
        csvfile=os.path.dirname(os.getcwd())+'\\data\\'
        modules=csv.reader(open(csvfile+'old_export.csv','r'))
        #获取文件总行数
        count=len(open(csvfile+'old_export.csv', 'r').readlines())
        i=0
        for module in modules:
            #获取csv文件中的每一行数据，并去掉空元素，组成list
            while '' in module:
                module.remove('')
            module_list=module
            #偶数行（通过link_text获取的模块链接）数据处理
            if(i%2==0):
                #偶数行数据处理
                last_module_name=Os_Rows_Process(module_list,self.driver).os_rows_process()
            elif i%2==1 and module_list:
                #奇数行、非空数据处理
                for j in range(len(module_list)):
                    get_module_name=Js_Rows_Process(module_list,j,self.driver).js_rows_process()
                    #判断导出照片、导出
                    Juge_Old_Export(self.driver,self.logger,get_module_name).juge_old_export()
            else:
                #奇数行、空数据处理
                get_module_name=last_module_name
                #判断导出照片、导出
                Juge_Old_Export(self.driver,self.logger,get_module_name).juge_old_export()
            i=i+1
            if(i%2==0):
                    #页面刷新到首页
                    self.driver.get(self.readConfig.f5_url)
        if(i%2==1 and i==count):
            #处理最后一行为偶数的数据(即页面无table切换)
            Juge_Old_Export(self.driver,self.logger,last_module_name).juge_old_export()
            #页面刷新到首页
            self.driver.get(self.readConfig.f5_url)
        if(i==0 and i==count):
            #处理最后一行为偶数（0）的数据(即页面无table切换)
            Juge_Old_Export(self.driver,self.logger,last_module_name).juge_old_export()
            #页面刷新到首页
            self.driver.get(self.readConfig.f5_url)
