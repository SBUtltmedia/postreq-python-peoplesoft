import json
import os


def create_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


def write(data, file, indent=None, separators=None):
    create_dir(file)
    with open(file, 'w+') as outfile:
        json.dump(data, outfile, indent=indent, separators=separators)


def write_pretty(data, file):
    write(data, file, indent=2)


def write_minified(data, file):
    write(data, file, separators=(',', ':'))
