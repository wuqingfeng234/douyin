import datetime
import os
import random
import logging
from time import sleep
from urllib.parse import urlparse

import requests
import json
from lxml import etree

from file_checker import FileChecker
from douyin_config import DouyinConfig


class DouyinCrawler:

    def __init__(self):
        self.__DOUYIN_HOST = 'www.douyin.com'
        self.config = DouyinConfig()
        self.file_checker = FileChecker()

    def get_followings_info(self, user_id):
        followings_url = self.config.get_followings_url()
        cookie = self.config.get_cookie()
        headers = {'cookie': cookie
            ,
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
                   }
        response = requests.get(url=followings_url, headers=headers)
        if response.status_code == 200 and json.loads(response.text).get('status_code') == 0:
            with open("../data/fellowing.json", "w", encoding='utf-8') as of:
                of.writelines(response.text)
            return json.loads(response.text).get('followings')
        else:
            print("{} get_fellow error, status is {} ,code is {} .".format(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), response.status_code,
                response.text))

    def get_user_opus_info(self, user_name, user_id, max_cursor):
        opus_url = self.config.get_opus_url()
        cookie = self.config.get_cookie()
        headers = {'Host': self.__DOUYIN_HOST, 'cookie': cookie}
        aid = self.config.get_aid()
        params = {'aid': aid, 'sec_user_id': user_id, 'count': 18, 'max_cursor': max_cursor}
        response = requests.get(url=opus_url, headers=headers, params=params)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            logging.error("{} get_fellow error, status is {} ,code is {} .".format(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), response.status_code,
                response.text))

    def get_user_opus_infos(self, user_name, user_id):
        opus = []
        r = self.get_user_opus_info(user_name, user_id, 0)
        aweme_list = r.get('aweme_list')
        opus.extend(aweme_list)
        max_cursor = r.get('max_cursor')
        request_item_cursor = r.get('request_item_cursor')
        time_list = r.get('time_list')
        folder_path = os.path.join(os.getcwd(), "video", user_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)
        while aweme_list is not None and len(aweme_list) > 0:
            r = self.get_user_opus_info(user_name, user_id, max_cursor)
            aweme_list = r.get('aweme_list')
            opus.extend(aweme_list)
            max_cursor = r.get('max_cursor')
        return opus

    def download_video(self, user_name, video_id, desc):
        play_url = self.config.get_play_url()
        download_cookie = self.config.get_cookie()
        headers = {'Host': self.__DOUYIN_HOST,
                   'cookie': download_cookie,
                   'Accept-Encoding': 'gzip, deflate',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'}
        params = {'video_id': video_id}
        response = requests.get(play_url, headers=headers, params=params, allow_redirects=False)
        path = os.path.join(os.getcwd(), "video", user_name, desc + video_id + '.mp4')
        if response.status_code == 200 and len(response.content) > 10:
            with open(path, 'wb') as f:
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
            if response.status_code == 200:
                with open(path, 'wb') as f:
                    f.write(response.content)
                logging.info("{} down load video from user {},video name {} ,video id {}  successfully .".format(
                    datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), user_name, desc,
                    video_id))
                self.file_checker.set_exsited_video(video_id)
            else:
                logging.error("{} download video error, status is {} ,code is {} .".format(
                    datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), response.status_code,
                    response.text))
                logging.error("{} down load video from user {},video name {} ,video id {}  failed .".format(
                    datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), user_name, desc,
                    video_id))
        else:
            logging.error("{} download video error, status is {} ,code is {} .".format(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), response.status_code,
                response.text))
            logging.error("{} down load video from user {},video name {} ,video id {}  failed .".format(
                datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), user_name, desc,
                video_id))

    def down_target_user_video(self, user_name, user_id):
        opus = self.get_user_opus_infos(user_name, user_id)
        for o in opus:
            video_id = o.get("video").get("play_addr").get("uri")
            desc = o.get('desc')
            if not self.file_checker.is_video_exsits(video_id):
                try:
                    self.download_video(user_name, video_id, desc)
                except Exception as e:
                    logging.error("{} down load video from user {},video name {} ,video id {}  error ,except is {} .".format(
                        datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), user_name, desc,
                        video_id, e))
                    sleep(2 * random.random())
            else:
                logging.info(
                    "{} video {} from user {} exsited ,will not down load any more .".format(
                        datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'), video_id,
                        user_name))

    def down_fellowings_video(self, user_id):
        fellowings = self.get_followings_info(user_id)
        for fellowing in fellowings:
            name = fellowing.get('nickname')
            user_id = fellowing.get('sec_uid')
            if not self.file_checker.is_people_exclude(user_id):
                self.down_target_user_video(name, user_id)
