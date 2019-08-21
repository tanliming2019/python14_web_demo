#!/usr/bin/env python3
#-*- coding:utf-8 -*-
# author:muji
# datetime:2019/5/13 20:59
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
import pytest




if __name__ == '__main__':
    pytest.main(["-m success -s", r"--html=report\test.html",r"--alluredir=report\allure"])