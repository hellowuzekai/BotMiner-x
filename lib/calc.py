# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from data import C_FLOWS, FLOWS


def scale_data(max, item):
    max = float(max)

    vector = [0, max * 0.05, max * 0.1, max * 0.15, max * 0.2, max * 0.25, max * 0.3, max * 0.4, max * 0.5, max * 0.6,
              max * 0.7, max * 0.8, max * 0.9, max + 1]

    final = [0] * (len(vector) - 1)
    for cf in C_FLOWS:
        for i in range(len(vector) - 1):
            for value in getattr(cf, item):
                if vector[i] <= value < vector[i + 1]:  # 注意vector结尾的 max+1 在这里作用
                    final[i] += 1
        setattr(cf, item, final)
        final = [0] * (len(vector) - 1)  # here


def scale_cflow():
    fph_all = []
    for cf in C_FLOWS:
        fph_all.extend(cf.fph)
    fph_max = sorted(fph_all)[-1]
    bps_max = sorted([f.bps for f in FLOWS])[-1]
    ppf_max = sorted([f.ppf for f in FLOWS])[-1]
    bpp_max = sorted([f.bpp for f in FLOWS])[-1]
    print '[calc] fph_max: {}\n[calc] bps_max: {}\n[calc] ppf_max: {}\n[calc] bpp_max: {}' \
        .format(fph_max, bps_max, ppf_max, bpp_max)

    scale_data(fph_max, 'fph')
    scale_data(bps_max, 'bps')
    scale_data(ppf_max, 'ppf')
    scale_data(bpp_max, 'bpp')

    print '[calc] Data scaled success.'
