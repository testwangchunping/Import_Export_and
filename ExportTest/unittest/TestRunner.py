#coding=utf-8
import HTMLTestRunner
import os
import time
import unittest

# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'

# 获取系统当前时间
now = time.strftime("%Y-%m-%d", time.localtime(time.time()))
# 设置报告名称格式
HtmlFile = report_path + now + "Report.html"
#通过open()方法以二进制写模式打开当前目录下的Report.html，如果没有，则自动创建该文件
fp = open(HtmlFile, "wb")

#discover找到指定目录下所有测试模块，并可递归查到子目录下的测试模块，只有匹配到的文件才能被加载
suite = unittest.TestLoader().discover('H:\\selenium_test\\demo\\xbwq5\\ExportTest\\testsuits', pattern='test*.py')

if __name__=='__main__':

    #执行用例
    # 初始化一个HTMLTestRunner实例对象，用来生成报告（stream用来指定测试报告文件，title定义测试报告标题，description定义测试报告副标题）
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="项目导入导出测试报告", description="用例测试情况")
    # 开始执行测试套件中所组装的测试用例
    runner.run(suite)
    #关闭报告文件
    fp.close()

