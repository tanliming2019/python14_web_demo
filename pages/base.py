# _*_ coding:utf-8 _*_
# @time     :  15:10
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : base.py
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import login_locators
import logging

class BasePage:
    '''基类'''
    #初始化一个浏览器
    def __init__(self,driver:Chrome):
        self.driver=driver

    def wait_presence_element(self,locator,timeout=10,poll_frequency=0.1):
        '''等待元素出现  定义复杂，调用简单'''
        try:
            ele = WebDriverWait(self.driver, timeout,poll_frequency).until(
                ec.presence_of_element_located(locator))
            return ele
        except Exception as e:
            #logger
            logging.error('元素定位失败')
        #截屏
        self.driver.save_screenshot('test.jpg')



    def wait_clickable_element(self,locator):
        '''等待可以点击的元素出现'''
        ele=WebDriverWait(self.driver, 30).until(
            ec.element_to_be_clickable(locator))
        return ele

    # def switch(self,name="",if_window=True):
    #     '''窗口、iframe、alert切换'''
    #     if name=="":
    #         #切换到默认页面、主页面
    #         pass
    #
    #     pass
    #
    # def click(self):
    #     pass
    #
    # def sendkeys(self):
    #     pass



