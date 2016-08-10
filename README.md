# douban_crawl
豆瓣影人图片爬虫

豆瓣所有影人的相册链接均如下模式
https://movie.douban.com/celebrity/1333229/photos/?type=C&start=40&sortby=vote&size=a&subtype=a
不同处只是中间的数字串，即上例中的“1333229” 。我们称为url识别码。

本爬虫类 只需实例化一个豆瓣影人 mizuki_hoshina = Douban_spider() 
并传入三个参数，分别是url识别码，文件夹名称，以及相册页数
我们以上边的链接星名美津纪（mizuki_hoshina）为例：

mizuki_hoshina = Douban_spider(1333229, mizuki_hoshina, 2)
然后执行：
mizuki_hoshina.start_crawl()
宅男腐女人喜欢的美图就源源不断的进入我们的电脑了~
