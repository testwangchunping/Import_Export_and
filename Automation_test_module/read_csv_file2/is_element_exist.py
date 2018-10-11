#coding=utf-8
from ExportTest.frame.logger import Logger
#logger=Logger(logger='old_Export').getlog()
class IsElementExist(object):
    def __init__(self,driver):
        self.driver=driver
    def is_element_exist(self,classname):
        s=self.driver.find_elements_by_class_name(classname)
        if len(s)==0:
            #logger.debug('元素未找到：%s'%classname)
            return False
        elif len(s)==1:
            return True
        else:
            #logger.debug('找到%s个元素：%s'%(len(s),classname))
            return False



