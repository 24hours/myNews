# -*- coding: utf-8 -*-

# Scrapy settings for myNews project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'myNews'

SPIDER_MODULES = ['myNews.spiders']
NEWSPIDER_MODULE = 'myNews.spiders'


ITEM_PIPELINES = {
    'myNews.pipelines.DupePipeline': 100,
    'myNews.pipelines.DatePipeline': 100,
    'myNews.pipelines.ContentPipeline': 300,
}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'myNews (+http://www.yourdomain.com)'
star = {}
star['gigya_key'] = '2_K-akhSiZodjV_QHhH3XwXEtdC1Z10sO7a5tTJBqUUGKwys4YQ4b1uDKVru6_Y6td'



# Nation
# Regional
# World
# Environment
# Education
# In Other Media
