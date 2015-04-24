
__author__ = 'Matthew'

import os
import fnmatch
import re


def search(path):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.mp4'):
            files.append(filename)
    return files


class VideoNoMatchException(Exception):
    """This exceptions is raised if a filename cannot be turned into a title, season and episode list"""


class Video:
    """Class that parses a filename and gets certain metadata from it"""

    TV_SHOW_PATTERN = '^(?P<title>[\w\.]*)\.s(?P<season>[0-9]{1,2})\.e(?P<episode>[0-9]{1,2})'

    def __init__(self, filename):
        self.filename = filename
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
        return self._match.group('season')

    @property
    def episode(self):
        return self._match.group('episode')


