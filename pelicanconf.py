#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = u'Raul E. Lopez Briega'
SITENAME = u'Raul E. Lopez Briega'
SITESUBTITLE = u'Matemáticas, análisis de datos y python'
SITEURL = ''
DESCRIPTION = u'Todo sobre python aplicado a las ciencias. Análisis de datos, matemáticas, machine learning, inteligencia artificial, probabilidad y estadística'

TIMEZONE = 'America/Argentina/Buenos_Aires'

DEFAULT_LANG = u'es'

# Feed generation is usually not desired when developing
#FEED_ALL_ATOM = None
#CATEGORY_FEED_ATOM = None
#TRANSLATION_FEED_ATOM = None

# Set the article URL
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

MENUITEMS = [('About', '/pages/acerca-de-mi.html'),
             ('Home Page', '/index.html'),             
             ('Archives', '/archives.html'),
             ('Mi otro Blog', 'http://relopezbriega.com.ar/'),
             ('IAAR Book', 'https://iaarbook.github.io/'),
             ('2048', '/2048/'),
             ('Contacto', '/pages/contacto.html')]

# Blogroll
LINKS =  (('Mi otro blog', 'http://relopezbriega.com.ar'),
          ('IAAR Book', 'https://iaarbook.github.io/'),
		  ('Pelican', 'http://getpelican.com/'),
          ('Python.org', 'http://python.org/'),
          ('Jinja2', 'http://jinja.pocoo.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/relopezbriega'),
          ('linkedin', 'https://ar.linkedin.com/in/relopezbriega'),
          ('github', 'https://github.com/relopezbriega/'),)

GITHUB_URL = 'https://github.com/relopezbriega/'

DEFAULT_PAGINATION = 10

THEME = 'pelican-octopress-theme/'

DISPLAY_PAGES_ON_MENU = False

PLUGIN_PATHS = ['pelican-plugins']
#PLUGINS = ['summary', 'liquid_tags.img', 'liquid_tags.video',
#           'liquid_tags.include_code', 'liquid_tags.notebook',
#           'liquid_tags.literal']

PLUGINS = ['summary', 'liquid_tags.notebook', 'tipue_search']

STATIC_PATHS = ['images', 'figures', 'downloads', 'pages', 
                'favicon.png', 'matrix', '2048']

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# The theme file should be updated so that the base header contains the line:
#
#  {% if EXTRA_HEADER %}
#    {{ EXTRA_HEADER }}
#  {% endif %}
# 
# This header file is automatically generated by the notebook plugin
if not os.path.exists('_nb_header.html'):
    import warnings
    warnings.warn("_nb_header.html not found.  "
                  "Rerun make html to finalize build.")
else:
	EXTRA_HEADER = open('_nb_header.html').read() #.decode('utf-8')

# Sharing
TWITTER_USER = 'relopezbriega'
GOOGLE_PLUS_USER = 'relopezbriega'
GOOGLE_PLUS_ONE = True
GOOGLE_PLUS_HIDDEN = False
FACEBOOK_LIKE = True
TWITTER_TWEET_BUTTON = True
TWITTER_LATEST_TWEETS = True
TWITTER_FOLLOW_BUTTON = True
TWITTER_TWEET_COUNT = 3
TWITTER_SHOW_REPLIES = 'false'
TWITTER_SHOW_FOLLOWER_COUNT = 'true'


# RSS/Atom feeds
FEED_DOMAIN = SITEURL
FEED_ATOM = 'atom.xml'


# Search
#SEARCH_BOX = True
TIPUE_SEARCH = True

#TEMPLATE_PAGES = {
#        'search.html': 'search.html',
#        }

DIRECT_TEMPLATES = ['index', 'tags', 'categories', 'authors', 'archives', 'search']

#INDEX_SAVE_AS = 'blog_index.html'
