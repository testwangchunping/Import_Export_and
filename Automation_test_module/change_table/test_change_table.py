from selenium import webdriver
from Automation_test_module.change_table.is_element_exist import IsElementExist
import time
driver=webdriver.Chrome()
driver.get('http://wqtest.xbwq.com.cn/wq/admin/core/login/index')
driver.maximize_window()
driver.implicitly_wait(4)

driver.find_element_by_name('company').send_keys('zdh2')
driver.find_element_by_name('account').send_keys('boss')
driver.find_element_by_name('pass').send_keys('aaaaaa')
driver.find_element_by_class_name('login_btn').click()

driver.find_element_by_link_text('客户管理').click()
driver.find_element_by_link_text('客户资料设置').click()
iee=IsElementExist(driver)
list=['1','2','3','4']
for i in range(len(list)):
# driver.find_element_by_partial_link_text('区域').click()
    driver.find_element_by_xpath('//*[@class="content"]/div[1]/a[{}]'.format(i+1)).click()
    try:
        driver.switch_to.frame('app_iframe')
    except:
        pass
    if iee.is_element_exist_partial_link_text('导入'):
        driver.find_element_by_partial_link_text('导入').click()
    time.sleep(2)
    print('跳转')
    #跳出表单
    try:
        driver.switch_to.default_content()
    except:
        pass







