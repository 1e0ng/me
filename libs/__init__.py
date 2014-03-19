#!/usr/bin/python
# -*- coding: utf-8 -*-
import time
from collections import namedtuple
import traceback
import json
import os

from sqlstore import SqlStore

PERFORMANCE_METRIC_MARKER = '<!-- _performtips_ -->'

def show_performance_metric(request, output):
    idx = output.find(PERFORMANCE_METRIC_MARKER)
    if idx > 0:
        pt = int((time.time() - request.start_time) * 1000)
        cls = pt > 250 and 'red' or pt > 100 and 'orange' or 'green'
        block = '<li class="hidden-phone"><a style="color:%s"> %d ms </a></li>' % (cls, pt)
        output = (output[:idx] + block + output[idx+len(PERFORMANCE_METRIC_MARKER):])
    return output

store = SqlStore(host='localhost', user='bear', passwd='', db='me')

class DoubanDB(dict):
    def set(self, k, v):
        self[k] = v
    def delete(self, k):
        del self[k]

class EmployeeClass(object):
    def dget(this, card_id):
        return namedtuple('fullname', 'douban_mail', 'entry_date')('rush', 'rush@lost.com', 2341343)

doubandb = DoubanDB()
doubanfs = DoubanDB()
doubanmc = DoubanDB()

Employee = EmployeeClass()
User = EmployeeClass()
