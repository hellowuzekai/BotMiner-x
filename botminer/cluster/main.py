# !/usr/bin/env python
#  -*- coding: utf-8 -*-
from cross import *

A_ALL = [A(1, 1, 1), A(2, 1, 2), A(3, 1, 3), A(4, 1, 4)]
C_ALL = []

with open('data4.csv', 'r') as f:
    count = 1
    for line in f.readlines():
        id = count
        data = line.split(',')
        if data[0] == '1':
            A_ALL[0].add_host(id)
        if data[1] == '1':
            A_ALL[1].add_host(id)
        if data[2] == '1':
            A_ALL[2].add_host(id)
        if data[3] == '1':
            A_ALL[3].add_host(id)
        id += 1

with open('out.txt', 'r') as f:
    for line in f.readlines():
        data = line.split(',')
        host_id = int(data[0])
        c_id = int(data[1])
        for c in C_ALL:
            if c.id == c_id:
                c.add_host(host_id)
        else:
            C_ALL.append(C(id=c_id))

print len(C_ALL)
print len(A_ALL)

for i in range(530):
    print count_botscore(i, A_ALL, C_ALL)
