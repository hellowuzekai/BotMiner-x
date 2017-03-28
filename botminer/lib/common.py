# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import MySQLdb
from data import cpanel, conf
from model import Cflow, Flow, Packet


def read_pcap(group_id):
    db = MySQLdb.connect(conf.DB.HOST, conf.DB.USER, conf.DB.PASS, conf.DB.NAME)
    cursor = db.cursor()
    sql = "select * from Packets where GROUP_ID={} order by id".format(group_id)

    raw_packets = cursor.fetchmany(cursor.execute(sql))
    print(raw_packets)
    print '[database] Selected Packets: {}'.format(len(raw_packets))

    cpanel.START_TIME = raw_packets[0][2]
    print '[common] START_TIME: %s' % str(cpanel.START_TIME)
    for p in raw_packets:
        cpanel.PACKETS.append(Packet(p))

    print '[common] Packets loading finished.'


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

    # 计算三个关键值
    for f in cpanel.FLOWS:
        f.calc()


def split_cflow():
    count = 1
    for flow in cpanel.FLOWS:
        for f in cpanel.C_FLOWS:
            # 这里根据源IP划分CFlow，与论文不同 TODO 验证可行性
            # if flow.ip_src == f.ip_src and flow.ip_dst == f.ip_dst and flow.port_dst == f.port_dst:
            if flow.ip_src == f.ip_src:
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


def save(output_path):
    with open(output_path, 'w') as f:  # TODO more checks here
        for cf in cpanel.C_FLOWS:
            line = ','.join([str(cf.id), str(cf.fph), str(cf.bps), str(cf.bpp), str(cf.ppf), str(cf.ip_src),
                             str(cf.ip_dst)]).replace('[', '').replace(']', '').replace(' ', '')
            f.write(line + '\n')
