# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import MySQLdb
import os, sys
from scapy.all import *
from config import DB


def init_database():
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS)

    cursor = db.cursor()
    cursor.execute("create database if not exists BOTNET ;")
    db.select_db("BOTNET")
    sql = """CREATE TABLE  DataGroup(
             ID INT NOT NULL AUTO_INCREMENT,
             UPLOAD_TIME CHAR(10),
             UPLOAD_NAME CHAR(20),
             START_TIME  FLOAT,
             PRIMARY KEY (ID))
             """

    cursor.execute(sql)
    sql = """CREATE TABLE  Packets(
             ID INT NOT NULL AUTO_INCREMENT,
             GROUP_ID INT NOT NULL,
             TIMESTAMP  FLOAT NOT NULL,
             LENGTH INT NOT NULL,
             IP_SRC CHAR(15) NOT NULL,
             IP_DST CHAR(15) NOT NULL,
             PORT_SRC INT NOT NULL,
             PORT_DST INT NOT NULL,
             FLAG CHAR(5),
             PRIMARY KEY (ID),
             foreign key(GROUP_ID) references DataGroup(ID)
             )"""

    sql = """CREATE TABLE  Cflow(
             ID INT NOT NULL AUTO_INCREMENT,
             GROUP_ID INT NOT NULL,
             IP_SRC VARCHAR(20),
             IP_DST VARCHAR(20),
             PORT_SRC INT,
             PORT_DST INT,
             FLOWS INT NOT NULL,
             FPH_13 VARCHAR (100) NOT NULL,
             PPF_13 VARCHAR (100) NOT NULL,
             BPP_13 VARCHAR (100) NOT NULL,
             BPS_13 VARCHAR (100) NOT NULL,
             NOTE CHAR (100),
             PRIMARY KEY (ID),
             foreign key(GROUP_ID) references DataGroup(ID)
             )"""
    cursor.execute(sql)

    db.close()


def insert_packets(delete=False):
    filename = sys.argv[1]
    group_id = sys.argv[2]
    upload_time = sys.argv[3]
    upload_name = sys.argv[4]

    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, DB.NAME)
    cursor = db.cursor()

    sql = "INSERT INTO DataGroup(ID, UPLOAD_TIME, UPLOAD_NAME, START_TIME)VALUES (" + group_id + ", '" + upload_time + "','" + upload_name + "', '" + "1000" + "')"  # below 100s
    cursor.execute(sql)
    db.commit()

    def insert_single_file(filename):
        pcap = rdpcap(filename)[TCP]
        for i in xrange(len(pcap)):
            length = len(pcap[i])
            try:
                timestamp = pcap[i].time - int(pcap[i].time) / 100 * 100  # below 100s
                ip_src = pcap[i]['IP'].src
                ip_dst = pcap[i]['IP'].dst
                port_src = str(pcap[i]['IP'].sport)
                port_dst = str(pcap[i]['IP'].dport)
            except:
                continue
            """
            <Ether  dst=00:23:89:3a:8b:08 src=00:0e:c6:c2:5f:d8 type=0x800 |<IP  version=4L ihl=5L tos=0x0 len=40 id=34019 flags=DF frag=0L ttl=64 proto=tcp chksum=0x9920 src=172.29.90.176 dst=42.156.235.98 options=[] |<TCP  sport=47571 dport=https seq=3681001345 ack=1822908669 dataofs=5L reserved=0L flags=A window=65280 chksum=0x1ce7 urgptr=0 |>>>
            """
            if bin(pcap[i][TCP].flags)[-1] == '1':
                flag = 'Fin'
            elif bin(pcap[i][TCP].flags)[-2] == '1':
                flag = 'Syn'
            else:
                flag = ''

            sql = "INSERT INTO Packets(GROUP_ID, TIMESTAMP,LENGTH,IP_SRC,IP_DST,PORT_SRC,PORT_DST,FLAG)VALUES (" + group_id + "," + str(
                timestamp) + "," + str(
                length) + ", '" + ip_src + "','" + ip_dst + "', '" + port_src + "', '" + port_dst + "', '" + flag + "')"
            cursor.execute(sql)
            db.commit()

        if delete:
            os.remove(filename)

    if os.path.isfile(filename):
        insert_single_file(filename)
    elif os.path.isdir(filename):
        files = os.listdir(filename)
        total = len(files)
        print '[loader] Total pcap files: {}'.format(total)

        finished = 0
        for each in files:
            finished += 1
            insert_single_file(os.path.abspath(os.path.join(filename, each)))
            print '[loader] {}/{} finished.'.format(finished, total)
