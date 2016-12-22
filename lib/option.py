# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import os
from data import cpanel, arg
from parse import cliparse


def init_options():
    parse_args()
    cpanel.START_TIME = [0]
    cpanel.EPOCH = 10
    cpanel.TIME_UNIT = 60  # 单位 秒，一小时=3600秒 此量应与 EPOCH 一同变化
    cpanel.PACKETS = []
    cpanel.FLOWS = []
    cpanel.C_FLOWS = []


def parse_args():
    arg.update(cliparse().__dict__)
    if arg.filter_all:
        arg.filter_internal = arg.filter_broken = arg.filter_external = arg.filter_whitelist = True

    if not arg.output_path:
        arg.output_path = 'data.csv'  # TODO

    arg.input_path = os.path.join(os.path.realpath(os.path.curdir), arg.input_path)
    if arg.input_path and os.path.isfile(arg.input_path):
        pass
    else:
        raise IOError('Invalid pcap file')
