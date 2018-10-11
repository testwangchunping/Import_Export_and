#coding=utf-8
import HTMLTestRunner
import unittest
import os
import time

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))

# 设置报告名称格式
HtmlFile = report_path + now + "HTMLReport.html"
fp = open(HtmlFile, "wb")
suite=unittest.TestLoader().discover('H:\\selenium_test\\demo\\xbwq5\ExportTest\\testsuits')

if __name__=='__main__':
    #执行用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=u"某某项目测试报告", description=u"用例测试情况")
    # 开始执行测试套件
    runner.run(suite)
