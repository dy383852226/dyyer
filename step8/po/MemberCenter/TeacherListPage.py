from po.Common_page import Page
from selenium.webdriver.common.by import By


class TeacherListPage(Page):
    """教师列表页面"""

    # 对象层
    btn_menbercenter_loc = (By.LINK_TEXT, '会员中心')
    lnk_studentlist_loc = (By.LINK_TEXT, '教师列表')
    iframe_main_loc = (By.ID, 'mainframe')

    # 操作层
    # 点击会员中心
    def clickMemberCenterButton(self):
        self.dv.find_element(*self.btn_menbercenter_loc).click()

    # 点击教师列表
    def clickTeacherListLink(self):
        self.dv.find_element(*self.lnk_studentlist_loc).click()

    # 进入教师Iframe框
    def changeTeacherFrame(self):
        # 点击教师列表
        self.dv.find_element_by_link_text('教师列表').click()
        # 切入Iframe框操作教师列表里面的内容
        ele = self.dv.find_element(*self.iframe_main_loc)
        self.dv.switch_to.frame(ele)

    # 回到上一层
    def change_main_frame(self):
        self.dv.switch_to.default_content()

    # 业务层
    # 进入教师列表
    def optionInTeacherList(self):
        self.clickMemberCenterButton()
        self.clickTeacherListLink()
        self.changeTeacherFrame()


if __name__ == "__main__":
    pass
