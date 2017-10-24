# encoding: utf-8
import scrapy

from scrapy import Selector
from pacong.items import MovieHome
from scrapy import Request

class DmozSpider(scrapy.Spider):

    name = "movie"

    start_urls = [
        "http://www.dytt8.net/"
    ]
    url = "http://www.dytt8.net/"

    def parse(self, response):
        movies = MovieHome()
        selector = Selector(response)
        sMovies = selector.xpath('//tr') #//根节点 [@]提取属性内容
        for movie in sMovies:
            tds = movie.xpath('td')
            if len(tds) == 2:
                # title = tds[0].xpath('a/text()').extract()
                href = tds[0].xpath('a/@href').extract()
                # if title and len(title)>1:
                #     title = title[1]
                # time = tds[1].xpath('font/text()').extract()
                # movies['name'] = title
                # movies['time'] = time[0] #time是list,转字符串
                # yield movies

                if href:
                    print href[1]
                    # yield Request(self.url+href, callback=self.parseDetail)


    def parseDetail(self, response):
        movies = MovieHome()
        selector = Selector(response)

        # for eachMovie in sMovies:
        #     title = eachMovie.xpath('td/a/span/text()').extract()
        #     time  = eachMovie.xpath('td/a/span/text()').extract()
        #     print title
        #     print time
            # for each in title:
            #     fulltitle += each
            # movieInfo = eachMovie.xpath('div[@class = "bd"]/p/text()').extract()
            # star = eachMovie.xpath('div[@class = "bd"]/div[@class = "star"]/span[@class = "rating_num"]/text()').extract()[0]
            # quote = eachMovie.xpath('div[@class = "bd"]/p[@class = "quote"]/span/text()').extract()
            # if quote: #判断quote是否为空
            #     quote = quote[0]
            # else:
            #     quote = ''

            # movies['time'] =

        # nextLink = selector.xpath('//span[@class = "next"]/a/@href').extract()
        # if nextLink:
        #     nextLink = nextLink[0]
        #     print nextLink
        #     yield Request(self.url + nextLink, callback=self.parse)