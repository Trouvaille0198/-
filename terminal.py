from lianjia_crawler import LianjiaCrawler

city = input('输入城市：')
location = input('输入地区：')
page = input('输入爬取页数：')
crawler = LianjiaCrawler(city, location, page)
crawler.gogogo()
