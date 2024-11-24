import unittest

from douyin_config import DouyinConfig


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)  # add assertion here

    def test_get_params(self):
        douyin_config = DouyinConfig()
        sec_user_id, aid = douyin_config.get_params()
        print("sec_user_id is {} ,aid is {} .".format(sec_user_id, aid))


if __name__ == '__main__':
    unittest.main()
