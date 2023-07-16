# Scrapy settings for Douban project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "Douban"

SPIDER_MODULES = ["Douban.spiders"]
NEWSPIDER_MODULE = "Douban.spiders"


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "Douban (+http://www.yourdomain.com)"
#USER_AGENT = "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML like Gecko) Chrome/19.0.1055.1 Safari/535.24"
USER_AGENT_LIST =[
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML like Gecko) Chrome/22.0.1207.1 Safari/537.1',
'Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML like Gecko) Chrome/20.0.1132.57 Safari/536.11',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML like Gecko) Chrome/20.0.1092.0 Safari/536.6',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML like Gecko) Chrome/20.0.1090.0 Safari/536.6',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML like Gecko) Chrome/19.77.34.5 Safari/537.1',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.9 Safari/536.5',
'Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML like Gecko) Chrome/19.0.1084.36 Safari/536.5',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1063.0 Safari/536.3',
'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1063.0 Safari/536.3',
'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1063.0 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1062.0 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1062.0 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1061.1 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1061.1 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1061.1 Safari/536.3',
'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML like Gecko) Chrome/19.0.1061.0 Safari/536.3',
'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML like Gecko) Chrome/19.0.1055.1 Safari/535.24',
'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML like Gecko) Chrome/19.0.1055.1 Safari/535.24'
]
# Obey robots.txt rules
ROBOTSTXT_OBEY = False
#LOG_LEVEL = 'WARNING'

# RETRY_ENABLE = True
# RETRY_TIMES = 10
# DOWNLOAD_TIMEOUT = 10

PROXY_LIST=[
{"ip_port":"122.239.152.93:19649"},
{"ip_port":"114.220.38.60:16529"},
{"ip_port":"175.155.189.104:15542"},
{"ip_port":"1.198.72.188:18790"},
{"ip_port":"110.83.146.60:19907"},
{"ip_port":"125.117.192.225:19179"},
# {"ip_port":"110.243.7.228:9999"},
# {"ip_port":"39.137.69.7:80"},
# {"ip_port":"121.232.148.106:9000"}
]

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    "Douban.middlewares.DoubanSpiderMiddleware": 543,   
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "Douban.middlewares.RandomUserAgent": 543,
   "Douban.middlewares.RandomProxy": 400,
   #"Douban.middlewares.ProxyDownloaderMiddleware": 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "Douban.pipelines.DoubanPipeline": 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"