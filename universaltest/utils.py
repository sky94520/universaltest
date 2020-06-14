#! /usr/bin/python3.6
# -*-coding:utf-8 -*-

from os.path import realpath, dirname
import json


def get_config(name):
    path = "%s/configs/%s.json" % (dirname(realpath(__file__)), name)
    with open(path, 'r', encoding='utf-8') as f:
        return json.loads(f.read())
