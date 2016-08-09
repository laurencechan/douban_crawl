# coding=utf-8
import urllib
import time
import urllib2
import re
import requests

headers = {
    "cookie": 'JSESSIONID=F982BD96AC84C4090D186BBD3B8F9269; BDTUJIAID=54a6915268252b1e49f56619ea789772; Hm_lvt_65499fd57541d09e46def2791033d87f=1470477116,1470480078; Hm_lpvt_65499fd57541d09e46def2791033d87f=1470480270; CNZZDATA1254770214=1146773404-1470472398-null%7C1470477817; jiathis_rdc=%7B%22http%3A//www.dbmeinv.com/dbgroup/887345%22%3A%220%7C1470480269912%22%7D',
    "referer": 'http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=1',
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}


def getHtml(url):
    request = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(request).read()
    return html


def getImage(html):
    reg = r'src="(.+?\.jpg)" />'
    imgre = re.compile(reg)
    print type(imgre)
    imglist = re.findall(imgre, html)
    # imglist_new = []
    # for i in imglist:
    #     i = i.replace('thumb', 'raw')
    #     imglist_new.append(i)
    # print imglist_new
    # x = 0
    for imgurl in imglist:
        with open('E://python//scrapy_crawl//lifan//%s' % imgurl[-15:], "wb") as ryan:
            ryan.write(requests.get(imgurl).content)

            # urllib.urlretrieve(imgurl, 'E://python//scrapy_crawl//lifan//%s'% imgurl[-15:])
            # time.sleep(0.1)
            # x += 1


for x in range(697):
    getImage(getHtml('http://www.dbmeinv.com/dbgroup/show.htm?cid=2&pager_offset=%s' % x))
    print "正在爬取第%s页" % x

if __name__ == '__main__':
    pass
# https://img3.doubanio.com/view/photo/raw/public/p2359332002.jpg
# https://img3.doubanio.com/view/photo/thumb/public/p2359332002.jpg
