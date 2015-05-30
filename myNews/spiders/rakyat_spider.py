from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor
from myNews.items import MynewsItem

class RakyatSpider(CrawlSpider):
  name = 'rakyat'
  allowed_domains = ["www.therakyatpost.com"]
  start_urls = ['http://www.therakyatpost.com/category/news/']

  rules = (
      Rule(LinkExtractor(allow=('http://www.therakyatpost.com/news/', )), callback='parse_item'),
  )

  def parse_item(self, response):
    item = MynewsItem()
    item['host'] = 'www.therakyatpost.com'
    item['url'] = response.url
    item['title'] = response.css("h1.singleTitle").xpath('text()').extract()[0]
    item['date'] = response.css('p.singleHeaderTime').xpath('text()').extract()[0]
    item['news'] = response.css('div.singleContent').extract()[0]
    item['category'] = 'news' # might as well
    return item







