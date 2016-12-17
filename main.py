# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
import random
from lib.common import read_pcap, split_cflow, split_flow, save
from lib.calc import scale_cflow
from lib.data import C_FLOWS


def main():
    if len(sys.argv) < 2 or '-h' in sys.argv:
        msg = "Usage:\n  python pcapdata.py [pcap-file]\n" \
              "Example:\n  python pcapdata.py ../ca1_http.pcap"
        sys.exit(msg)

    read_pcap(sys.argv[1])
    split_flow()
    split_cflow()
    scale_cflow()
    # test()
    save()


# 随机输出一个Cflow的具体信息作为测试
def test():
    cf = random.choice(C_FLOWS)
    print '[test] random cf in C_FLOW:'
    print cf.__dict__


if __name__ == '__main__':
    main()
