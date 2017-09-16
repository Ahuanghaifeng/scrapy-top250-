# encoding: utf-8
import scrapy

from scrapy import Selector
from pacong.items import PacongItem
from scrapy import Request

class DmozSpider(scrapy.Spider):

    name = "dmoz"

    start_urls = [
        "https://movie.douban.com/top250"
    ]
    url = "https://movie.douban.com/top250"

    def parse(self, response):
        douban = PacongItem()
        selector = Selector(response)
        Movies = selector.xpath('//div[@class = "info"]') #//根节点 [@]提取属性内容
        for eachMovie in Movies:
            title = eachMovie.xpath('div[@class="hd"]/a/span/text()').extract()
            fulltitle = ''
            for each in title:
                fulltitle += each
            movieInfo = eachMovie.xpath('div[@class = "bd"]/p/text()').extract()
            star = eachMovie.xpath('div[@class = "bd"]/div[@class = "star"]/span[@class = "rating_num"]/text()').extract()[0]
            quote = eachMovie.xpath('div[@class = "bd"]/p[@class = "quote"]/span/text()').extract()
            if quote: #判断quote是否为空
                quote = quote[0]
            else:
                quote = ''
            douban['title'] = fulltitle
            douban['movieInfo'] = ';'.join(movieInfo)
            douban['star'] = star
            douban['quote'] = quote
            yield douban
        nextLink = selector.xpath('//span[@class = "next"]/a/@href').extract()
        if nextLink:
            nextLink = nextLink[0]
            print nextLink
            yield Request(self.url + nextLink, callback=self.parse)