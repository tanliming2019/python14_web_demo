# _*_ coding:utf-8 _*_
# @time     :  20:09
# @Author   : lemon_Liming
# @Email    : 1104197970@qq.com
# @File     : login.py

#数据 1.账号  2.密码  3.预期结果

#测试用例分组
#用户分组依据：测试用例逻辑方法步骤是否发生变化

user_info_success={"username":"18684720553","pwd":"python","expected":"python10"}

user_info_error=[
    ({"username":""},{"pwd":""},{"expected":"请输入手机号"}),
    ({"username":"12"},{"pwd":""},{"expected":"请输入正确的手机号"}),
    ({"username":"18654321456"},{"pwd":""},{"expected":"请输入密码"})]

# user_info_error=[("","","请输入手机号"),("18654321456","","请输入密码"),("12","","请输入正确的手机号")]


user_info_authorize={"username":"18654321454","pwd":"12","expected":"此账号没有经过授权，请联系管理员!"}
