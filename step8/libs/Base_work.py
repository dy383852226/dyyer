# coding:utf-8
from po.Login_page import LoginPage
from selenium import  webdriver



def admin_login(UserName='admin',PassWord='admin'):
    # 首次实例化父类的Driver在Admin login
    obj = LoginPage()
    obj.open_url()
    obj.dv.implicitly_wait(10)
    obj.set_username(UserName)
    obj.set_password(PassWord)
    obj.click_login_button()
    return obj.dv

if __name__ == "__main__":
    admin_login('admin','admin')


