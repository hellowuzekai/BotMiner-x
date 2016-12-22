# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from scapy.all import *
from lib.data import cpanel
from lib.model import Cflow, Flow, Packet
from filter.cpanel import pcap_filter, filter_broken
from lib.data import arg


def read_pcap():
    filtered_file = pcap_filter(arg.input_path)
    pcap = rdpcap(filtered_file)
    pcap = pcap[TCP]
    cpanel.START_TIME[0] = pcap[0].time
    print '[data] START_TIME: %s' % str(cpanel.START_TIME)
    count = 0
    for p in pcap:
        cpanel.PACKETS.append(Packet(p, count))
        count += 1

    print '[common] Total packets: %d' % len(cpanel.PACKETS)


def split_flow():
    flows = []
    count = 1
    for p in cpanel.PACKETS:
        for f in flows:
            if f.ip_src == p.ip_src and f.ip_dst == p.ip_dst and f.port_src == p.port_src and f.port_dst == p.port_dst:
                f.add_packet(p)
                break
        else:
            flow = Flow(count, p)
            count += 1
            flow.add_packet(p)
            flows.append(flow)  # 改为中间变量存储未进行第二次过滤的flows

    cpanel.FLOWS = flows
    print '[common] Total flows: %d' % len(cpanel.FLOWS)

    if arg.filter_broken:
        filter_broken()


    # 计算三个关键值
    for f in cpanel.FLOWS:
        f.calc()


def split_cflow():
    count = 1
    for flow in cpanel.FLOWS:
        for f in cpanel.C_FLOWS:
            # 这里根据2个IP和1个port判断
            if flow.ip_src == f.ip_src and flow.ip_dst == f.ip_dst and flow.port_dst == f.port_dst:
                f.add_flow(flow)
                break
        cflow = Cflow(count, 24, flow)
        cflow.add_flow(flow)
        cpanel.C_FLOWS.append(cflow)
        count += 1

    # 计算4个关键值
    for c in cpanel.C_FLOWS:
        c.calc()

    print '[common] Total c-flows: %d' % len(cpanel.C_FLOWS)


def save():
    with open(arg.output_path, 'w') as f:
        for cf in cpanel.C_FLOWS:
            line = ','.join([str(cf.id), str(cf.fph), str(cf.bps), str(cf.bpp), str(cf.ppf), str(cf.ip_src),
                             str(cf.ip_dst)]).replace('[', '').replace(']', '').replace(' ', '')
            f.write(line + '\n')
