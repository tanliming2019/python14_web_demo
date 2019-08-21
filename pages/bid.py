# _*_ coding:utf-8 _*_
# @time     :  17:37
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : bid.py

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import login_locators
from pages.base import BasePage


class BidPage(BasePage):
    '''投资页面'''
    #投资输入框
    bid_input_locator=(By.XPATH, "//input[@class='form-control invest-unit-investinput']")
    #投标按钮
    bid_submit_locator=(By.XPATH, "//button[@class='btn btn-special height_style']")
    #查看并激活按钮
    alert_active_locator=(By.XPATH, "//div[@class='layui-layer-content']//button[text()='查看并激活']")

    def get_bid_input_element(self):
        '''定位投资输入框'''
        return self.wait_presence_element(self.bid_input_locator)

    def click_bid_submit(self):
        '''点击投标按钮'''
        e=self.wait_clickable_element(self.bid_submit_locator)
        e.click()

    def click_alert(self):
        '''点击查看并激活按钮'''
        e=self.wait_clickable_element(self.alert_active_locator)
        e.click()


