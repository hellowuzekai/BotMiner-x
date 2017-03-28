# !/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Usage:

 First time
   1. apt-get install mysql-server mysql-client && service mysql start
   2. vi ./config.py
   3. python main.py --init

 Insert data
   1. mkdir data2
   2. editcap -c 1000 big.pcap ./data2/small.pcap
   3. python main.py ./data2 <GROUP_ID> <TIME> <NOTE>

"""


def helpmsg():
    exit(__doc__)
