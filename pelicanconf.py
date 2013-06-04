#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Dong Weiming'
SITENAME = u'小明明s Github'
SITEURL = 'http://dongweiming.github.io'

TIMEZONE = "Asia/Shanghai"                                                     
LOCALE = "zh_CN.UTF-8" 
DATE_FORMATS = {
    "en": "%A, %d %B, %Y",
    }
#ARTICLE_URL = "blog/{date:%Y}/{date:%m}/{slug}.html"
#ARTICLE_SAVE_AS = "blog/{date:%Y}/{date:%m}/{slug}.html"
#PAGE_URL = "{slug.html}"
#PAGE_SAVE_AS = "{slug}.html"
#DIRECT_TEMPLATES = ('blog/index', 'tags', 'categories', 'archives')
#PAGINATED_DIRECT_TEMPLATES = ['blog/index']
#ARTICLE_EXCLUDES = ["pages", "old"]
FEED_ATOM = "feeds/atom.xml"
CATEGORY_FEED_ATOM = "feeds/%s.atom.xml"
FEED_MAX_ITEMS = 20
RELATIVE_URLS = False
RECENT_POST_NUMBER = 8

import os
if os.environ.get("OVERRIDE_SITEURL"):
    SITEURL = os.environ["OVERRIDE_SITEURL"]

def FORMAT_DATE(date):
    d = date.strftime("%A, %B ")
    day = str(date.day)
    if day[-1] == "1":
        day += "st"
    elif day[-1] == "2":
        day += "nd"
    elif day[-1] == "3":
        day += "rd"
    else:
        day += "th"
    d += day + date.strftime(", %Y")
    return d

TYPOGRIFY = True

#USE_FOLDER_AS_CATEGORY = False

THEME = './mystyle'

LINKS = (('小明明s à domicile', 'http://www.dongwm.com'),)                     
                                                                               
SOCIAL = (('twitter', 'http://twitter.com/dongweiming'),                       
          ('github', 'http://github.com/orzrd'),                               
          ('github', 'http://github.com/dongweiming'),) 

DEFAULT_PAGINATION = 8

PLUGIN_PATH = '/home/dongwm/pelican-plugins'
PLUGINS = [
    'github_activity',
    'related_posts',
    'assets',
    ]

GITHUB_ACTIVITY_FEED = 'https://github.com/dongweiming.atom'


GOOGLE_ANALYTICS = "UA-41346031-1"

#MENUITEMS = [
    #("About", "/about.html"),
#    ("blog", "/blog/"),
#    ("projects", "/projects.html"),
#    ]

#FILES_TO_COPY = (('favicon.ico', 'favicon.ico'),)

WEBASSETS = True
#DISPLAY_PAGES_ON_MENU = False
GETATTR = getattr

#import os
#with open(os.path.join(os.path.dirname(__file__), "content/old/archive-fragment.html")) as fp:
#    EXTRA_ARCHIVE = fp.read()
