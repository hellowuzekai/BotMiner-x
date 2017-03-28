# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy

bot_count = 30
pc_count = 500
A_clusted = 4

rand_start = 0
rand_end = 5


def gen():
    final_str = ''
    for p in range(pc_count):
        final_str += ','.join([str(random.randint(rand_start, rand_end)) for i in range(52)]) + '\n'

    bot_data = ','.join([str(random.randint(rand_start, rand_end)) for i in range(52)])
    for p in range(bot_count):
        final_str += bot_data + '\n'

    return final_str


s = gen()
with open('data52.csv', 'w') as f:
    f.write(s)

with open('data8.csv', 'w') as f:
    with open('data52.csv', 'r') as p:
        for line in p.readlines():
            data_list = [int(a) for a in line.split(',')]
            data = [data_list[:13], data_list[13:26], data_list[26:39], data_list[39:]]
            line = []
            for each in data:
                avg = numpy.mean(data_list)
                var = numpy.var(data_list)
                line.append(str(avg))
                line.append(str(var))
            f.write(','.join(line) + '\n')

with open('data4.csv', 'w') as f:
    for i in range(pc_count):
        f.write(','.join(['0' for m in range(A_clusted)]) + '\n')
    for j in range(bot_count):
        f.write(','.join([random.choice(['0', '1']) for k in range(A_clusted)]) + '\n')
