# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter
#from .myextend import pro   
from Douban.settings import USER_AGENT_LIST
from Douban.settings import PROXY_LIST

def user_agent(ual_filename):
    result=[]
    with open(ual_filename, encoding='utf-8') as f:
        for line in f:
            result.append(line.strip('\n').split(',')[0])
    return result

useragnetfile = 'F:\\淮北理工学院工作\\BaiduSyncdisk\\PythonCode\\Spider\\scrapy\\Douban\\Douban\\user_agent.txt'

class RandomUserAgent(object):
    def process_request(self,request,spider):
        #print(request.headers['user_agent'])
        AGENT_LIST = user_agent(useragnetfile)
        ub =random.choice(AGENT_LIST)
        ua =random.choice(USER_AGENT_LIST)
        request.headers['user_agent'] = ub

# class ProxyDownloaderMiddleware:

#     def process_request(self, request, spider):
#         proxy = random.choice(pro.proxy_list)

#         # 用户名密码认证(私密代理/独享代理)
#         username = "d1389322591"
#         password = "e4p2pjed"
#         request.meta['proxy'] = "http://%(user)s:%(pwd)s@%(proxy)s/" % {"user": username, "pwd": password, "proxy": proxy}

#         # 白名单认证(私密代理/独享代理)
#         # request.meta['proxy'] = "http://%(proxy)s/" % {"proxy": proxy}
#         return None

        
class RandomProxy(object):
    def process_request(self, request, spider):
        proxy = random.choice(PROXY_LIST)
        print(proxy)
        if 'user_passwd' in proxy:
            #对账号密码进行编码
            b64_up = base64.b64encode(proxy['user_passwd'].encode())
            #设置认证
            request.headers['Proxy-Authorization'] = 'Basic ' + b64_up.decode()
            #设置代理
            request.meta['proxy'] = proxy['ip_port']
        else:
            #设置代理
            request.meta['proxy'] = proxy['ip_port']
       


# class DoubanSpiderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the spider middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_spider_input(self, response, spider):
#         # Called for each response that goes through the spider
#         # middleware and into the spider.

#         # Should return None or raise an exception.
#         return None

#     def process_spider_output(self, response, result, spider):
#         # Called with the results returned from the Spider, after
#         # it has processed the response.

#         # Must return an iterable of Request, or item objects.
#         for i in result:
#             yield i

#     def process_spider_exception(self, response, exception, spider):
#         # Called when a spider or process_spider_input() method
#         # (from other spider middleware) raises an exception.

#         # Should return either None or an iterable of Request or item objects.
#         pass

#     def process_start_requests(self, start_requests, spider):
#         # Called with the start requests of the spider, and works
#         # similarly to the process_spider_output() method, except
#         # that it doesn’t have a response associated.

#         # Must return only requests (not items).
#         for r in start_requests:
#             yield r

#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)


# class DoubanDownloaderMiddleware:
#     # Not all methods need to be defined. If a method is not defined,
#     # scrapy acts as if the downloader middleware does not modify the
#     # passed objects.

#     @classmethod
#     def from_crawler(cls, crawler):
#         # This method is used by Scrapy to create your spiders.
#         s = cls()
#         crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
#         return s

#     def process_request(self, request, spider):
#         # Called for each request that goes through the downloader
#         # middleware.

#         # Must either:
#         # - return None: continue processing this request
#         # - or return a Response object
#         # - or return a Request object
#         # - or raise IgnoreRequest: process_exception() methods of
#         #   installed downloader middleware will be called
#         return None

#     def process_response(self, request, response, spider):
#         # Called with the response returned from the downloader.

#         # Must either;
#         # - return a Response object
#         # - return a Request object
#         # - or raise IgnoreRequest
#         return response

#     def process_exception(self, request, exception, spider):
#         # Called when a download handler or a process_request()
#         # (from other downloader middleware) raises an exception.

#         # Must either:
#         # - return None: continue processing this exception
#         # - return a Response object: stops process_exception() chain
#         # - return a Request object: stops process_exception() chain
#         pass

#     def spider_opened(self, spider):
#         spider.logger.info("Spider opened: %s" % spider.name)
