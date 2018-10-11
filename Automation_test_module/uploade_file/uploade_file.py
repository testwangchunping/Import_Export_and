from selenium import webdriver
from Automation_test_module.change_table.is_element_exist import IsElementExist
import time
import os
import csv
driver=webdriver.Chrome()
driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/login/index')
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element_by_name('company').send_keys('zdh2')
driver.find_element_by_name('account').send_keys('boss')
driver.find_element_by_name('pass').send_keys('aaaaaa')
driver.find_element_by_class_name('login_btn').click()

csvfile=os.path.dirname(os.getcwd())+'\\uploade_file\\'
modules=csv.reader(open(csvfile+'old_import.csv','r'))
for module in modules:
    #获取csv文件中的每一行数据，并去掉空元素，组成list
    while '' in module:
        module.remove('')
    module_list=module
try:
    if(module_list[0]==module_list[1]):
        driver.find_element_by_link_text(module_list[0]).click()
        time.sleep(1)
        driver.find_elements_by_link_text(module_list[0])[1].click()
        time.sleep(1)
except:
    pass
for name in module_list:
    get_module_name=name
    driver.find_element_by_link_text(name).click()
    time.sleep(1)
try:
    driver.switch_to.frame('app_iframe')
except:
    pass
driver.find_element_by_xpath('//*[@id="content"]/div[1]/a[3]').click()
try:
    driver.switch_to.frame('app_iframe')
except:
    pass
file_path=os.path.dirname(os.getcwd())+'\\uploade_file\\'
import_file=file_path+'商品管理2'+'.zip'
driver.find_element_by_name('file').send_keys(import_file)
time.sleep(2)
driver.find_element_by_id('OK-Button').click()

