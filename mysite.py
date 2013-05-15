AUTHOR = u"Karla"
SITENAME = u"pitonisax"
SITEURL = 'http://pitonisax.pycourse.com'
RELATIVE_URLS = True

TIMEZONE = 'America/Los_Angeles'
ARTICLE_DIR = ('articles')
ARTICLE_EXCLUDES = ['pages']
ARTICLE_URL = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
DEFAULT_LANG = 'en'
DEFAULT_CATEGORY = 'notes'
PATH = 'src/'
OUTPUT_PATH = 'www/'
STATIC_PATHS = ['images']
DISQUS_SITENAME = "krpy"


SOCIAL = (('Karla\'s Site', 'http://pitonisax.wordpress.com/'),
          ('Karla\'s Twitter', 'http://twitter.com/pitonisax'),
          ('Liz\'s Site', 'http://www.eleddy.com'),
          ('Liz\'s Twitter', 'http://twitter.com/eleddy'),
          ('Kellan\'s Site', 'http://kellanjacobs.com'),
          ('Kellan\'s Twitter', 'http://twitter.com/kellanjacobs'),)


DEFAULT_PAGINATION = 10