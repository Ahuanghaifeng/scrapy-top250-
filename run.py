from scrapy import cmdline

cmdline.execute("scrapy crawl dmoz".split())
#scrapy crawl douban -o items.json -t json
#scrapy crawl douban -o items.csv -t csv