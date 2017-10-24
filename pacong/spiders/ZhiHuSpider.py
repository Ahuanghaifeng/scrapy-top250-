# encoding: utf-8
import scrapy

from scrapy import Selector, FormRequest
from pacong.items import ZhiHuItem
from pacong.items import ZhihuItem
from scrapy import Request


class ZhiHuSpider(scrapy.Spider):
    name = "zhihu"

    start_urls = [
        "https://www.zhihu.com"
    ]
    url = "https://www.zhihu.com"

    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4",
        "Connection": "keep-alive",
        "Content-Type": " application/x-www-form-urlencoded; charset=UTF-8",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Referer": "http://www.zhihu.com/",
    }

    cookies = {
        "q_c1":"5b3005ad8da14749906c352ee9ef1209|1506064742000|1506064742000",
        "d_c0":"AJBCu7kwagyPTnFkFomUc83yzQ9KcBiUtTM = | 1506064742",
        "_zap":"fd983c6b-8990-4281-94cc-8a0ef9f4e5bb",
        "aliyungf_tc":"AQAAAGFBeH5GNwwANtSBtzxErd9IIzPE",
        "r_cap_id":"YzNmYTAzMDI1YTY0NGVmYjkzN2NkM2Q2YjM3ZWJjNmM = | 1507541608 | 168cb3ed76f135040009e3edb00ae1923d72dc58",
        "cap_id":"OTM0MjYwZjBmMzNlNGI4YWIzNzQzMTQwZjZmZTI5ODk = | 1507541608 | bf0ee8ef374808051623795181b37f929991ba3b",
        "_xsrf":"da339699-e918-413f-bfdb-b93108fdfb56",
        "l_cap_id":"ZDgwYzc3YTQ0YWI1NDlmZmJhNGIxZWY1MWYyNjZkODY = | 1507541639 | b9d3705a7a1a9ad3d523d93f7a8030e79bb3e457",
        "__utma":"51854390.1681012169.1506064676.1506394038.1507541514.3",
        "__utmb":"51854390.0.10.1507541514",
        "__utmc":"51854390",
        "__utmz":"51854390.1507541514.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic",
        "__utmv":"51854390.000--|2=registration_date=20150915=1^3=entry_date=20170922=1"
    }

    def start_requests(self):
        return [Request("https://www.zhihu.com/",
                        cookies=self.cookies,
                        meta={'cookiejar': 1},
                        callback=self.post_login)]  # 重写了爬虫类的方法, 实现了自定义请求, 运行成功后会调用callback回调函数

    # FormRequeset
    def post_login(self, response):
        # 下面这句话用于抓取请求网页后返回网页中的_xsrf字段的文字, 用于成功提交表单
        xsrf = Selector(response).xpath('//input[@name="_xsrf"]/@value').extract()[0]
        # FormRequeset.from_response是Scrapy提供的一个函数, 用于post表单
        # 登陆成功后, 会调用after_login回调函数
        return [FormRequest(url="https://www.zhihu.com/login/email",
                            meta={'cookiejar': response.meta['cookiejar']},
                            headers=self.headers,
                            formdata={'_xsrf': xsrf, 'email': '1490738477@qq.com',
                                      'password': 'H9009910480'},
                            callback=self.after_login,
                            dont_filter=True)]

    def after_login(self, response):
        print response.url
        for url in self.start_urls:
            yield self.make_requests_from_url(url)

    def parse(self, response):
        problem = Selector(response)
        item = ZhihuItem()
        item['url'] = response.url
        name = problem.xpath('//[@id="root"]/div/main/div/div/div[1]/div[2]/div/div[2]/div/div[2]/div[1]/div/div/meta[1]').extract()
        print name
        # item['title'] = problem.xpath('//h2[@class="zm-item-title zm-editable-content"]/text()').extract()
        # item['description'] = problem.xpath('//div[@class="zm-editable-content"]/text()').extract()
        # item['answer'] = problem.xpath('//div[@class=" zm-editable-content clearfix"]/text()').extract()
        # return item
