from scrapy import cmdline

cmdline.execute("scrapy crawl movie".split())
#scrapy crawl douban -o items.json -t json
#scrapy crawl douban -o items.csv -t csv