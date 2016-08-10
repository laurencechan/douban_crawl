# coding=utf-8
import requests, re, urllib2, os

headers = {
    "referer": "https://movie.douban.com/celebrity/1348382/photos/?type=C&start=0&sortby=vote&size=a&subtype=a",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36",# 自己使用的浏览器
    "Cookie": 'bid = Bgywljn1xF0;ll = "118146";gr_user_id = 6686bb9c - b4ef - 4b18 - 939f - 4e78f8d8894d;viewed = "1985875";ps = y;ct = y;ap = 1;_ga = GA1.2.454041090.1465957319;dbcl2 = "50144819:bpy9uZi6Xo0";ck = kFvi;__utmt = 1;_vwo_uuid_v2 = B30AC40B221A4FE539E42DBBE369B97A | 2347d7f84d94228e2c3427da5a24ebfe;_pk_ref.100001.4cf6 = % 5B % 22 % 22 % 2C % 22 % 22 % 2C1470702514 % 2C % 22https % 3A % 2F % 2Fwww.douban.com % 2F % 22 % 5D;push_noty_num = 0;push_doumail_num = 0;__utma = 30149280.454041090.1465957319.1470624031.1470702511.35;__utmb = 30149280.2.10.1470702511;__utmc = 30149280;__utmz = 30149280.1470487004.33.20.utmcsr = douban.com | utmccn = (referral) | utmcmd = referral | utmcct = / group / topic / 76597301 /;__utmv = 30149280.5014;__utma = 223695111.803188614.1465957319.1470624897.1470702514.23;__utmb = 223695111.0.10.1470702514;__utmc = 223695111;__utmz = 223695111.1470702514.23.16.utmcsr = douban.com | utmccn = (referral) | utmcmd = referral | utmcct = /; _pk_id.100001.4cf6 = 8ef1bd7f0403cc70.1465957319.23.1470702549.1470625514.;_pk_ses.100001.4cf6 = *',
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch"
}


class Douban_spide():
    def __init__(self, number, name, page):
        # https://movie.douban.com/celebrity/1348382/photos/
        self.number = number   # 对应右侧URL中中间的七位数字（每一位豆瓣影人都有拥有七位独一无二的数字，其余内容都相同的URL） https://movie.douban.com/celebrity/1348382/photos/?type=C&start=0&sortby=vote&size=a&subtype=a
        self.name = name        # 本地存放图片文件夹的名称，可以用明星的名字命名
        self.page = page        # 影人豆瓣相册的页数

    def get_url(self):
        # 根据number获取目标URL
        return "https://movie.douban.com/celebrity/" + str(self.number) + "/photos/?type=C&start=0&sortby=vote&size=a&subtype=a"

    def __make_dir(self):
        # 在F盘创建一个以name命名的文件夹用来存放爬取的图片
        os.makedirs("F://img//%s" % self.name)
        pass

    def range_num(self):
        # 通过页数获取range数
        return 40 * self.page

    def header_referer_change(self):
        # 根据不同的URL得到不同的头文件 referer
        headers["referer"] = self.get_url()
        return headers

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
        reg = r'src="(.+?\.jpg)" class'  # 匹配图片的正则
        imgre = re.compile(reg)  # 将正则表达式编译成pattern对象
        imgurl_list = re.findall(imgre, html)  # 获取 html文本中所有与 imgre pattern 匹配的文本列表
        for i in imgurl_list:
            i = i.replace("thumb", "raw")
            with open(self.get_route() + "//%s" % i[-15:], "wb") as f: # 在目标文件夹创建文件，并以图片后14位命名
                f.write(requests.get(i, headers=self.header_referer_change()).content) # 将jpg图片写入在目标文件夹创建的文件


    def start_crawl(self):
        # 启动爬虫
        self.__make_dir()  # 创建存储文件夹
        url_process = self.get_url().split("&", 2)     # 分解目标url
        for x in range(0, self.range_num(), 40):
            print "正在爬取%s第%s页..." % (self.name, x / 40)
            url_new = url_process[0] + "&" + "start=" + str(x) + "&" + url_process[2]  # 重组获得下一页的目标url
            html = self.get_html(url_new)
            self.get_image(html)
        print "Finished all，good job!!!!!"


if __name__ == '__main__':
    pass


"https://img3.doubanio.com/view/photo/thumb/public/p2363884304.jpg"
"https://img3.doubanio.com/view/photo/raw/public/p2363884304.jpg"
