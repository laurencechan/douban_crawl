# coding=utf-8

from Douban_spider import Douban_spide

jiganglifan = Douban_spide(
    "https://movie.douban.com/celebrity/1318109/photos/?type=C&start=40&sortby=vote&size=a&subtype=a", 'xiaoqiai', 5)

jiganglifan.start_crawl()

if __name__ == '__main__':
    pass
