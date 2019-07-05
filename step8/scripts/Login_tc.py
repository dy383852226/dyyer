import unittest
import sys
from libs.Base_work import admin_login
from po.Login_page import LoginPage
from po.MemberCenter.TeacherListPage import TeacherListPage
from po.MemberCenter.TeacherList.AddTeacherPage import AddTeacherPage

class LoginTest(unittest.TestCase):

    def setUp(self):
        self.obj = LoginPage()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_browser()

    def test_login_success_001(self):
        self.obj.login_operator('admin','admin')
        r = self.obj.get_success_msg()
        self.assertEqual(r,'admin')

    def test_login_error_001(self):
        self.obj.login_operator('', 'admin')
        r = self.obj.get_username_error_msg()
        self.assertEqual(r,'账号或密码不能为空')
