import pymysql
import yagmail
import os
from selenium import webdriver

# 配置浏览器类型
bs = 'gc'
def create__browser_driver(b=bs):
    try:
        if b == 'gc':
            dv = webdriver.Chrome()
        elif b == 'ff':
            dv = webdriver.Firefox()
        elif b == 'ie':
            dv = webdriver.Ie()
        else:
            pass
        return dv
    except BaseException:
        pass

# 数据库的操作
def read_mysql_data(host,port,user,pwd,db,sql):
    # 建立sql连接对象
    conn = pymysql.connect(host=host, port=port, user=user, password=pwd, db=db)
    # 生成游标对象
    cur = conn.cursor()
    # 执行sql语句
    cur.execute(sql)
    # 关闭游标
    cur.close()
    # 关闭数据库
    conn.close()
    # 查询sql结果
    data = cur.fetchone()
    return data

# 发送邮件
def send_email(user,pwd,port,body,subject,report,to_user,host='smtp.163.com',):
    '''
    :param user:
    :param pwd:
    :param port:
    :param body:
    :param subject:
    :param report:
    :param to_user: 接受者账号，默认是字符串，如果传多个请用列表的方式传递
    :param host:
    :return:
    '''
    # 生成发送对象
    send = yagmail.SMTP(user=user, password=pwd, host=host, port=port)
    if type(to_user) is list:
        # 发送邮件
        send.send(to=to_user,subject=subject,contents=[body,report])
        flag = '发送给批量用户成功'
    elif type(to_user) is str:
        # 发送邮件
        send.send(to=to_user,subject=subject,contents=[body,report])
        flag = '发送给单个用户成功'
    else:
        flag = '发送数据错误'
    return flag

FD = "./reports"


def GetNewReport(FileDir=FD):
    # 打印目录所在所有文件名（列表对象）
    l = os.listdir(FileDir)
    # 按时间排序
    l.sort(key=lambda fn: os.path.getmtime(FileDir + "\\" + fn))
    # 获取最新的文件保存到file_new
    f = os.path.join(FileDir, l[-1])
    return f

if __name__ == '__main__':
    pass
