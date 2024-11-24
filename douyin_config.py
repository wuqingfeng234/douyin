import configparser
import os


class DouyinConfig(object):
    def __init__(self):
        self.parser = configparser.RawConfigParser()
        self.parser.read(os.path.join(os.getcwd(), 'douyin_config.ini'), 'utf-8-sig')

    def get_params(self):
        sec_user_id = self.parser.get('params', 'sec_user_id')
        aid = self.parser.get('params', 'aid')
        return sec_user_id, aid

    def get_aid(self):
        aid = self.parser.get('params', 'aid')
        return aid

    def get_cookie(self):
        cookie = self.parser.get('headers', 'cookie')
        return cookie

    def get_followings_url(self):
        return self.parser.get('urls', 'fellow_url')

    def get_opus_url(self):
        return self.parser.get('urls', 'opus_url')

    def get_play_url(self):
        return self.parser.get('urls', 'play_url')
