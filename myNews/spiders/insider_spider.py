from scrapy.contrib.spiders import XMLFeedSpider
from myNews.items import MynewsItem
from scrapy import Request

class InsiderSpider(XMLFeedSpider):
  name = 'insider'
  allowed_domains = ["www.themalaysianinsider.com"]
  start_urls = ['http://www.themalaysianinsider.com/rss/malaysia']

  def parse_node(self, response, node):
    item = MynewsItem()
    item['host'] = 'www.themalaysianinsider.com'
    item['url'] = node.xpath('link/text()').extract()[0].strip()
    item['title'] = node.xpath('title/text()').extract()[0].strip()
    item['category'] = 'news'
    request = Request(item['url'] , callback=self.parse_content)
    request.meta['item'] = item
    yield request

  def parse_content(self, response):
    item = response.meta['item']
    item['news'] = response.css('article').extract()[0]
    item['date'] = response.css('p.datetime').xpath('text()').extract()[0]
    return item







