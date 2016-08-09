# coding=utf-8

from Douban_spider import Douban_spide

doubancrawl = Douban_spide(
    "https://movie.douban.com/celebrity/1054453/photos/?type=C&start=0&sortby=vote&size=a&subtype=a", 'Scarlett', 57)

doubancrawl.start_crawl()

if __name__ == '__main__':
    pass
