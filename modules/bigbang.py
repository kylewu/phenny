#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
bigbang.py - Spider Module for mozilla.com.cn
Author: wwu, mozilla.com.cn
"""

import urllib
import re
import time

INTERVAL = 60
LINK = 'http://mozilla.com.cn/qa/user/new/'
Q_LINK = 'http://mozilla.com.cn/qa/user/Q.%s/'
RE_LINK = re.compile('/qa/user/Q.(?P<id>\d+)/">(?P<title>.*)</a>')
RE_CONTENT = re.compile('''<div\s{1}id="question-detail-content"\s{1}class="safehtml-content">\s*<p>(?P<content>.*)</p>''',
            re.DOTALL)

is_first_run = True
newest_id = 0
already_started = False

def spy(phenny):
    global is_first_run
    global newest_id

    try:
        page = urllib.urlopen(LINK).read()
    except:
        return

    m = RE_LINK.search(page)
    if m is not None:
        if is_first_run:
            newest_id = m.group('id')
            is_first_run = False
            #TODO remove the next line
            #phenny.say('Bug fixed')
            new_question(phenny, Q_LINK%newest_id, m.group('title'))
        elif int(m.group('id')) > int(newest_id):
            newest_id = m.group('id')
            new_question(phenny, Q_LINK%newest_id, m.group('title'))

def new_question(phenny, link, title):
    phenny.say('社区新问题:%s %s' % (title, link))
    return

    try:
        page = urllib.urlopen(link).read()
    except:
        return

    m = RE_CONTENT.search(page)

    if m is not None:
        content =  m.group('content')
        content= content.replace('\n', '')
        content = content.replace('\r', '')

        #print title, content, link

        phenny.say('社区新问题 %s:\n\t%s\nLink : %s' % (title, content, link))

def spider(phenny, input):
    if not input.admin:
        return
    global already_started
    if already_started:
        return
    already_started = True
    while True:
        spy(phenny)
        time.sleep(INTERVAL)

spider.commands = ['spy']
spider.example = '.spy'
spider.thread = True

if __name__ == '__main__':

    new_question(None, None, None)
    #spy(None)

