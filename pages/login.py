# _*_ coding:utf-8 _*_
# @time     :  2:23
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : login.py

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from pages.locators import login_locators
from pages.base import BasePage

class LoginPage(BasePage):
    '''登录页面'''
    url = 'http://120.78.128.25:8765/Index/login.html'

    #
    # def __init__(self,driver):
    #     self.driver=driver



    def login(self,username, pwd):
        '''登录'''
        # 1.打开浏览器open_browser
        # driver = Chrome()

        # 2.访问登录页面visit_login_page
        self.driver.get(self.url)

        # 3.定位元素 find_element   用户输入框  密码输入框
        use_ele=self.get_user_info()
        pwd_ele=self.get_pwd_info()

        # 4.发送用户密码，提交 submit
        use_ele.send_keys(username)
        pwd_ele.send_keys(pwd)
        use_ele.submit()
        return self.driver

    def get_flash_info(self):
        '''获取错误信息'''
        flash_info=WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.form-error-info')))
        return flash_info

    def get_unauth_info(self):
        '''获取没授权信息'''
        unauth_info = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, '.layui-layer-content')))
        return unauth_info

    def clear_user_info(self):
        '''清空用户数据'''
        self.clear_username()
        self.clear_pwd()

    def clear_username(self):
        '''清空用户名'''
        #定位 get_username()
        return self.get_user_info().clear()

    def clear_pwd(self):
        '''清空密码'''
        return self.get_pwd_info().clear()


    def get_user_info(self):
        '''定位用户名'''
        use_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(login_locators.usename_locator))
        return use_ele

    def get_pwd_info(self):
        '''定位密码'''
        pwd_ele = WebDriverWait(self.driver, 20).until(
            ec.presence_of_element_located(login_locators.pwd_locator))
        return pwd_ele







