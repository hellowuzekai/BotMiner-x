# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import argparse
import sys


def cliparse():
    parser = argparse.ArgumentParser(description='BotMiner-x',
                                     usage='python main.py (-r FILE) [options]',
                                     add_help=False)

    filter = parser.add_argument_group('FILTER')
    filter.add_argument('-fI', dest="filter_internal", default=False, action='store_true',
                        help='Filter out communications between internal hosts.')
    filter.add_argument('-fB', dest="filter_broken", default=False, action='store_true',
                        help='Filter out flows that are not completely established.')
    # TODO
    filter.add_argument('-fE', dest="filter_external", default=False, action='store_true',
                        help='Filter out flows initiated from external hosts towards internal hosts.')
    # TODO
    filter.add_argument('-fW', dest="filter_whitelist", default=False, action='store_true',
                        help='Filter out flows whose destinations are legitimate servers.')
    filter.add_argument('--filter-all', dest="filter_all", default=False, action='store_true',
                        help='Apply all filters.')

    io = parser.add_argument_group('IO')
    io.add_argument('-r', metavar='FILE', dest="input_path", type=str, default='',
                    help='input pcap file path&name.')
    io.add_argument('-w', metavar='FILE', dest="output_path", type=str, default='',
                    help='output file path&name. default in ./output/')

    system = parser.add_argument_group('SYSTEM')
    system.add_argument('-h', '--help', action='help',
                        help='show this help message and exit.')

    if len(sys.argv) == 1:
        sys.argv.append('-h')
    args = parser.parse_args()
    return args
