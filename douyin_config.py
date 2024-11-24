import configparser
import os


class DouyinConfig(object):
    def __init__(self):
        self.parser = configparser.ConfigParser()
        self.parser.read(os.path.join(os.getcwd(), 'douyin_config.ini'), 'utf-8-sig')

    def get_params(self):
        sec_user_id = self.parser.get('params', 'sec_user_id')
        aid = self.parser.get('params', 'aid')
        return sec_user_id, aid

    def get_headers(self):
        host = self.parser.get('headers', 'host')
        cookie = self.parser.get('headers', 'cookie')
        return host, cookie
