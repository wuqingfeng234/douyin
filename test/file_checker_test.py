import unittest

from file_checker import FileChecker


class FileCheckerTest(unittest.TestCase):
    def test_is_video_exsits(self):
        file_checker = FileChecker()
        exsits = file_checker.is_video_exsits("v0300fg10000ctckuhvog65hmu7hmif0")
        print(exsits)
