import os
import sys


class Command:
    def __init__(self):
        self.path = "/home/lunchbot/kakao/blog/directory"

    def isDirectory(self, name):
        path = self.path

        return os.path.isdir(path+'/'+name)

    def ls(self):
        path = self.path

        f = os.popen('ls ' + path)

        return f.read()

    def ls2(self):
        path = self.path

        return os.listdir(path)

    def command(self):
        result = "This is help page."

        return result

    def cd(self):
        return "test"
