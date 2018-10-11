#coding=utf-8
from Automation_test_module.read_csv_file2.is_element_exist import IsElementExist
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Export(object):
    def __init__(self,driver):
        self.driver=driver
    def old_Export(self,module_name):
        time.sleep(3)
        elements=self.driver.find_elements_by_id('Export')
        number=len(elements)
        for id in range(number):
            text=elements[id].text
            print(text)
            elements[id].click()
            iee=IsElementExist(self.driver)
            if iee.is_element_exist('explain')==True:
                self.driver.find_element_by_class_name('btn_ok').click()
            else:
                pass
            try:
                #webdriver显示等待：WebDriverWait
                message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,'//*[@id="task_body"]/a')))
                tips=message.text
                print(module_name+'-->'+text+':'+tips)
                # self.logger.info(module_name+'-->'+text+':'+tips)
            except:
                print(module_name+'-->'+text+':'+'导出失败或请求超时')
                # self.logger.warning(module_name+'-->'+text+':'+'导出失败或请求超时')
            self.driver.find_element_by_class_name('btn_ok').click()
            time.sleep(2)

    def old_Export_Photo(self):
        module_name=self.driver.find_element_by_xpath('//*[@class="breadcrumbs"]/ul/li[2]/a').text
        element=self.driver.find_element_by_id('Export_photo')
        text=element.text
        element.click()
        try:
            #webdriver显示等待：WebDriverWait
            message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,'//*[@id="task_body"]/a')))
            tips=message.text
            #self.logger.info(module_name+'-->'+text+':'+tips)
        except:
            pass
            #self.logger.warning('导出失败或请求超时')
        self.driver.find_element_by_class_name('btn_ok').click()
    def new_Export(self):
        #获取模块名
        module_name=self.driver.find_element_by_xpath('//*[@class="breadcrumbs"]/ul/li[2]/a').text
        elements=self.driver.find_elements_by_class_name('async_export')
        number=len(elements)
        for id in range(number):
            text=elements[id].text
            elements[id].click()
            try:
                #webdriver显示等待：WebDriverWait
                message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,'//*[@class="ow_open_cont"]/div/a')))
                tips=message.text
                #self.logger.info(module_name+'-->'+text+':'+tips)
                time.sleep(5)
            except:
                pass
                #self.logger.warning(module_name+'-->'+text+':导出失败或请求超时')
            self.driver.find_element_by_class_name('confirm').click()

