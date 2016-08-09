# coding=utf-8

from Douban_spider import Douban_spide

doubancrawl = Douban_spide(
    "https://movie.douban.com/celebrity/1344112/photos/?type=C&start=40&sortby=vote&size=a&subtype=a", 'liuaihecai', 2)

doubancrawl.start_crawl()

if __name__ == '__main__':
    pass
