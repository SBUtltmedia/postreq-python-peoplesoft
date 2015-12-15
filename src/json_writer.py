import json


def write_pretty(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile, indent=2)


def write_minified(data, file):
    with open(file, 'w') as outfile:
        json.dump(data, outfile)