#coding=utf-8
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from ExportTest.configure.read_config_file import ReadConfigFile
import os
from ExportTest.frame.is_element_exist import IsElementExist
import time
class Importe(object):
    def __init__(self,driver,logger,module_name):
        self.driver=driver
        self.logger=logger
        self.module_name=module_name
    readConfig=ReadConfigFile()

    #import_module_name,导入文件应该以模块名命名规则
    #1、奇数列为空，即列表中无table切换，导入文件名为“最后一个link_text导航栏名”；
    # 2、奇数列不为空，即列表中有table切换，导入文件名为“切换的table的名字”）

    import_text='导入'
    iframe_name='app_iframe'

    #文件上传按钮
    import_file_button1='upload-file'
    import_file_button2='file'

    #确认导入按钮
    confirm_button1='OK-Button'
    confirm_button2='save_button'

    #导入成功的提示
    import_success_message='//*[@id="task_body"]/div/div[1]/span[1]'
    #导入成功后，返回上一级按钮
    import_success_button='//*[@id="task_body"]/div/div[1]/a'

    #返回上级按钮
    return_button='btn_back'
    #导入失败的提示
    error_message='没有可导入的文件、导入文件名错误、导入失败或请求超时'

    def test_old_importe(self):
        iee=IsElementExist(self.driver,self.logger)
        if iee.is_element_exist_partial_link_text(self.import_text):
            elements=self.driver.find_elements_by_partial_link_text(self.import_text)
            number=len(elements)

            for id in range(number):
                time.sleep(2)
                elements=self.driver.find_elements_by_partial_link_text(self.import_text)

                text=elements[id].text
                elements[id].click()
                time.sleep(2)
                try:
                    self.driver.switch_to.frame(self.iframe_name)
                except:
                    pass
                file_path=os.path.dirname(os.getcwd())+'\\data\\'
                try:
                    if number==1:
                        import_file=file_path+self.module_name+'.xls'
                    else:
                        import_file=file_path+self.module_name+str(id+1)+'.xls'
                    self.driver.find_element_by_id(self.import_file_button1).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element_by_id(self.confirm_button1).click()
                except:
                    pass
                try:
                    if number==1:
                        import_file=file_path+self.module_name+'.zip'
                    else:
                        import_file=file_path+self.module_name+str(id+1)+'.zip'
                    self.driver.find_element_by_name(self.import_file_button2).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element_by_id(self.confirm_button2).click()
                except:
                    pass

                try:
                    #webdriver显示等待：WebDriverWait
                    message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.import_success_message)))
                    tips=message.text
                    self.logger.info(self.module_name+'-->'+text+':'+tips)
                    time.sleep(1)
                    self.driver.find_element_by_xpath(self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element_by_class_name(self.return_button).click()
                except:
                    self.logger.warning(self.module_name+self.error_message)
                    self.driver.get(self.readConfig.f5_url)
        else:
            pass
    def test_new_importe(self):

        iee=IsElementExist(self.driver,self.logger)

        if iee.is_element_exist_partial_link_text(self.import_text):
            elements=self.driver.find_elements_by_partial_link_text(self.import_text)
            number=len(elements)
            print(number)
            for id in range(number):
                elements=self.driver.find_elements_by_partial_link_text(self.import_text)
                text=elements[id].text
                elements[id].click()
                time.sleep(2)
                try:
                    self.driver.switch_to.frame(self.iframe_name)
                except:
                    pass

                try:
                    file_path=os.path.dirname(os.getcwd())+'\\data\\'
                    if number==1:
                        import_file=file_path+self.module_name+'.xls'
                    else:
                        import_file=file_path+self.module_name+str(id+1)+'.xls'
                    self.driver.find_element_by_id(self.import_file_button1).send_keys(import_file)
                    time.sleep(2)
                    self.driver.find_element_by_id(self.confirm_button1).click()

                    #webdriver显示等待：WebDriverWait
                    message=WebDriverWait(self.driver,60,3,None).until(EC.presence_of_element_located((By.XPATH,self.import_success_message)))
                    tips=message.text
                    self.logger.info(self.module_name+'-->'+text+':'+tips)
                    time.sleep(1)
                    self.driver.find_element_by_xpath(self.import_success_button).click()
                    time.sleep(1)
                    self.driver.find_element_by_class_name(self.return_button).click()
                except:
                    self.logger.warning(self.module_name+self.error_message)
                    self.driver.get(self.readConfig.f5_url)
        else:
            pass