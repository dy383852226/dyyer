from libs.Tools import create__browser_driver
from config.Secert import edu_url


class Page(object):

    def __init__(self, driver=''):

        b = driver
        if b == '':
            self.dv = create__browser_driver()
        else:
            self.dv = b
        self.dv.maximize_window()
        self.dv.implicitly_wait(10)

    def open_url(self, url=edu_url):
        self.dv.get(url)

    def close_browser(self):
        self.dv.close()
