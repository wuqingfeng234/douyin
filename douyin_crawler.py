import requests
import json

from douyin_config import DouyinConfig


class DouyinCrawler:
    _DOUYIN_HOST = 'www.douyin.com'

    def __init__(self):
        self.config = DouyinConfig()

    def get_followings(self):
        followings_url = self.config.get_followings_url()
        cookie = self.config.get_cookie()
        headers = {'cookie': cookie}
        sec_user_id, aid = self.config.get_params()
        params = {'aid': aid, 'sec_user_id': sec_user_id}
        response = requests.get(url=followings_url, headers=headers, params=params)
        if response.status_code == 200:
            print(response.content)
            return json.loads(response.text).get('followings')
        else:
            print("get_fellow error, detail is {} .".format(response))

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

    def _build_header(self):
        pass
