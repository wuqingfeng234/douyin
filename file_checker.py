class FileChecker:
    def __init__(self):
        self.__exsit_video = []
        self.__exclude_people = []
        self.__init_exsit_video()
        self.__init_exclude_people()

    def __init_exsit_video(self):
        exsited_file = 'record.txt'
        with open(exsited_file, "r", encoding='utf-8') as of:
            ls = of.readlines()
            for l in ls:
                x = l.replace('\n', '')
                self.__exsit_video.append(x)

    def __init_exclude_people(self):
        execlude_people = 'execlude_people.txt'
        with open(execlude_people, "r", encoding='utf-8') as of:
            ls = of.readlines()
            for l in ls:
                x = l.replace('\n', '')
                self.__exclude_people.append(x)

    def set_exsited_video(self, video_id):
        exsited_file = 'record.txt'
        with open(exsited_file, "a", encoding='utf-8') as of:
            of.writelines(video_id)
        self.__exsit_video.append(video_id)

    def is_video_exsits(self, video_id):
        return video_id in self.__exsit_video

    def is_people_exclude(self, user_id):
        return user_id in self.__exclude_people
