# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import MySQLdb

class DB:
    HOST = 'localhost'
    USER = 'root'
    PASS = 'root'
    NAME = 'BOTNET'

db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)

# class SETTING:
#     PCAP_SIZE = 10  # cut into small files (10M)
