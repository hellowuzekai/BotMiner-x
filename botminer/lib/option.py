# !/usr/bin/env python
#  -*- coding: utf-8 -*-

from data import cpanel,conf


def init_options():
    cpanel.START_TIME = 0
    cpanel.EPOCH = 10
    cpanel.TIME_UNIT = 6  # 单位 秒，一小时=3600秒 此量应与 EPOCH 一同变化
    cpanel.PACKETS = []
    cpanel.FLOWS = []
    cpanel.C_FLOWS = []
    conf.DB = DB

class DB:
    HOST = 'localhost'
    USER = 'root'
    PASS = 'root'
    NAME = 'BOTNET'

