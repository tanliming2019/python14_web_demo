# _*_ coding:utf-8 _*_
# @time     :  16:11
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : test_login.py
'''测试登录功能'''
import sys
sys.path.append('./')
print(sys.path)

import time
import unittest
import ddt
import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.index import IndexPage
from pages.login import LoginPage
from test_data.login import user_info_error,user_info_authorize,user_info_success
from common.my_log import ReadLogging




my_log=ReadLogging()
@pytest.mark.login
class TestLogin:
    @pytest.mark.error
    @pytest.mark.parametrize("data1,data2,data3",user_info_error)#user_info_success为列表
    def test_login_1_error(self,data1,data2,data3,class_web,founction_web):
        '''请输入手机号'''
        my_log.info('测试数据是：{},{},{}'.format(data1,data2,data3))
        #登录
        self.driver,self.login_page=class_web
        self.login_page.login(data1["username"],data2["pwd"])

        flash_info=self.login_page.get_flash_info()

        #断言
        assert (data3["expected"]==flash_info.text)
        #清空用户数据
        self.login_page.clear_user_info()

    @pytest.mark.auth
    def test_login_2_unaut(self,class_web,founction_web):
        '''号码暂无授权'''
        # 登录
        self.driver, self.login_page = class_web
        self.login_page.login(user_info_authorize["username"], user_info_authorize["pwd"])
        my_log.info('测试数据；{}'.format(user_info_authorize))
        #定位无授权信息元素
        unauth_info=self.login_page.get_unauth_info()
        #断言
        assert (user_info_authorize["expected"] == unauth_info.text)

        # 清空用户数据
        self.login_page.clear_user_info()

    @pytest.mark.success
    def test_login_3_success(self,class_web,founction_web):
        #登录login
        self.driver,self.login_page=class_web
        my_log.info('测试数据；{}'.format(user_info_success))
        self.login_page.login(user_info_success["username"], user_info_success["pwd"])

        #5.断言
        #获取用户信息 get_user_info
        user_ele=IndexPage(self.driver).get_user_info()
        assert (user_info_success["expected"] in user_ele.text)
        self.driver.quit()






if __name__ == '__main__':
    pytest.main(["-m success -s", r"--html=report\test.html",r"--alluredir=report\allure"])