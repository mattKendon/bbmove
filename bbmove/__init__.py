__author__ = 'Matthew'

import os


def search(path):
    files = []
    for file in os.listdir(path):
        if file.endswith('.mp4'):
            files.append(file)
    return files