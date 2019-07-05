import unittest
import sys
from libs.Base_work import admin_login
from po.MemberCenter.TeacherListPage import TeacherListPage
from po.MemberCenter.TeacherList.AddTeacherPage import AddTeacherPage


class AddStudentTest(unittest.TestCase):
    '''添加学生功能测试'''

    def setUp(self):
        # 传入driver解决问题
        # 首次实例化父类的Driver在Admin login
        self.dv = admin_login()
        self.obj_sp = TeacherListPage(self.dv)
        self.obj_ap = AddTeacherPage(self.dv)
    #
    def tearDown(self):
        self.obj_ap.close_browser()

    def addTeacherData(self):
        self.obj_sp.optionInTeacherList()
        self.obj_ap.optionAddTeacher('13800000094', 'hahaha', '12345678', 'aaa@163.com', '13902455555', 'hahaha','whoami')
        result = self.obj_ap.optionVerifyData()
        return result

    def test_addTeacher_success(self):
        '''成功添加教师账号测试'''
        result = self.addTeacherData()
        self.assertEqual(result, '13800000094')

if __name__ == '__main__':
    unittest.main(verbosity=2)
