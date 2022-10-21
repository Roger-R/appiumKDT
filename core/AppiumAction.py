from appium import webdriver
import time


class AppiumKeyWords:
    """

    """
    # init with configs
    def __init__(self,config):
        self.config = config

    def start(self,url):
        self.driver = webdriver.Remote(url, self.config)
        return self.driver

    def implicitily(self,sec):
        self.driver.implicitly_wait(sec)

    def element(self,by,path):
        by = by.lower()
        if by =="uiautomator":
            ele = self.driver.find_element_by_android_uiautomator(path)
        else:
            ele = self.driver.find_element(by,path)
        return ele

    def elements(self,by,path,index):
        by = by.lower()
        if by=="uiautomator":
            eles = self.driver.find_elements_by_android_uiautomator(path)
        else:
            eles = self.driver.find_elements(by,path)
        ele = eles[index]
        return ele

    def clickSingle(self,by,path):
        ele = self.element(by, path)
        ele.click()

    def click(self,by,path,index):
        if index is None:
            self.clickSingle(by,path)
        else:
            ele = self.elements(by,path,index)
            ele.click()

    def sleep(self,sec):
        time.sleep(sec)

    def swipe(self,x1,y1,x2,y2):
        self.driver.swipe(x1,y1,x2,y2,5000)
