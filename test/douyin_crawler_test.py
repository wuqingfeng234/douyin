import unittest

from douyin_crawler import DouyinCrawler


class DouyinCrawlerTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_get_fellow(self):
        crawler = DouyinCrawler()
        crawler.get_followings()


if __name__ == '__main__':
    unittest.main()
