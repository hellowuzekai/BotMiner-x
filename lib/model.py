# !/usr/bin/env python
#  -*- coding: utf-8 -*-

from data import START_TIME, TIME_UNIT, EPOCH
import random
from scapy.all import *


class Cflow:
    def __init__(self, id, epoch, flow):
        self.epoch = int(epoch)
        self.id = int(id)
        self.ip_src = flow.ip_src
        self.ip_dst = flow.ip_dst
        self.port_src = flow.port_src
        self.port_dst = flow.port_dst
        self.flow_count = 0
        self.fph = []
        self.bps = []
        self.bpp = []
        self.ppf = []
        self.flows = []

    def calc(self):
        # TODO 由于我们的测试数据都是几分钟的，按小时算数据无效，这里先用random模拟结果测试程序 (PS:增加全局变量 TIME_UNIT 作为可调整的时间单位)
        for f in self.flows:
            leftIndex = int((f.packets[0].timestamp - START_TIME[0]) // TIME_UNIT)  # 有个坑，普通变量拿不到改变后的值，用list引用可以
            rightIndex = int((f.packets[-1].timestamp - START_TIME[0]) // TIME_UNIT + 1)
            for i in range(leftIndex, rightIndex):
                self.fph.append(i)
        #self.fph = [random.choice([0, 1]) for i in range(self.epoch)]
        self.bps = [f.bps for f in self.flows]
        self.bpp = [f.bpp for f in self.flows]
        self.ppf = [f.ppf for f in self.flows]

    def add_flow(self, flow):
        self.flows.append(flow)
        self.flow_count += 1


class Flow:
    def __init__(self, id, packet):
        self.id = int(id)  # 编号
        self.packet_num = 0  # packet数量
        self.ip_src = packet.ip_src
        self.ip_dst = packet.ip_dst
        self.port_src = packet.port_src
        self.port_dst = packet.port_dst
        self.packets = []
        self.bps = self.bpp = self.ppf = None

    def add_packet(self, packet):
        self.packets.append(packet)
        self.packet_num += 1

    def _calc_ppf(self):
        self.ppf = self.packet_num

    def _calc_bps(self):  # 全部大小 除以 总时间
        # TODO 这里应该过滤掉只有一个包的flow就没事了，先用random代替 (PS: split_flow已过滤，每个Flow中至少含有Syn,Fin两个包)
        total_byte = sum([packet.byte for packet in self.packets])
        timestamp_sorted = sorted([packet.timestamp for packet in self.packets])
        total_time_second = timestamp_sorted[-1] - timestamp_sorted[0]
        # if not total_time_second:
        #     raise ValueError('invalid dataset.')
        #     total_time_second =
        self.bps = total_byte / total_time_second
        #self.bps = random.uniform(1, 5)

    def _calc_bpp(self):  # 全部大小 除以 包个数
        total_byte = sum([packet.byte for packet in self.packets])
        self.bpp = total_byte / self.packet_num

    def _check_data(self):
        if self.packet_num and self.packets:
            pass
        else:
            raise ValueError('invalid dataset.')

    def calc(self):
        self._check_data()
        self._calc_ppf()
        self._calc_bpp()
        self._calc_bps()


class Packet:
    def __init__(self, packet, id):
        self.id = id
        self.byte = len(packet)
        self.timestamp = packet.time  # 转换为秒为单位 #TODO 确认这个是以秒为单位
        self.content = str(packet)
        self.ip_src = packet['IP'].src
        self.ip_dst = packet['IP'].dst
        self.port_src = packet.sport
        self.port_dst = packet.dport
        if bin(packet[TCP].flags)[-1] == '1':
            self.flag = 'Fin'
        elif bin(packet[TCP].flags)[-2] == '1':
            self.flag = 'Syn'
        else:
            self.flag = ''
