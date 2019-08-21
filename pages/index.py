# _*_ coding:utf-8 _*_
# @time     :  15:53
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : index.py
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.base import BasePage


class IndexPage(BasePage):
    '''首页类'''
    #标的元素
    bid_locator=(By.XPATH, "//div[text()='12%']//parent::div//following-sibling::a")
    #
    # def __init__(self,driver):
    #     self.driver=driver

    def get_user_info(self):
        '''获取首页的用户信息'''
        user_ele = WebDriverWait(self.driver, 30).until(
            ec.presence_of_element_located((By.XPATH, '//a[@href="/Member/index.html"]')))
        return  user_ele

    def choose_bid(self):
        '''选择标的'''
        #定位投标按钮
        ele=self.wait_clickable_element(self.bid_locator)
        #点击投标
        return ele.click()
