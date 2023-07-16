import scrapy
from Douban.items import DoubanItem

class MovieSpider(scrapy.Spider):
    name = "movie"
    allowed_domains = ["douban.com"]
    start_urls = ["https://movie.douban.com/top250"]

    def parse(self, response):
        print(response.text)
        node_list =response.xpath('//*[@class="info"]')
        print(node_list)
        item = DoubanItem()
        for node in node_list:
            item['name']=node.xpath('./div[1]/a/span[1]/text()').extract_first()
            item['info']=str(node.xpath('./div[2]/p[1]/text()[1]').extract_first()).strip().replace('\xa0','')
            item['category']=str(node.xpath('./div[2]/p[1]/text()[2]').extract_first()).strip().replace('\xa0','')
            item['score']=node.xpath('./div[2]/div/span[2]/text()').extract_first()
            item['desc']=node.xpath('./div[2]/p[2]/span/text()').extract_first()
            item['link']=node.xpath('./div[1]/a/@href').extract_first()

            detail_url = response.urljoin(item['link'])
            print(detail_url)
            yield scrapy.Request(
                    url = detail_url,
                    callback = self.parse_detail,
                    meta={'item':item}
                    )
 
        #翻页的判断条件，如果能取到下一页的链接就递归调用自身解析数据。如果不能取到下一页的链接就结束递归。
        next_url=response.xpath('//*[@id="content"]/div/div[1]/div[2]/span[3]/a/@href').extract_first()
        if next_url!=None:
            next_url =response.urljoin(next_url)
            yield scrapy.Request(
                url = next_url,
                callback=self.parse
                )

    def parse_detail(self,response):
        item = response.meta['item']
        item['story'] = str(response.xpath('//*[@id="link-report-intra"]/span[1]/span/text()').extract()).strip().replace("'",'')
        item['review'] = str(response.xpath('//*[@id="hot-comments"]//span[@class="short"]//text()').extract()).strip().replace('\n','').replace("'",'')

        yield item
        