# coding=utf-8

from Douban_spider import Douban_spide

# https://movie.douban.com/celebrity/1318109/photos/?type=C&start=0&sortby=vote&size=a&subtype=a (日本写真女星筱崎爱)


star_favour = Douban_spide(1318109, 'xiaoqiai_test_1', 5)

star_favour.start_crawl()

if __name__ == '__main__':
    pass
