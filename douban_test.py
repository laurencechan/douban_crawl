import requests

Headers = {
    "authority": "img3.doubanio.com",
    "method": "GET",
    "path": "/view/photo/raw/public/p2350382070.jpg",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "accept-encoding": "gzip, deflate, sdch",
    "accept-language": 'zh-CN,zh;q=0.8,en;q=0.6',
    "cache-control": 'max-age=0',
    "cookie": 'bid=jT_6KJrVtwI',
    "if-modified-since": 'Wed, 21 Jan 2004 19:51:30 GMT',
    "referer": 'https://movie.douban.com/celebrity/1348382/photo/2350382070/',
    "upgrade-insecure-requests": 1,
    "user-agent": 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}
url = 'https://img3.doubanio.com/view/photo/raw/public/p2350382070.jpg'
# url = 'https://img3.doubanio.com/view/photo/photo/public/p2350382070.jpg'

r = requests.get(url, verify=False)
with open("lallala.jpg", "wb") as code:
    code.write(r.content)
    if __name__ == '__main__':
        pass
