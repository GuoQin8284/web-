import unittest

from Tools.HTMLTestRunner import HTMLTestRunner
from config import BASE_DIR
from scripts.test_login import TestLogin

# suite = unittest.TestSuite()
# suite.addTest(TestLogin("test_login"))

# runner = unittest.TextTestRunner()
# runner.run(loader)

loader = unittest.TestLoader().discover(start_dir="./scripts", pattern="test*.py")

with open(file=BASE_DIR+"./report/osid测试报告.html", mode="wb") as f:
    runner = HTMLTestRunner(stream=f, title="osid作者端登录模块自动化测试报告", description="chrome版本 83.0.4103.97（正式版本） （64 位）")
    runner.run(loader)



