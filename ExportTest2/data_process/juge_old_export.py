from ExportTest.frame.is_element_exist import IsElementExist
from ExportTest.service.export import Export

class Juge_Old_Export(object):
    def __init__(self,driver,logger,module_name):
        self.driver=driver
        self.logger=logger
        self.module_name=module_name
    #导出按钮id
    export_id='Export'
    export_photo_id='Export_photo'
    def juge_old_export(self):
        iee=IsElementExist(self.driver,self.logger)
        if iee.is_element_exist_id(self.export_id):
            Export(self.driver,self.logger).old_Export(self.module_name)
        else:
            pass
        if iee.is_element_exist_id(self.export_photo_id):
            Export(self.driver,self.logger).old_Export_Photo(self.module_name)
        else:
            pass