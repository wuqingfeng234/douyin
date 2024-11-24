import requests
import json


class DouyinCrawler:
    def __init__(self):
        self.header = None

    def get_fellow(self):
        fellow_url = 'https://www.douyin.com/aweme/v1/web/im/spotlight/relation/'
        req = requests.get(url=fellow_url, verify=False)
        pass

    def get_opus(self):
        pass

    def download_video(self, url, name):
        if not url:
            return
        try:
            r = requests.get(url, headers=self.headers)
            with open(name + '.mp4', 'wb') as f:
                f.write(r.content)
            print("下载完成")

        except Exception as e:
            print("下载失败")
            print(e)
