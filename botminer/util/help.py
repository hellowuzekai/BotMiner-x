# !/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Usage:
  python main.py <GROUP_ID> (--save|--debug|--outfile)

Example:
  python main.py 2 --save

Options:
  --save     Save results to database
  --outfile  Save results in ./output/results.txt
  --debug    Show more details.

"""


def helpmsg():
    exit(__doc__)
