#-*- coding = utf-8 -*-
#@Time : 2021/4/18 20:55
#@Author : linovce

import scrapy

class mingyan(scrapy.Spider):
    name = "csdn_spider"

    def start_requests(self):
        urls = [
            'https://blog.csdn.net/qq_35524157',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)  # 爬取到的页面如何处理？提交给parse方法处理

    def parse(self, response):
        blogIdList = response.css('div.article-item-box::attr(data-articleid)').extract()
        filename = 'CSDNSpider/spiders/blogIdList.txt'
        f = open(filename, "a+")
        for i in blogIdList:
            print(i)
            f.write(i)
            f.write('\n')  # 换行
        f.close()  # 关闭文件操作