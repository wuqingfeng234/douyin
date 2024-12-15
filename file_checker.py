class FileChecker:
    def __init__(self):
        self.list = []
        exsited_file = 'record.txt'
        with open(exsited_file, "r", encoding='utf-8') as of:
            ls = of.readlines()
            for l in ls:
                x=l.replace('\n','')
                self.list.append(x)

    def set_exsited_video(self, video_id):
        exsited_file = 'record.txt'
        with open(exsited_file, "a", encoding='utf-8') as of:
            of.writelines(video_id)
        self.list.append(video_id)

    def is_video_exsits(self, video_id):
        return video_id in self.list
