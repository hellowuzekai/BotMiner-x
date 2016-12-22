# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import random
from lib.common import read_pcap, split_cflow, split_flow, save
from lib.calc import scale_cflow
from lib.data import cpanel
from lib.option import init_options
from lib.parse import cliparse


def main():
    cliparse()
    init_options()
    read_pcap()
    split_flow()
    split_cflow()
    scale_cflow()
    # test()
    save()


# 随机输出一个Cflow的具体信息作为测试
def test():
    cf = random.choice(cpanel.C_FLOW)
    print '[test] random cf in C_FLOW:'
    print cf.__dict__


if __name__ == '__main__':
    main()
