import unittest

from douyin_crawler import DouyinCrawler


class DouyinCrawlerTest(unittest.TestCase):

    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_get_followings(self):
        crawler = DouyinCrawler()
        fellowings = crawler.get_followings()
        print(fellowings)

    def test_get_opus(self):
        crawler = DouyinCrawler()
        user_name = '妙仙亭'
        user_id = 'MS4wLjABAAAAm83Y8scMOFZ3iUpy8_3RX2fwlvmgfBYnjm-decoxACU'
        crawler.get_opus(user_name, user_id, 0)

    def test_get_user_opus(self):
        crawler = DouyinCrawler()
        user_name = '妙仙亭'
        user_id = 'MS4wLjABAAAAm83Y8scMOFZ3iUpy8_3RX2fwlvmgfBYnjm-decoxACU'
        crawler.get_user_opus(user_name, user_id)

    def test_download_video(self):
        crawler = DouyinCrawler()
        video_id = 'v0200fg10000ct1cdfnog65p3378l60g'
        download_cookie = 'UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d11217ec76064fda798e6d749bbc21c30162b5365958250c1a4abdb4a37d90fd6b040df76b7fa36f7397d3506e4bc6775e10; s_v_web_id=verify_m35udnia_ovcb7ZpF_OmDv_4YJ6_ALtQ_sEcgUMApgYAd; hevc_supported=true; xgplayer_user_id=526950803128; passport_csrf_token=4ad5e33ef3c5418537a952cc7d4bb19b; passport_csrf_token_default=4ad5e33ef3c5418537a952cc7d4bb19b; fpk1=U2FsdGVkX189oJ+2X3zCIHI0/bEj4vGuxhOpI/mVs03gaIzv2PSq5wLLNqK0tEk0ORVPbvBvJkyGnV2iSU/G+g==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; bd_ticket_guard_client_web_domain=2; passport_mfa_token=Cjc27c8bm0vTM0fn6qsqoCZFPUvZfkfbvUxU65anO5q4B5wpxXg80djsaqBQuHhVLShv4kAeBKofGkoKPCwWbJmvrwCCI8UGLJGcDGHHxDKdQUvWINak6UJzkTxZm%2B5ZaAbygyaAwRyCs79yIqWfvub2MfMaVMs0GRCC4eANGPax0WwgAiIBA0CAUoc%3D; d_ticket=18d5c7746d146edf4aaa7bcb70f8a27e0428f; passport_assist_user=CkCWTBkWYPeJ4BTNZTIzBplblFH3BPV9nCpLBE1LDFGOprPRT3uTb_CQuIiWfEHlwg0MjVdE2LL1jgU6n8HWTa9JGkoKPBgBr_xFkp25meKzWD8bi_Z-racq-yk3ztc0s0apJd0YqqSy59x7KlUjVCiWidbPesHKRokuQmL7PTWqSxDm3-ANGImv1lQgASIBA1EEYEA%3D; n_mh=TioMYmRh9AnfFCGzXPq1EHhasDHjipuiqLODHIk2pvA; sso_uid_tt=a0c072ff4999838adbcdb9fc796a969f; sso_uid_tt_ss=a0c072ff4999838adbcdb9fc796a969f; toutiao_sso_user=86e78d0a781db61dbcdc5842f6590d82; toutiao_sso_user_ss=86e78d0a781db61dbcdc5842f6590d82; sid_ucp_sso_v1=1.0.0-KDIzNzE0YzBiYjk2MTBiYTA1ZDlhZWJhNWUxN2YzNWU1OWJiNTJhMTgKIQiEx_CN0s2eARCpvq25BhjvMSAMMJW4yK4GOAZA9AdIBhoCaGwiIDg2ZTc4ZDBhNzgxZGI2MWRiY2RjNTg0MmY2NTkwZDgy; ssid_ucp_sso_v1=1.0.0-KDIzNzE0YzBiYjk2MTBiYTA1ZDlhZWJhNWUxN2YzNWU1OWJiNTJhMTgKIQiEx_CN0s2eARCpvq25BhjvMSAMMJW4yK4GOAZA9AdIBhoCaGwiIDg2ZTc4ZDBhNzgxZGI2MWRiY2RjNTg0MmY2NTkwZDgy; login_time=1730895660295; passport_auth_status=a5c0f98c45f9d57e4966401627a7d187%2C; passport_auth_status_ss=a5c0f98c45f9d57e4966401627a7d187%2C; uid_tt=c136fae79f289b5557fabfdd848a3e7f; uid_tt_ss=c136fae79f289b5557fabfdd848a3e7f; sid_tt=a930836a69bbeea6f41e3ea82940a48c; sessionid=a930836a69bbeea6f41e3ea82940a48c; sessionid_ss=a930836a69bbeea6f41e3ea82940a48c; is_staff_user=false; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d11217ec76064fda798e6d749bbc21c30162a090656dc186a97b088699a5f5ee93f70e38d7c5cf111826a1bdee94169a82fbea066b38da81279256b17101ed43440a52a4d2fb5fafb9bd3926f802ccd18190f018e2af241e24ee71a0edabe301eb09053d4f2a47a8b591bf532776c8e55b25adef22f6964df8a6832101bc60980d5b; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; _bd_ticket_crypt_cookie=5596e9efdddfe725ef3bf2681db3675b; __security_server_data_status=1; sid_guard=a930836a69bbeea6f41e3ea82940a48c%7C1730895662%7C5183998%7CSun%2C+05-Jan-2025+12%3A21%3A00+GMT; sid_ucp_v1=1.0.0-KDA3MDZhNjFmYzZhYmYxZjEyOGJhNzQ5YThlZTc3ZjE0NmM5MzBkMDUKGwiEx_CN0s2eARCuvq25BhjvMSAMOAZA9AdIBBoCbHEiIGE5MzA4MzZhNjliYmVlYTZmNDFlM2VhODI5NDBhNDhj; ssid_ucp_v1=1.0.0-KDA3MDZhNjFmYzZhYmYxZjEyOGJhNzQ5YThlZTc3ZjE0NmM5MzBkMDUKGwiEx_CN0s2eARCuvq25BhjvMSAMOAZA9AdIBBoCbHEiIGE5MzA4MzZhNjliYmVlYTZmNDFlM2VhODI5NDBhNDhj; is_dash_user=1; SEARCH_RESULT_LIST_TYPE=%22single%22; store-region=cn-bj; store-region-src=uid; my_rd=2; live_use_vvc=%22false%22; xgplayer_device_id=37678671110; publish_badge_show_info=%221%2C0%2C0%2C1732429627568%22; pwa2=%220%7C0%7C3%7C0%22; _tea_utm_cache_1243=undefined; MONITOR_WEB_ID=dd39c3d9-f033-48b6-94b7-67f900ce3f5e; dy_swidth=1366; dy_sheight=768; ttwid=1%7CXFa9g8D14cG8ng4XlvwsjMQAOktcPAU9J54ufIS-mbo%7C1732430249%7C9c2ff14d38bdf29a6869df3bc6bf87f958dac887ec96838fcc8a5805ecd6c859; download_guide=%223%2F20241124%2F0%22; FOLLOW_RED_POINT_INFO=%221%22; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.335%7D; douyin.com; device_web_cpu_core=8; device_web_memory_size=8; architecture=amd64; strategyABtestKey=%221732539062.569%22; csrf_session_id=c46e6a17de3b8e05f4251b2fa6fef0f0; biz_trace_id=160d91c7; xg_device_score=7.554258647749727; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; WallpaperGuide=%7B%22showTime%22%3A1732436142446%2C%22closeTime%22%3A0%2C%22showCount%22%3A3%2C%22cursor1%22%3A71%2C%22cursor2%22%3A22%7D; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAl_9zTWpxneEZC3Tn0hKbczqHNM3IZ_io7yUgepTIbgY%2F1732550400000%2F1732539068372%2F0%2F1732542270962%22; __ac_nonce=0674485770043ce5eb2bc; __ac_signature=_02B4Z6wo00f01R8adPgAAIDAwEGHtKb0.PkfOnBAACCE39; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAl_9zTWpxneEZC3Tn0hKbczqHNM3IZ_io7yUgepTIbgY%2F1732550400000%2F1732543869870%2F0%2F1732542196716%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1366%2C%5C%22screen_height%5C%22%3A768%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A8%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A100%7D%22; passport_fe_beating_status=true; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCSms0TkpjczNwRGVSVng2alpFZ0NPUW9GRXpmQXVhek1FdUZNallXdjNsOVF2eEM1MmVWeUNRcHcyVzB5Ump4ZnEyVit4TVVXVlBLbzJma2ZtVzgzTzA9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; odin_tt=0b6ed17cdc46c8e2f68fc2d611b9a2caaa3283efd8d41880dc3dd23e2b7cec750479c2a36664e1afafd8d2cfd860b2039b8eb6d15f9c6cb40e5881afa4eaeb5c; IsDouyinActive=true'
        desc = '#天生丽质 #极品身材 #叶凯薇'
        crawler.download_video(video_id, download_cookie, desc)

    def test_run(self):
        crawler = DouyinCrawler()
        crawler.run()


if __name__ == '__main__':
    unittest.main()
