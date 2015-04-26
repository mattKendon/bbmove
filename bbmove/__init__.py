import shutil

__author__ = 'Matthew'

import os
import fnmatch
import re


def touch(path, dir_only=False):
    basedir = os.path.dirname(path)
    if not os.path.exists(basedir):
        os.makedirs(basedir)
    if not dir_only:
        with open(path, 'a'):
            os.utime(path, None)


def search(path):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.mp4'):
            files.append(os.path.join(root, filename))
    return files


def move(path, tv_show_path):
    for filename in search(path):
        try:
            file = Video(filename)
        except VideoNoMatchException as e:
            continue
        else:
            file.move(tv_show_path)


class VideoNoMatchException(Exception):
    """This exceptions is raised if a filename cannot be turned into a title, season and episode list"""


class Video:
    """Class that parses a filename and gets certain metadata from it"""

    TV_SHOW_PATTERN = '^(?P<title>[\w\.]*)\.s(?P<season>[0-9]{1,2})\.e(?P<episode>[0-9]{1,2})'

    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self._match = self._match()

    def _match(self):
        match = re.match(self.TV_SHOW_PATTERN, self.filename, re.IGNORECASE)
        if match is None:
            raise VideoNoMatchException
        return match

    @property
    def title(self):
        return self._match.group('title').replace('.', ' ').capitalize()

    @property
    def season(self):
        return int(self._match.group('season'))

    @property
    def episode(self):
        return int(self._match.group('episode'))

    @property
    def title_folder(self):
        return self._match.group('title').replace('.', '_').replace('the_', '')

    @property
    def season_folder(self):
        padded_number = str(int(self._match.group('season'))).zfill(2)
        return "season_{0}".format(padded_number)

    @property
    def folder_tree(self):
        return os.path.join(self.title_folder, self.season_folder)

    def move(self, base_folder):
        target = os.path.join(base_folder, self.folder_tree, self.filename)
        touch(target)
        shutil.move(self.filepath, target)
