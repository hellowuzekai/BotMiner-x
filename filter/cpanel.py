# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import os
from lib.data import cpanel, arg
from lib.model import Flow


def pcap_filter(path):
    """
    使用tshark进行初步过滤：
    1 仅保留IPV4中TCP和UDP协议的数据包
    2 去除内网之间通信的数据包
    """
    print '[filter] Loading file: ' + path
    name = path.split('/')[-1].split('.')[0]
    new_path = os.path.join('./data/', name + '_filtered.pcap')
    if os.path.exists(new_path):
        if raw_input('[filter] Filtered pcap file already exists: {}, [R]emove or [U]se it? '.format(new_path)) in ['U',
                                                                                                                    'u']:
            return new_path
        else:
            os.remove(new_path)
    if arg.filter_internal:
        print '[filter] filter_internal...'
        command = 'tshark -r {} -Y "not ipv6 and (tcp or udp) and not ((ip.src==127.0.0.0/8 or ip.src==192.168.0.0/16 or ip.src==10.0.0.0/8 or ip.src==172.16.0.0/12) and (ip.dst==127.0.0.0/8 or ip.dst==192.168.0.0/16 or ip.dst==10.0.0.0/8 or ip.dst==172.16.0.0/12))" -w {} -F pcap'.format(
            path, new_path)
    else:
        command = 'tshark -r {} -Y "not ipv6 and tcp" -w {} -F pcap'.format(path, new_path)

    os.system(command)
    print '[filter] Dump filtered pcap file to path: ' + new_path
    return new_path


def filter_broken():
    # TODO: 过滤掉“不完整通信”和“错误通信”和“未被回复的通信”
    count = 1
    for f in cpanel.FLOWS:
        # TODO: 过滤只有一个packet的Flow
        if len(f.packets) < 2:
            cpanel.FLOWS.remove(f)
            continue

    print '[filter-broken] Flows after filtered: %d' % len(cpanel.FLOWS)

    # TODO: 这里仍然有问题
    # packets = []
    # syn = [None]
    # tell = 0
    # for p in f.packets:
    #     if tell == 1 and p.flag == '':  # 判断普通包是在Syn之后
    #         packets.append(p)
    #     if p.flag == 'Syn':
    #         if tell == 1 and packets != []:  # 判断Sny包为无Fin包的最后一个，并且清空之前的普通包
    #             packets[:] = []
    #         tell = 1
    #         syn[0] = p
    #     if p.flag == 'Fin' and tell == 1:
    #         tell = 0
    #         flow = Flow(count, p)
    #         packets[:0] += syn
    #         packets.append(p)
    #         flow.packets += packets
    #         flow.packet_num = len(packets)
    #         flow.calc()
    #         cpanel.FLOWS.append(flow)
    #         count += 1
    #         packets[:] = []


def filter_external():
    pass


def filter_whitelist():
    pass
