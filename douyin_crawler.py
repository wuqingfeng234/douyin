import os
from urllib.parse import urlparse

import requests
import json
from lxml import etree
from douyin_config import DouyinConfig


class DouyinCrawler:

    def __init__(self):
        self.__DOUYIN_HOST = 'www.douyin.com'
        self.config = DouyinConfig()

    def get_followings_info(self):
        followings_url = self.config.get_followings_url()
        cookie = self.config.get_cookie()
        headers = {'cookie': cookie
            ,
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                   }
        response = requests.get(url=followings_url, headers=headers)
        print(response.request.url)
        print(response.request.headers)
        if response.status_code == 200 and json.loads(response.text).get('status_code') == 0:
            return json.loads(response.text).get('followings')
        else:
            print("get_fellow error, status is {} ,code is {} .".format(response.status_code, response.text))

    def get_user_opus_info(self, user_name, user_id, max_cursor):
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

    def get_user_opus_infos(self, user_name, user_id):
        opus = []
        r = self.get_user_opus_info(user_name, user_id, 0)
        aweme_list = r.get('aweme_list')
        opus.extend(aweme_list)
        max_cursor = r.get('max_cursor')
        request_item_cursor = r.get('request_item_cursor')
        time_list = r.get('time_list')
        while (aweme_list != None and len(aweme_list) > 0):
            r = self.get_user_opus_info(user_name, user_id, max_cursor)
            aweme_list = r.get('aweme_list')
            opus.extend(aweme_list)
            max_cursor = r.get('max_cursor')
        return opus

    def download_video(self, video_id, desc):
        play_url = self.config.get_play_url()
        download_cookie = self.config.get_cookie()
        headers = {'Host': self.__DOUYIN_HOST,
                   'cookie': download_cookie,
                   'Accept-Encoding': 'gzip, deflate',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
        params = {'video_id': video_id}
        response = requests.get(play_url, headers=headers, params=params, allow_redirects=False)
        if response.status_code == 200 and len(response.content) > 10:
            with open(desc + video_id + '.mp4', 'wb') as f:
                f.write(response.content)
        elif response.status_code == 302:
            htmldata = etree.HTML(response.content)
            real_url = htmldata.xpath('//a/@href')[0]
            o = urlparse(real_url)
            headers = {'Host': o.hostname,
                       'Accept': '*/*',
                       'Connection': 'keep-alive',
                       'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                       }
            response = requests.get(real_url, headers=headers)
            print(response.request.url)
            print(response.request.headers)
            print(response.request.path_url)
            print(response.request.body)
            if response.status_code == 200:
                with open(desc + video_id + '.mp4', 'wb') as f:
                    f.write(response.content)
            else:
                print("download video error, status is {} ,code is {} .".format(response.status_code, response.text))
        else:
            print("download video error, status is {} ,code is {} .".format(response.status_code, response.text))

    def down_target_user_video(self, user_name, user_id):
        opus = self.get_user_opus_infos(user_name, user_id)
        for o in opus:
            video_id = o.get("video").get("play_addr").get("uri")
            url = o.get("video").get("play_addr").get("url_list")[0]
            desc = o.get('desc')
            self.download_video(video_id, desc)

    def down_fellowings_video(self):
        fellowings = self.get_followings_info()
        for fellowing in fellowings:
            print(fellowing)
