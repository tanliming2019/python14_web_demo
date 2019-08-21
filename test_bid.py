# _*_ coding:utf-8 _*_
# @time     :  2:22
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : test_bid.py
import sys
sys.path.append('./')
print(sys.path)
import time
import unittest
import ddt
import pytest
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.bid import BidPage
from pages.index import IndexPage
from pages.login import LoginPage
from pages.user import UserPage
from test_data.bid import invest_money
from test_data.login import user_info_success

'''投资的前置条件：
1.登录
2.有没有余额  1.查询余额，不够的话去充值 ————>接口充值  3.改数据库  4.直接充100亿  手动充值更快
3.标有没有钱  没有的话去创建一个标（手动）
'''


class TestBid:
    '''测试投资'''
    @pytest.mark.aa
    def test_bid_sucess(self,class_web2,founction_web):

        self.driver,self.bid_page=class_web2
        #在首页选择标的 choose_bid(),点击投标
        IndexPage(self.driver).choose_bid()

        #定位投资输入框元素 get_bid_input_element()
        e=self.bid_page.get_bid_input_element()

        #投资前金额
        expect=float(e.get_attribute('data-amount'))
        print(expect)

        #发送投资金额
        e.send_keys(invest_money)

        #点击投标按钮
        self.bid_page.click_bid_submit()
        # print("当前时间： ",time.strftime('%Y.%m.%d %H:%M ',time.localtime(time.time())))

        #激活并查看
        self.bid_page.click_alert()

        #用户余额
        actual_money_str=UserPage(self.driver).get_user_money()
        actual_money= float(actual_money_str)

        #调试
        print(int(expect * 100))
        print(int(invest_money * 100))
        print(actual_money * 100)

        assert (int(expect * 100) - invest_money * 100 == actual_money* 100)





if __name__ == '__main__':
    unittest.main()
