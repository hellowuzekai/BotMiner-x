# !/usr/bin/env python
#  -*- coding: utf-8 -*-

"""
Usage:
  python main.py <GROUP_ID> (--save|--debug|--outfile|--status)

Example:
  python main.py 2 --save
  python main.py 2 --outfile
  python main.py --status

Options:
  --save     Save results to database
  --outfile  Save results in ./output/results.txt
  --status   Show data status in database.
  --debug    Show more details.

"""


def helpmsg():
    exit(__doc__)
