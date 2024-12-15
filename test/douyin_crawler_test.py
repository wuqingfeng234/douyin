import unittest
from bisect import insort

from douyin_crawler import DouyinCrawler


class DouyinCrawlerTest(unittest.TestCase):

    def test_get_followings(self):
        crawler = DouyinCrawler()
        fellowings = crawler.get_followings_info()
        print(fellowings)

    def test_get_usrtopus(self):
        crawler = DouyinCrawler()
        user_name = '痞欠'
        user_id = 'MS4wLjABAAAAMIYFdK1YjoSpqH9-koTw5QUk2BKgESsOnNZiQLJVbD8'
        info = crawler.get_user_opus_info(user_name, user_id, 0)

    def test_get_user_opus_infos(self):
        crawler = DouyinCrawler()
        user_name = '小李成绩特别好'
        user_id = 'MS4wLjABAAAAk51Pb5d8EMJcIKuVutaVCUc8maIfCpRE883bIVHQ0XY'
        infos = crawler.get_user_opus_infos(user_name, user_id)
        print(infos)

    def test_get_user_opus_infos_mine(self):
        crawler = DouyinCrawler()
        user_name = '青春热舞'
        user_id = 'MS4wLjABAAAAl_9zTWpxneEZC3Tn0hKbczqHNM3IZ_io7yUgepTIbgY'
        infos = crawler.get_user_opus_infos(user_name, user_id)
        print(infos)

    def test_download_video(self):
        crawler = DouyinCrawler()
        video_id = 'v0200fg10000ct1cdfnog65p3378l60g'
        desc = '#天生丽质 #极品身材 #叶凯薇'
        crawler.download_video('test',video_id, desc)

    def test_down_target_user(self):
        crawler = DouyinCrawler()
        crawler.down_target_user_video('青春热舞', 'MS4wLjABAAAAl_9zTWpxneEZC3Tn0hKbczqHNM3IZ_io7yUgepTIbgY')

    def test_down_target_user2(self):
        crawler = DouyinCrawler()
        crawler.down_target_user_video('你的灵儿吖', 'MS4wLjABAAAAhKlSnJS5yJ0QCuAQyjAHpxJbeEXYh3DJZQZnfXFoxDg')


if __name__ == '__main__':
    unittest.main()
