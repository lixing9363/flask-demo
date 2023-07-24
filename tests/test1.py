import os
import unittest

from apps import create_app


class TestConfig(unittest.TestCase):

    # setUp()方法会在每个测试方法之前执行,用于进行测试用例的初始化工作。
    def setUp(self):
        self.app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        self.app_context = self.app.app_context()
        self.app_context.push()

    # tearDown()方法会在每个测试方法之后执行,用于测试后环境的清理。
    def tearDown(self):
        self.app_context.pop()

    def test_app_exists(self):
        app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        with app.app_context():
            print("test111111111111")

    def test_app_exists2(self):
        app = create_app(os.getenv('FLASK_CONFIG') or 'default')
        with app.app_context():
            print("test222222222222")


if __name__ == '__main__':
    unittest.main()
