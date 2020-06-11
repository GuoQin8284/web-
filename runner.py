import os
import unittest

from Tools.HTMLTestRunner import HTMLTestRunner
from action.CreateDir import create_dir
from config import BASE_DIR


# suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_login"))

# runner = unittest.TextTestRunner()
# runner.run(loader)
# 哈哈哈

loader = unittest.TestLoader().discover(start_dir="./scripts", pattern="test*.py")
file= BASE_DIR + os.sep + "report"+os.sep+"osid测试报告.html"
create_dir(file)
with open(file, mode="wb") as f:
    runner = HTMLTestRunner(stream=f, title="osid作者端登录模块自动化测试报告", description="chrome版本 83.0.4103.97（正式版本） （64 位）")
    runner.run(loader)



