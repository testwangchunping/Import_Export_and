#coding=utf-8
from ExportTest.frame.is_element_exist import IsElementExist
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class Export(object):
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger
    #旧导出
    old_export_id='Export'
    old_export_photo_id='Export_photo'
    old_export_success_message='//*[@id="task_body"]/a'
    old_close_export_window='btn_ok'
    old_mult_photo_exort='photo'
    #新导出
    new_export_id1='async_export'
    #导出考勤报表弹窗元素
    window_include_message='explain'   #考勤报表导出选择
    #订单导出
    new_export_id2='btn_order_export' #订单导出按钮
    order_radio_choose1='form-radio'
    order_radio_choose2='//*[@type="radio"]'
    order_click_export='btn_ok' #导出订单弹窗-确定
    close_order_window='btn_cancel'    #导出订单弹窗-取消
    #定位轨迹导出
    new_export_id3='btn_expor_track'   #轨迹导出按钮
    new_export_id31='btn_add_export_task'   #轨迹导出按钮
    tree_checkbox='x-tree-item-checkbox'
    new_export_success_message='//*[@class="ow_open_cont"]/div/span'  #导出成功提示
    new_close_export_window='confirm'  #导出成功后，关闭弹窗
    tree_select='//*[@id="export_user_dept"]/div/div/div[2]/div/div[2]/div[3]/div/i[2]'  #轨迹导出，树结构选择，选择第一个部门
    export_error_message='导出失败或请求超时'
    close_select_window='ow_open_close'


    def old_Export(self,module_name):
        time.sleep(1)
        elements=self.driver.find_elements_by_id(self.old_export_id)
        number=len(elements)
        for id in range(number):
            text=elements[id].text
            elements[id].click()
            iee=IsElementExist(self.driver,self.logger)
            if iee.is_element_exist_class(self.window_include_message)==True:
                self.driver.find_element_by_class_name(self.old_close_export_window).click()
            else:
                pass
            try:
                #webdriver显示等待：WebDriverWait
                message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.old_export_success_message)))
                tips=message.text
                self.logger.info(module_name+'-->'+text+':'+tips)
            except:
                self.logger.warning(module_name+'-->'+text+':'+self.export_error_message)
            self.driver.find_element_by_class_name(self.old_close_export_window).click()
            time.sleep(1)
    def old_Export_Photo(self,module_name):
        element=self.driver.find_element_by_id(self.old_export_photo_id)
        text=element.text
        element.click()
        time.sleep(1)
        try:
            self.driver.find_element_by_class_name(self.old_mult_photo_exort).click()
            self.driver.find_element_by_class_name(self.old_close_export_window).click()
        except:
            pass
        try:
            #webdriver显示等待：WebDriverWait
            message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.old_export_success_message)))
            tips=message.text
            self.logger.info(module_name+'-->'+text+':'+tips)
        except:
            self.logger.warning(module_name+'-->'+text+':'+self.export_error_message)
        self.driver.find_element_by_class_name(self.old_close_export_window).click()
        time.sleep(1)
    def new_Export(self,module_name):
        iee=IsElementExist(self.driver,self.logger)
        #获取模块名
        elements=''
        if iee.is_element_exist_classes(self.new_export_id1):
            elements=self.driver.find_elements_by_class_name(self.new_export_id1)
        elif iee.is_element_exist_id(self.new_export_id2):
            elements=self.driver.find_elements_by_id(self.new_export_id2)
        elif iee.is_element_exist_id(self.new_export_id3):
            elements=self.driver.find_elements_by_id(self.new_export_id3)
        else:
            pass
        number=len(elements)
        for id in range(number):
            text=elements[id].text
            elements[id].click()
            #订单导出
            if iee.is_element_exist_classes(self.order_radio_choose1):
                for i in self.driver.find_elements_by_xpath(self.order_radio_choose2):
                    i.click()
                    self.driver.find_element_by_class_name(self.order_click_export).click()
                    try:
                        #webdriver显示等待：WebDriverWait
                        message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.new_export_success_message)))
                        tips=message.text
                        self.logger.info(module_name+'-->'+text+':'+tips)
                    except:
                        self.logger.warning(module_name+'-->'+text+self.export_error_message)
                    self.driver.find_element_by_class_name(self.new_close_export_window).click()
                self.driver.find_element_by_class_name(self.close_order_window).click()
            #定位轨迹导出
            elif iee.is_element_exist_classes(self.tree_checkbox):
                time.sleep(2)
                self.driver.find_element_by_xpath(self.tree_select).click()
                t_max=datetime.datetime.now()
                t_min=t_max-datetime.timedelta(days=2)
                max_time=datetime.datetime.strftime(t_max,'%Y-%m-%d')
                min_time=datetime.datetime.strftime(t_min,'%Y-%m-%d')
                self.driver.find_element_by_id('min_time').send_keys(min_time)
                self.driver.find_element_by_id('max_time').send_keys(max_time)
                self.driver.find_element_by_id(self.new_export_id31).click()
                try:
                    #webdriver显示等待：WebDriverWait
                    message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.new_export_success_message)))
                    tips=message.text
                    self.logger.info(module_name+'-->'+text+':'+tips)
                except:
                    self.logger.warning(module_name+'-->'+text+self.export_error_message)
                self.driver.find_element_by_class_name(self.new_close_export_window).click()
                self.driver.find_element_by_class_name(self.close_select_window).click()
            #其他普通导出
            else:
                try:
                    #webdriver显示等待：WebDriverWait
                    message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.new_export_success_message)))
                    tips=message.text
                    self.logger.info(module_name+'-->'+text+':'+tips)
                except:
                    self.logger.warning(module_name+'-->'+text+self.export_error_message)
                self.driver.find_element_by_class_name(self.new_close_export_window).click()

