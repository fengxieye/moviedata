import json
import random
import time
import requests


# 爬取豆瓣所有电影的概要信息
def get_douban():
    headers = {}
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
    headers["Accept-Encoding"] = "gzip, deflate, sdch"
    headers["Accept-Language"] = "zh-CN,zh;q=0.8,en;q=0.6,zh-TW;q=0.4,ja;q=0.2"
    headers["Connection"] = "keep-alive"
    headers["Host"] = "m.douban.com"
    headers["Referer"] = "https://movie.douban.com/explore"
    headers["Upgrade-Insecure-Requests"] = "1"
    headers["User-Agent"] = "Mozilla/6.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36"

    start = 0
    while start < 40:
        url = "https://m.douban.com/rexxar/api/v2/movie/recommend?refresh=0&start=%d&count=20&selected_categories={}&uncollect=false&sort=T&tags=" % (
            start)
        ret = requests.get(url=url, headers=headers)
        movies = json.loads(ret.text)['items']
        rand = random.randint(0,100)/100
        time.sleep(rand)
        if len(movies) == 0:
            break
        for item in movies:
            count = item['rating']['count']
            star = item['rating']['star_count']
            value = item['rating']['value']
            title = item['title']
            card_subtitle = item['card_subtitle']
            countries = card_subtitle.split("/")[1].split(' ')
            country_str = ''
            for country in countries:
                if country != '':
                    if country_str != '':
                        country_str += ','
                    country_str += country.strip()
            tags = card_subtitle.split("/")[2].split(' ')
            tag_str = ''
            for tag in tags:
                if tag != '':
                    if tag_str != '':
                        tag_str += ','
                    tag_str += tag
            cover = item['pic']['large']
            movieid = item['id']
            year = item['year']
            record = str(movieid) + ';' + title + ';' + tag_str + ';' + country_str + ';' + cover + ';' + str(year) + ';' + str(value) + ';' + str(count) + ';' + str(star) + '\n'
            # fw.write(record.encode('utf8'))
            print(record)
        start = start + 20


if __name__ == '__main__':
    get_douban()