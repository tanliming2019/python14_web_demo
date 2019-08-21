# _*_ coding:utf-8 _*_
# @time     :  0:09
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : test_yield.py
import pytest


@pytest.fixture()
def init_web():
    print('初始化浏览器')

    yield

    print('退出浏览器')


@pytest.fixture(scope='class')
def class_web():
    print('class before')

    yield

    print('class after')


@pytest.fixture(scope='module')
def module_web():
    print('module before')

    yield

    print('module after')

@pytest.fixture(scope='session')
def session_web():
    print('session before')

    yield

    print('session after')


class TestA:

    @pytest.mark.q
    def test_demo(self,init_web,class_web,module_web,session_web):
        print('执行测试用例')

    @pytest.mark.q
    def test_1_demo(self,init_web,class_web,module_web,session_web):
        print('执行测试用例2')

class TestB:

    @pytest.mark.q
    def test_3demo(self,init_web,class_web,module_web,session_web):
        print('执行测试用例3')