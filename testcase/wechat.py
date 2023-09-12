# -*- coding: utf-8 -*-
"""
@Time ： 2023/9/12 23:18
@Author ： kangmingxiao
"""

from base.driver import U2Driver

class Wechat(U2Driver):
    def run(self):
        self.setup()
        self.test_case()

    def setup(self):
        self.d.app_stop(self.package)
        self.d.app_start(self.package)
        self.d.implicitly_wait(30)

    def test_case(self):
        self.logger.info(f"打开{self.package}中")
        self.d.swipe(500,1800,500,1000)

if __name__ == '__main__':
    test=Wechat("emulator-5554","com.tencent.mm")
    test.run()

