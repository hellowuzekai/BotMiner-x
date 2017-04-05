# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import random
import sys
from lib.common import split_cflow, split_flow, save
from lib.calc import scale_cflow
from lib.data import cpanel
from lib.option import init_options
from lib.database import save_calc_results,read_packets


def main():
    if len(sys.argv) < 3:
        exit('Usage: python main.py <GROUP_ID> [--save] [--debug]\n'
             'Example: python main.py 2 --save')
    cpanel.group = sys.argv[1]

    init_options()
    read_packets(cpanel.group)
    split_flow()
    split_cflow()
    scale_cflow()

    if '--save' in sys.argv:
        save_calc_results()

    if '--debug' in sys.argv:
        test()

    if '--outfile' in sys.argv:
        output_path = './output/out.txt'
        save(output_path)


# 随机输出一个Cflow的具体信息作为测试
def test():
    cf = random.choice(cpanel.C_FLOWS)
    cf.flows = None
    print '[test] random cf in C_FLOWS:'
    print cf.__dict__


if __name__ == '__main__':
    main()
