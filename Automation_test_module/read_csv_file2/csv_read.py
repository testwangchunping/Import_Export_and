#coding=utf-8
import csv
import os
import time
from selenium import webdriver
from Automation_test_module.read_csv_file2.export import Export
class Test(object):
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
        time.sleep(3)
    def test_export(self):
        csvfile=os.path.dirname(os.getcwd())+'\\read_csv_file2\\'
        modules=csv.reader(open(csvfile+'info4.csv','r'))
        i=0
        for module in modules:
            #获取csv文件中的每一行数据，并去掉空元素，组成list
            while '' in module:
                module.remove('')
            module_list=module
            #偶数行（通过link_text获取的模块链接）数据处理
            print(len(module_list))
            # print(module_list[0])
            # print(module_list[1])
            if(i%2==0):
                # if(module_list[0]==module_list[1]):
                #     self.driver.find_elements_by_link_text(module_list[0])[0].click()
                #     time.sleep(2)
                #     self.driver.find_elements_by_link_text(module_list[0])[1].click()
                #     print('执行if')
                #     time.sleep(2)
                for name in module_list:
                    self.driver.find_element_by_link_text(name).click()
                    print('执行for')
                    time.sleep(3)
                module_name_old=name
                try:
                    self.driver.switch_to.frame('app_iframe')
                except:
                    pass
                i=i+1
            elif i%2==1 and module_list:
                #奇数行、非空数据处理
                for j in range(len(module_list)):
                    module_name=module_list[j]
                    self.driver.find_element_by_xpath('//*[@id="content"]/ul/li[{}]/a'.format(j+1)).click()
                    Export(self.driver).old_Export(module_name)
                i=i+1
                if(i%2==0):
                        self.driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/index/index')
            else:
                #奇数行、空数据处理
                    module_name=module_name_old
                    Export(self.driver).old_Export(module_name)
                    i=i+1
                    if(i%2==0):
                        self.driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/index/index')


