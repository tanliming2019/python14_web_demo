# _*_ coding:utf-8 _*_
# @time     :  17:49
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : user.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from pages.base import BasePage


class UserPage(BasePage):
    '''用户页面'''
    user_money_locator=(By.XPATH,"//li[@class='color_sub']")

    def get_user_money(self):
        '''获取用户余额'''
        e=self.wait_presence_element(self.user_money_locator)
        money=e.text[:-1].strip()   #strip()去除两边空格
        return money  #现在是一个字符串
