# encoding: utf-8
import scrapy

from scrapy import Selector
from scrapy import Request
from pacong.items import MovieNews, MovieChina, MovieOuMei, MovieRiHan;


class DmozSpider(scrapy.Spider):
    name = "movie"
    start_urls = [
        "http://www.dytt8.net"
    ]
    url = "http://www.dytt8.net"
    xq_url = "http://www.ygdy8.net"

    def parse(self, response):
        selector = Selector(response)
        typeul = selector.xpath('//ul')
        types = typeul.xpath('li')
        for index, t in enumerate(types):
            href = t.xpath('a/@href').extract()
            title = t.xpath('a/text()').extract()
            if index < 5:
                href = href[0]
                title = title[0]

                if 'http://' in href:
                    if href == "http://www.ygdy8.net/html/gndy/index.html":
                        pass
                    else:
                        yield Request(href, callback=self.parseItems, meta={'title': title,'url':href})
                else:
                    yield Request(self.xq_url + href, callback=self.parseItems, meta={'title': title,'url':self.xq_url+href})

    def parseItems(self, response):

        title = response.meta['title']
        urll = response.meta['url']

        selector = Selector(response)

        nextHrefs = selector.xpath('//select[@name="sldd"]')
        # for next in nextHrefs:
        hrefs = nextHrefs.xpath('option/@value').extract()
        for href in hrefs:
            nextUrl = urll[0:urll.rindex('/') + 1] + href
            yield Request(nextUrl, callback=self.parseItems, meta={'title': title, 'url': nextUrl})

        movies = selector.xpath('//div[@class="co_content8"]')
        mov = movies.xpath('ul/td/table')  # 审查元素和直接看网页源代码不一样，，，审查元素没有td标签，艹。
        for movie in mov:
            name = movie.xpath('tr/td/b/a/text()').extract()
            href = movie.xpath('tr/td/b/a/@href').extract()
            time = movie.xpath('tr/td/font/text()').extract()
            zonghe = movie.xpath('tr/td[@colspan="2"]/text()').extract()

            name = name[len(name)-1]
            href = href[len(href)-1]
            time = time[0]
            zonghe = zonghe[0]
            yield Request(self.xq_url + href, callback=self.parseDetail, meta={'name': name, "time": time, 'title': title, 'zonghe': zonghe})

    def parseDetail(self,response):
        selector = Selector(response)
        zoom = selector.xpath('//div[@id="Zoom"]')
        imgs = zoom.xpath('td/img/@src').extract()
        img = ','.join(imgs)
        downloadUrl = zoom.xpath('td/table/tbody/tr/td/a/text()').extract()

        title = response.meta['title']
        name = response.meta['name']
        time = response.meta['time']
        zonghe = response.meta['zonghe']
        if downloadUrl:
            downloadUrl = downloadUrl[0]

        if title == u"最新影片":
            movieNews = MovieNews()
            movieNews['movie_name'] = name
            movieNews['movie_time'] = time
            movieNews['movie_image'] = img
            movieNews['movie_abstract'] = zonghe
            movieNews['movie_download'] = downloadUrl
            yield movieNews
        elif title == u"其它电影":
            movieRh = MovieRiHan()
            movieRh['movie_name'] = name
            movieRh['movie_time'] = time
            movieRh['movie_image'] = img
            movieRh['movie_abstract'] = zonghe
            movieRh['movie_download'] = downloadUrl
            yield movieRh
        elif title == u"欧美电影":
            movieOm = MovieOuMei()
            movieOm['movie_name'] = name
            movieOm['movie_time'] = time
            movieOm['movie_image'] = img
            movieOm['movie_abstract'] = zonghe
            movieOm['movie_download'] = downloadUrl
            yield movieOm
        elif title == u"国内电影":
            movieCh = MovieChina()
            movieCh['movie_name'] = name
            movieCh['movie_time'] = time
            movieCh['movie_image'] = img
            movieCh['movie_abstract'] = zonghe
            movieCh['movie_download'] = downloadUrl
            yield movieCh
