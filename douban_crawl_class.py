# coding=utf-8
import requests, re, urllib2, os


class Douban_crawl():
    def __init__(self, url, name):
        self.url = url
        self.name = name

    def __make_dir(self):
        # 在F盘创建一个以name命名的文件夹用来存放爬取的图片
        os.makedirs("F://img//%s" % self.name)
        pass

    def get_route(self):
        # 返回文件夹图径，以备使用
        return "F://img//%s" % self.name

    def get_html(self, url):
        # 获取目标网页的html文件（str）
        response = urllib2.Request(url)
        html = urllib2.urlopen(response).read()
        return html

    def get_image(self, html):
        # 解析从html文档，获取图片地址并保存到本地文件夹
        reg = r'src="(.+?\.jpg)" />'  # 匹配图片的正则
        imgre = re.compile(reg)  # 将正则表达式编译成pattern对象
        imgurl_list = re.findall(imgre, html)  # 获取 html文本中所有与 imgre pattern 匹配的文本列表
        for i in imgurl_list:
            with open(self.get_route() + "//%s" % i[-15:], "wb") as f:
                f.write(requests.get(i).content)

    def start_crawl(self):
        # 启动爬虫
        self.__make_dir() # 创建存储文件夹
        url_process = self.url.split("=") # 分解目标url
        for x in range(1, 1000):
            print "正在爬取第%s页..." % x
            url_new = url_process[0] + "=" + url_process[1] + "=" + str(x)  # 重组获得下一页的目标url
            html = self.get_html(url_new)
            self.get_image(html)
        print "Finished all，good job!!!!!"
