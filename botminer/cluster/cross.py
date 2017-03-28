# !/usr/bin/env python
#  -*- coding: utf-8 -*-



class C:
    def __init__(self, id):
        self.id = int(id)
        self.host = set()

    def add_host(self, host):
        if host not in self.host:
            self.host.add(host)

    def __len__(self):
        return len(self.host)


class A:
    def __init__(self, id, weight, type):  # 4 types available, weight >= 1
        self.id = int(id)
        self.weight = float(weight)
        self.host = set()
        self.type = type

    def add_host(self, host):
        if host not in self.host:
            self.host.add(host)

    def __len__(self):
        return len(self.host)


def cross_cluster():
    pass


def count_botscore(host_id, As, Cs):
    def calc1(Ai, Aj):
        return Ai.weight * Aj.weight * (len(Ai.host.intersection(Aj.host)) / len(Ai.host.union(Aj.host)))

    def calc2(Ai, Ck):
        return Ai.weight * (len(Ai.host.intersection(Ck.host)) / len(Ai.host.union(Ck.host)))

    A_list = get_list_by_host(host_id, As)
    C_list = get_list_by_host(host_id, Cs)

    score = 0
    for i in range(len(A_list)):
        for j in range(len(A_list)):
            if j > i and A_list[i].type != A_list[j].type:
                score += calc1(A_list[i], A_list[j])
    for A in A_list:
        for C in C_list:
            score += calc2(A, C)

    return score


def get_list_by_host(host_id, A_list):
    """
    A(h) = {Ai}i=1...m

    the set of A-clusters that contain h,
    """
    res = []
    for A in A_list:
        if host_id in A.host:
            res.append(A)
    return res
