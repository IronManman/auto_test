# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/12 23:10
@Author ： kangmingxiao
"""
from base.log import BaseLog
import time
import uiautomator2 as u2

class U2Driver(BaseLog):
    def __init__(self,device_id,package):
        BaseLog.__init__(self)
        self.d=u2.connect(device_id)
        self.package=package

    def by_id(self,eid):
        self.d(resourceId=eid).click()

    def by_xpath(self,expath):
        self.d.xpath(expath).click()

