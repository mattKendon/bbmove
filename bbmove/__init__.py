__author__ = 'Matthew'

import os
import fnmatch


def search(path):
    files = []
    for root, dirnames, filenames in os.walk(path):
        for filename in fnmatch.filter(filenames, '*.mp4'):
            files.append(filename)
    return files