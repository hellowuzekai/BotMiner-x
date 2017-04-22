# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import MySQLdb
import sys
from option import DB
from data import cpanel, conf
from model import Packet


def read_packets(group_id):
    """
    从数据库中读取Packets并实例化
    """

    db = MySQLdb.connect(conf.DB.HOST, conf.DB.USER, conf.DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    sql = "select * from Packets where GROUP_ID={} order by TIMESTAMP".format(group_id)
    raw_packets = cursor.fetchmany(cursor.execute(sql))
    print '[database] Selected Packets: {}'.format(len(raw_packets))

    cpanel.START_TIME = raw_packets[0][2]
    print '[common] START_TIME: %s' % str(cpanel.START_TIME)
    for p in raw_packets:
        cpanel.PACKETS.append(Packet(p))

    print '[common] Packets loading finished.'


def save_calc_results():
    """
    将CFLOW数据录入数据库，包含4个13维向量和其他CFlow特征
    """

    def quote(s):
        return "'%s'" % s

    print "[database] Saving cflow vectors into database."

    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    # add uesr-prompt before overwrite cflow data.
    query = 'SELECT COUNT(*) FROM Cflow WHERE GROUP_ID={}'.format(cpanel.group)
    cursor.execute(query)
    result = cursor.fetchone()
    if result[0]:
        msg = '[!] [database] Group {} already has {} results, wants to overwrite? [Y/n]'.format(cpanel.group,
                                                                                                 int(result[0]))
        if raw_input(msg) in ['n', 'N', 'No', 'no']:
            sys.exit('System exit.')
        else:
            db.query('DELETE FROM Cflow WHERE GROUP_ID={}'.format(cpanel.group))
            # db.commit()

    for cflow in cpanel.C_FLOWS:
        query = """
            INSERT INTO Cflow(
             GROUP_ID,
             IP_SRC,
             FLOWS,
             FPH_13,
             PPF_13,
             BPP_13,
             BPS_13)VALUES ({},{},{},{},{},{},{})
            """.format(
            quote(str(cflow.group)),  # use cpanel.group instead? TODO
            quote(str(cflow.ip_src)),
            quote(str(cflow.flow_count)),
            quote(','.join([str(i) for i in cflow.fph])),
            quote(','.join([str(i) for i in cflow.ppf])),
            quote(','.join([str(i) for i in cflow.bpp])),
            quote(','.join([str(i) for i in cflow.bps])),
        )
        cursor.execute(query)

    db.commit()

    query = 'SELECT COUNT(*) FROM Cflow WHERE GROUP_ID={}'.format(cpanel.group)
    cursor.execute(query)
    result = cursor.fetchone()
    print "[database] Done, inserted items count: {}".format(int(result[0]))

    db.close()


def get_calc_results():  # TODO
    db = MySQLdb.connect(DB.HOST, DB.USER, DB.PASS)
    cursor = db.cursor()
    db.select_db("BOTNET")

    query = """

    """


def show_database_status():
    """
    查看当前数据库中的数据情况。

    DATABASE_STATUS

    GROUP_ID | UPLOAD_TIME | UPLOAD_NAME | START_TIME | PACKETS | CALC_CFLOW
    1	5.28.15.23	cdxy	1000.0	0	-
    2	5.28.15.23	cdxy	1000.0	54	7
    3	1111	cdxy-real-1	1000.0	26542	-
    5	1111	cdxy-real-1	1000.0	105329	-
    6	1111	cdxy-real-1	1000.0	171863	82
    7	111	    cdxy-real	1000.0	10207	-
    8	111	    cdxy-real	1000.0	62008	-
    9	111	    cdxy-real	1000.0	61997	-
    10	1	    cdxy-test	1000.0	61997	2678
    15	1	    cdxy-real	1000.0	5242606	32420

    """
    db = MySQLdb.connect(conf.DB.HOST, conf.DB.USER, conf.DB.PASS, conf.DB.NAME)
    cursor = db.cursor()

    sql = """
        select ID,UPLOAD_TIME,UPLOAD_NAME,START_TIME,
        (select count(*) from Packets where Packets.GROUP_ID=DataGroup.ID) as packets,
        IF( EXISTS (select * from Cflow where Cflow.GROUP_ID=DataGroup.ID),
            (select COUNT(*) from Cflow where Cflow.GROUP_ID=DataGroup.ID),
            '-'
        )
        from DataGroup
    """
    groups = cursor.fetchmany(cursor.execute(sql))

    print 'DATABASE_STATUS\n\nGROUP_ID | UPLOAD_TIME | UPLOAD_NAME | START_TIME | PACKETS | CALC_CFLOW'
    for g in groups:
        print('\t'.join([str(_) for _ in g]))
