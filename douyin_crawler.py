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

    def get_opus(self, user_name, user_id, max_cursor):
        if not os.path.exists(user_name):
            os.mkdir(user_name)
        opus_url = self.config.get_opus_url()
        cookie = self.config.get_cookie()
        headers = {'Host': self.__DOUYIN_HOST, 'cookie': cookie}
        aid = self.config.get_aid()
        params = {'aid': aid, 'sec_user_id': user_id, 'count': 18, 'max_cursor': max_cursor}
        response = requests.get(url=opus_url, headers=headers, params=params)
        if response.status_code == 200:
            print(response.text)
            return json.loads(response.text)
        else:
            print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def get_user_opus(self, user_name, user_id):
        opus = []
        r = self.get_opus(user_name, user_id, 0)
        aweme_list = r.get('aweme_list')
        opus.extend(aweme_list)
        max_cursor = r.get('max_cursor')
        request_item_cursor = r.get('request_item_cursor')
        time_list = r.get('time_list')
        while (aweme_list != None and len(aweme_list) > 0):
            r = self.get_opus(user_name, user_id, max_cursor)
            aweme_list = r.get('aweme_list')
            opus.extend(aweme_list)
            max_cursor = r.get('max_cursor')
        return opus

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
                with open(desc + video_id + '.mp4', 'wb') as f:
                    f.write(response.content)
            else:
                print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def down_target_user(self, user_name, user_id):
        opus = self.get_user_opus(user_name, user_id)
        for o in opus:
            video_id = o.get('aweme_id')
            desc = o.get('desc')

    def down_fwllowings(self):
        fellowings = self.get_followings()
        for fellowing in fellowings:
            print(fellowing)
