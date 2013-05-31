# -*- coding: utf-8 -*-
from __future__ import unicode_literals

AUTHOR = 'Dong Weiming'
SITENAME = "小明明s Github"
SITEURL = 'http://dongweiming.github.io'
TIMEZONE = "Asia/Shanghai"

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

GITHUB_URL = 'http://github.com/dongweiming/'
#GOOGLE_ANALYTICS = ''
DISQUS_SITENAME = "sgithub"
PDF_GENERATOR = False
REVERSE_CATEGORY_ORDER = True
LOCALE = "zh_CN.UTF-8"
DEFAULT_PAGINATION = 4
DEFAULT_DATE = (2013, 5, 15, 14, 1, 1)

FEED_ALL_RSS = 'feeds/all.rss.xml'
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'

LINKS = (('小明明s à domicile', 'http://www.dongwm.com'),)

SOCIAL = (('twitter', 'http://twitter.com/dongweiming'),
          ('github', 'http://github.com/orzrd'),
          ('github', 'http://github.com/dongweiming'),)

# global metadata to all the contents
DEFAULT_METADATA = (('yeah', 'it is'),)

# static paths will be copied under the same name
STATIC_PATHS = ["pictures", ]

# A list of files to copy from the source to the destination
FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)

# custom page generated with a jinja2 template
#TEMPLATE_PAGES = {'pages/jinja2_template.html': 'jinja2_template.html'}

# foobar will not be used, because it's not in caps. All configuration keys
# have to be in caps
foobar = "barbaz"
