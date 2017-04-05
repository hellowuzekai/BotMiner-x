# !/usr/bin/env python
#  -*- coding: utf-8 -*-


def get_cflow_data(group_id):
    """
    Fetch all cflow data from database
    """

    import MySQLdb
    db = MySQLdb.connect('localhost', 'root', 'root', 'BOTNET')
    cursor = db.cursor()
    sql = "select * from Cflow where GROUP_ID={} order by id".format(group_id)
    cflows = cursor.fetchmany(cursor.execute(sql))
    print "[database] cflows: {}".format(len(cflows))

    return cflows


# test
if __name__ == '__main__':
    get_cflow_data(group_id=6)
