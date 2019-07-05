# coding:utf-8
import time
import copy
import unittest
from HTMLTestReportCN import HTMLTestRunner
from libs.Tools import (
    send_email,
    GetNewReport
)
from config.Secert import (
    email_account,
    email_host,
    email_port,
    email_pwd,
    email_to_account,
)


def run_test():
    dirpath = './scripts'
    discover = unittest.defaultTestLoader.discover(dirpath, pattern='*_tc.py')
    currenttime = time.strftime('%y%m%d%H%M%S')
    filedir = './reports/' + 'report_' + currenttime + '.html'
    with open(filedir, 'wb') as fp:
        runner = HTMLTestRunner(stream=fp,
                                title='Edu自动化测试报告',
                                description='Edu在线教育平台V1.2自动化测试报告',
                                tester="测试大神", verbosity=2)
        runner.run(discover)
    f = GetNewReport()
    send_email(user=email_account,pwd=email_pwd,host=email_host,port=email_port,to_user=email_to_account,
               subject='自动化测试报告',body='老板这是今天的自动化报告，麻烦看看',report=f)
    print('发送邮件成功')


if __name__ == '__main__':
    run_test()
