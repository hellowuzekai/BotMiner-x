# !/usr/bin/env python
#  -*- coding: utf-8 -*-

from data import cpanel


class Cflow:
    def __init__(self, id, group, epoch, vector, flows):
        self.epoch = int(epoch)
        self.id = int(id)
        self.ip_src = vector  # TODO 暂时用ip_src定义cflow
        self.group = group
        # self.ip_dst = flow.ip_dst
        # self.port_src = flow.port_src
        # self.port_dst = flow.port_dst
        self.fph = []
        self.bps = []
        self.bpp = []
        self.ppf = []
        self.flows = flows
        self.flow_count = len(self.flows)

    def calc(self):
        for f in self.flows:
            leftIndex = int(
                (f.packets[0].timestamp - cpanel.START_TIME) // cpanel.TIME_UNIT)  # 有个坑，普通变量拿不到改变后的值，用list引用可以
            rightIndex = int((f.packets[-1].timestamp - cpanel.START_TIME) // cpanel.TIME_UNIT + 1)
            for i in range(leftIndex, rightIndex):
                self.fph.append(i)


class Flow:
    def __init__(self, id, vector, packets):
        self.id = int(id)

        _vector = vector.split(':')
        self.ip_src = _vector[0]
        self.ip_dst = _vector[1]
        self.port_src = _vector[2]
        self.port_dst = _vector[3]

        self.packets = packets  # list
        self.packet_num = len(self.packets)
        self.total_byte = sum([packet.byte for packet in self.packets])

        self.bps = self.bpp = self.ppf = None

    def _calc_ppf(self):
        self.ppf = self.packet_num

    def _calc_bps(self):  # 全部大小 除以 总时间
        # TODO 这里应该过滤掉只有一个包的flow就没事了，先用random代替 (PS: split_flow已过滤，每个Flow中至少含有Syn,Fin两个包)
        timestamp_sorted = sorted([packet.timestamp for packet in self.packets])
        total_time_second = timestamp_sorted[-1] - timestamp_sorted[0]
        if not total_time_second:
            print '[error] total-time=0, packet num: %d' % len(self.packets)
            total_time_second = 999
        self.bps = self.total_byte / total_time_second

    def _calc_bpp(self):  # 全部大小 除以 包个数
        self.bpp = self.total_byte / self.packet_num

    def calc(self):
        self._calc_ppf()
        self._calc_bpp()
        self._calc_bps()


class Packet:
    """
    +----+----------+-----------+--------+----------------+----------------+----------+----------+------+
    | ID | GROUP_ID | TIMESTAMP | LENGTH | IP_SRC         | IP_DST         | PORT_SRC | PORT_DST | FLAG |
    +----+----------+-----------+--------+----------------+----------------+----------+----------+------+
    |  1 |        2 |   73.6399 |     54 | 172.29.90.176  | 42.156.235.98  |    47571 |      443 |      |
    |  2 |        2 |   73.6906 |     62 | 42.156.235.98  | 172.29.90.176  |      443 |    47571 |      |
    """

    def __init__(self, raw_data):  # for database column
        self.id = float(raw_data[0])
        self.timestamp = float(raw_data[2])
        self.byte = float(raw_data[3])
        self.ip_src = str(raw_data[4])
        self.ip_dst = str(raw_data[5])
        self.port_src = str(raw_data[6])
        self.port_dst = str(raw_data[7])
        # TODO other details needed?
        # self.content = str()
        # self.flag = str(raw_data[8])
