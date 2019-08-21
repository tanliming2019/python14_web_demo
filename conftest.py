# _*_ coding:utf-8 _*_
# @time     :  0:35
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : conftest.py
from selenium.webdriver import Chrome
import pytest

from common.my_log import ReadLogging
from pages.bid import BidPage
from pages.login import LoginPage
my_log=ReadLogging()

@pytest.fixture(scope='class')
def class_web():
    '''初始化浏览器'''
    driver=Chrome()
    login_page=LoginPage(driver)


    yield driver,login_page

    driver.quit()


@pytest.fixture(scope='class')
def class_web2():
    '''初始化浏览器并登陆'''
    driver = Chrome()
    login_page = LoginPage(driver)
    login_page.login("18684720553","python")
    bid_page=BidPage(driver)

    yield driver,bid_page

    driver.quit()


@pytest.fixture()
def founction_web():
    '''测试提示'''
    my_log.info('-----测试开始----')

    yield

    my_log.info('-----测试结束----')