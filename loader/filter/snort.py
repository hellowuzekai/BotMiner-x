# !/usr/bin/env python
#  -*- coding: utf-8 -*-

import os


def snort():
    command = 'sudo snort -r ~/Desktop/botnet/BotMiner-access/BotMiner3/BotMiner/data/ca2.pcap -c /etc/snort/rule.conf -l customlog'
    os.system('')
