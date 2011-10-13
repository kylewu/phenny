#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bigbang.py - Spider Module for mozilla.com.cn
Author: wwu, mozilla.com.cn
"""

import urllib
import re
import time

INTERVAL = 10
LINK = 'http://mozilla.com.cn/qa/user/new/'
Q_LINK = 'http://mozilla.com.cn/qa/user/Q.%s/'
RE_LINK = re.compile('/qa/user/Q.(?P<id>\d+)/">(?P<title>.*)</a>')

is_first_run = True
newest_id = 0
already_started = False

def spy(phenny):
    global is_first_run
    global newest_id

    page = urllib.urlopen(LINK).read()

    m = RE_LINK.search(page)
    if m is not None:
        if is_first_run:
            newest_id = m.group('id')
            is_first_run = False
            newest_id = m.group('id')
            #TODO remove the next line
            new_question(phenny, Q_LINK%newest_id, m.group('title'))
            return
        elif m.group('id') > newest_id:
            newest_id = m.group('id')
            new_question(phenny, Q_LINK%newest_id, m.group('title'))

def new_question(phenny, link, title):
    phenny.say('%s %s' % (title, link))

def spider(phenny, input):
    global already_started
    if already_started:
        return
    already_started = True
    while True:
        spy(phenny)
        time.sleep(INTERVAL)

spider.commands = ['spider']
spider.example = '.spider'
spider.thread = True
