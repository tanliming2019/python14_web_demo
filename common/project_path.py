# _*_ coding:utf-8 _*_
# @time     :  0:25
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : project_path.py
import os
#文件路径  放这里
project_path=os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
print(project_path)
#
# #测试报告的路径
# report_path=os.path.join(project_path,'test_result','test_report','Test_report.html')
# # print(report_path)
#
#日志的路径
my_log_path=os.path.join(project_path,'test_result','test_log','test_log.log')
print(my_log_path)
#
# #配置文件的路径
# conf_path=os.path.join(project_path,'conf','case.conf')
# print(conf_path)
# conf_new_path=os.path.join(project_path,'conf','case_new.conf')