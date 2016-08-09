# coding=utf-8

from douban_crawl_class import Douban_crawl

meituikong = Douban_crawl("http://www.dbmeinv.com/dbgroup/show.htm?cid=3&pager_offset=1","meitui")

meituikong.start_crawl()

if __name__ == '__main__':
    pass