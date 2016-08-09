# coding=utf-8

import urllib2, re, requests

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",
    "Referer": "http://www.dbmeinv.com/dbgroup/show.htm?cid=6&pager_offset=1"
}


def gethtml(url):
    response = urllib2.Request(url, headers=headers)
    html = urllib2.urlopen(response).read()
    return html


def getimage(html):
    reg = r'src="(.+?\.jpg)" />'
    imgre = re.compile(reg)
    imgurl_list = re.findall(imgre, html)
    for imgurl in imgurl_list:
        with open('E://python//scrapy_crawl//qiaotunmei//%s' % imgurl[-15:], "wb") as laurence:
            laurence.write(requests.get(imgurl).content)


for x in range(1, 115):
    getimage(gethtml("http://www.dbmeinv.com/dbgroup/show.htm?cid=6&pager_offset=%s" % x))
    print "正在爬取翘臀妹第%s页，请稍安勿躁..." % x
print "爬完收工"
if __name__ == '__main__':
    pass
