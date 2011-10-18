#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__  = 'Wenbin Wu <admin@wenbinwu.com>'
__credits__ = 'Python best'
__date__    = 'Fri 14 Oct 2011 05:16:07 PM CST'
__version__ = '0.1'

import urllib2
import re

RE_TITLE = re.compile(r'\<title\>(?P<title>.*)\</title\>')
RE_LINK = re.compile(r'http://(?P<url>\S*)')

def link(phenny, input):
    content = 'dafadsg http://google.com/ hello '
    m = RE_LINK.search(content)
    if m is None:
        return

    url = m.group('url')

    try:
        page = urllib2.urlopen('http://'+url).read()
    except:
        return

    m = RE_TITLE.search(page)
    if m is not None:
        title = m.group('title')
        title = title.replace('\n', '')
        title = title.replace('\r', '')
        phenny.say(title)

#link.rule = ('.*')
#link.priority = 'low'

if __name__ == '__main__':
    link(None,None)
