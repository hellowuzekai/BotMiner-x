# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import random
import sys
from lib.common import read_pcap, split_cflow, split_flow, save
from lib.calc import scale_cflow
from lib.data import cpanel
from lib.option import init_options


def main():
    if len(sys.argv) < 3:
        exit('Usage: python main.py <GROUP_ID> <OUTPUT_PATH>\n'
             'Example: python main.py 2 ./output/result.csv')
    group = sys.argv[1]
    output_path = sys.argv[2]

    init_options()
    read_pcap(group)
    split_flow()
    split_cflow()
    scale_cflow()
    test()
    save(output_path)


# 随机输出一个Cflow的具体信息作为测试
def test():
    cf = random.choice(cpanel.C_FLOWS)
    print '[test] random cf in C_FLOWS:'
    print cf.__dict__


if __name__ == '__main__':
    main()
