# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from ..config import db


class apanel_cluster:
    def __init__(self, packet, group_id):
        self.packet = packet
        self.group_id = group_id
        self.run()

    def detect_mirai(self):
        # TODO 添加判断逻辑
        if True:
            self.insert_database('Mirai')

    def detect_ares(self):
        # TODO 添加判断逻辑
        if True:
            self.insert_database('Ares')

    def insert_database(self, table_name):
        try:
            ip_src = self.packet['IP'].src
            ip_dst = self.packet['IP'].dst
            port_src = str(self.packet['IP'].sport)
            port_dst = str(self.packet['IP'].dport)
        except:
            return

        cursor = db.cursor()
        sql = "INSERT INTO {}(GROUP_ID, IP_SRC, IP_DST, PORT_SRC, PORT_DST)VALUES ('{}','{}','{}','{}','{}')".format(
            table_name,
            self.group_id,
            ip_src,
            ip_dst,
            port_src,
            port_dst
        )
        cursor.execute(sql)
        db.commit()

    def run(self):
        if self.detect_ares():
            self.insert_database(self.packet, 'Ares')
        if self.detect_mirai():
            self.insert_database(self.packet, 'Mirai')
