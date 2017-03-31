# !/usr/bin/env python
#  -*- coding: utf-8 -*-
import sys
from data import cpanel


def find_split_point(item):
    """
    输入要排序的list数值
    返回13维向量的切分点

    然后在数值中用 <=切分点具体分成13段
    """
    max = len(item)
    if max < 10:
        raise Exception('[split-point] Error! Cannot scale items less than 10.')

    sorted_item = sorted(item)

    vector = [max * 0.05, max * 0.1, max * 0.15, max * 0.2, max * 0.25, max * 0.3, max * 0.4, max * 0.5, max * 0.6,
              max * 0.7, max * 0.8, max * 0.9]

    split_point = [-1]  # < 左边满足的最小值，避免和0重复取-1
    for i in vector:  # 向下取整 后面选择时要使用 <=
        split_point.append(sorted_item[int(i)])
    split_point.append(sorted_item[-1])  # 加上最大值

    return split_point


def scale_data(item_name):
    """
    工厂函数　<--debug>

    首先取出全部flow.<item_name>，得到分割点。
    遍历每个cflow。将其中的每一个flow.<item_name>利用　a < value <=b 对号入座，
    然后修改final_vector对应位置的数据+=1
    最终将final_vector作为cflow.<item_name>结果储存
    """

    item = [getattr(f, item_name) for f in cpanel.FLOWS]

    print '[scale-data] Scale flow.{}, total: {}'.format(item_name, len(item))
    spoint = find_split_point(item)
    if '--debug' in sys.argv:
        print '{} split by: {}'.format(item_name, spoint)

    v = len(spoint)  # v==14
    for cflow in cpanel.C_FLOWS:  # 对每一个C_FLOW
        final_vector = [0 for _ in range(v - 1)]  # 初始化填充13位0
        for flow in cflow.flows:  # 让单个Ｃ_FLOW中的每一个Flow对号入座
            for i in range(v):
                if i < v - 1:
                    if spoint[i] < getattr(flow, item_name) <= spoint[i + 1]:
                        final_vector[i] += 1
                elif i == v - 1:
                    pass  # 第14位不需要计算

        if '--debug' in sys.argv:
            print final_vector, len(cflow.flows)

        if sum([i for i in final_vector]) != len(cflow.flows):  # 检查算法是否正确
            raise Exception('[scale-data] check this manually(1).')

        if item_name == 'bps':
            cflow.bps = final_vector
        elif item_name == 'ppf':
            cflow.ppf = final_vector
        elif item_name == 'bpp':
            cflow.bpp = final_vector
        else:
            raise Exception('[scale-data] check this manually(2).')  # 检查输入是否正确


def scale_cflow():
    """
    计算每个cflow的4种13维向量
    """
    scale_data_fph()

    for each in ['bps', 'ppf', 'bpp']:
        scale_data(each)

    print '[calc] Data scaled success.'


def scale_data_fph():
    item = [cf.fph for cf in cpanel.C_FLOWS]
    spoint = find_split_point(item)
    if '--debug' in sys.argv:
        print '{} split by: {}'.format('fph', spoint)

    v = len(spoint)  # v==14
    for cflow in cpanel.C_FLOWS:  # 对每一个C_FLOW
        final_vector = [0 for _ in range(v - 1)]  # 初始化填充13位0
        for each in cflow.fph:  # 取出cflow.fph的每个值
            for i in range(v):
                if i < v - 1:
                    if spoint[i] < each <= spoint[i + 1]:
                        final_vector[i] += 1
                elif i == v - 1:
                    pass  # 第14位不需要计算

        if '--debug' in sys.argv:
            print final_vector, len(cflow.flows)

        if sum([i for i in final_vector]) != len(cflow.fph):  # 检查算法是否正确
            raise Exception('[scale-data] check this manually(3).')
