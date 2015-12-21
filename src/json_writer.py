import json
import os


def create_dir(path):
    if not os.path.exists(os.path.dirname(path)):
        os.makedirs(os.path.dirname(path))


def output(data):
    return json.dumps(data)


def write(data, path, indent=None, separators=None):
    create_dir(path)
    with open(path, 'w+') as outfile:
        json.dump(data, outfile, indent=indent, separators=separators)


def write_pretty(data, path):
    write(data, path, indent=2)


def write_minified(data, path):
    write(data, path, separators=(',', ':'))
