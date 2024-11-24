import os

import requests
import json
from lxml import etree
from douyin_config import DouyinConfig


class DouyinCrawler:

    def __init__(self):
        self.__DOUYIN_HOST = 'www.douyin.com'
        self.config = DouyinConfig()

    def get_followings(self):
        followings_url = self.config.get_followings_url()
        cookie = self.config.get_cookie()
        headers = {'cookie': cookie}
        sec_user_id, aid = self.config.get_params()
        params = {'aid': aid, 'sec_user_id': sec_user_id}
        response = requests.get(url=followings_url, headers=headers, params=params)
        if response.status_code == 200:
            return json.loads(response.text).get('followings')
        else:
            print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def get_opus(self, user_name, user_id):
        os.mkdir(user_name)
        opus_url = self.config.get_opus_url()
        cookie = self.config.get_cookie()
        headers = {'Host': self.__DOUYIN_HOST, 'cookie': cookie}
        aid = self.config.get_aid()
        params = {'aid': aid, 'sec_user_id': user_id, 'count': 18}
        response = requests.get(url=opus_url, headers=headers, params=params)
        if response.status_code == 200:
            print(response.text)
            return json.loads(response.text).get('aweme_list')
        else:
            print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def download_video(self, video_id, download_cookie, desc):
        play_url = self.config.get_play_url()
        headers = {'Host': self.__DOUYIN_HOST, 'cookie': download_cookie}
        params = {'video_id': video_id}
        response = requests.get(play_url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 302:
            htmldata = etree.HTML(response.content)
            real_url = htmldata.xpath('//a/@href')
            headers = {'Host': 'v18-daily-coldb.douyinvod.com'}
            response = requests.get(real_url[0], headers=headers)
            if response.status_code == 200:
                with open(desc + '.mp4', 'wb') as f:
                    f.write(response.content)
            else:
                print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def _build_header(self):
        pass
