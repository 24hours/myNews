from scrapy import Request
from scrapy.contrib.spiders import XMLFeedSpider
from myNews.items import MynewsItem

class StarFeedSpider(XMLFeedSpider):
  name = 'star'
  allowed_domains = ['www.thestar.com.my']
  
  start_urls = ['http://www.thestar.com.my/RSS/News/Nation', 
                'http://www.thestar.com.my/RSS/News/Regional', 
                'http://www.thestar.com.my/RSS/News/World', 
                'http://www.thestar.com.my/RSS/News/Environment', 
                'http://www.thestar.com.my/RSS/News/Education']

  def parse_node(self, response, node):
    item = MynewsItem()
    item['host'] = 'www.thestar.com.my'
    item['url'] = node.xpath('link/text()').extract()[0].strip()
    item['title'] = node.xpath('title/text()').extract()[0].strip()
    item['date'] = node.xpath('pubDate/text()').extract()[0].strip()
    request =  Request(item['url'] , callback=self.parse_content)
    request.meta['item'] = item
    return request

  def parse_content(self, response):
    item = response.meta['item']
    item['category'] = response.css('p.breadcrumbs').css('a').xpath('text()').extract()[2]
    item['news'] = response.css('div.story').extract()[0]
    return item