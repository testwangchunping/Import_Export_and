#coding=utf-8
class IsElementExist(object):
    def __init__(self,driver,logger):
        self.driver=driver
        self.logger=logger

    def is_element_exist_class(self,classname):
        s=self.driver.find_elements_by_class_name(classname)
        if len(s)==0:
            self.logger.debug('元素未找到：%s'%classname)
            return False
        elif len(s)==1:
            return True
        else:
            self.logger.debug('找到%s个元素：%s'%(len(s),classname))
            return False
    def is_element_exist_classes(self,classname):
        s=self.driver.find_elements_by_class_name(classname)
        if len(s)==0:
            self.logger.debug('元素未找到：%s'%classname)
            return False
        elif len(s)==1:
            return True
        else:
            self.logger.debug('找到%s个元素：%s'%(len(s),classname))
            return True
    def is_element_exist_id(self,id):
        s=self.driver.find_elements_by_id(id)
        if len(s)==0:
            self.logger.debug('元素未找到：%s'%id)
            return False
        elif len(s)==1:
            return True
        else:
            self.logger.debug('找到%s个元素：%s'%(len(s),id))
            return False
    def is_element_exist_partial_link_text(self,link_text):
        s=self.driver.find_elements_by_partial_link_text(link_text)
        if len(s)==0:
            self.logger.debug('元素未找到：%s'%link_text)
            return False
        elif len(s)==1:
            return True
        else:
            self.logger.debug('找到%s个元素：%s'%(len(s),link_text))
            return True
    def is_element_exist_tag_name(self,tag_name):
        s=self.driver.find_elements_by_tag_name(tag_name)
        if len(s)==0:
            self.logger.debug('元素未找到：%s'%tag_name)
            return False
        elif len(s)==1:
            return True
        else:
            self.logger.debug('找到%s个元素：%s'%(len(s),tag_name))
            return True
