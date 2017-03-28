# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
from common import init_database, insert_packets
from help import helpmsg


def main():
    if '--init' in sys.argv:
        init_database()
        exit('Database initialized success.')

    if '-h' in sys.argv or '--help' in sys.argv or len(sys.argv) < 5:
        helpmsg()

    insert_packets()


if __name__ == '__main__':
    main()
