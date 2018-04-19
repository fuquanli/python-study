# 爬取电影排行

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'gbk'
        return r.text
    except:
        return 'Error'

def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    movies_list = soup.find('ul', class_='picList clearfix')
    movies = movies_list.find_all('li')
    for movie in movies:
        name = movie.find('a', class_='aPlayBtn')['title']
        try:
            time = movie.find('span', class_='sIntro').text
        except:
            time = '暂无上映时间'
        actors = movie.find('p', class_='pActor')
        actor = ''
        for act in actors:
            actor = actor + act.string + ' '
        intor = movie.find('p', class_='pTxt pIntroShow').text
        img_url = movie.find('img')['src']
        print('片名：{}\t{}\n{}\n{} \n \n '.format(name,time,actor,intor))
        with open('D:/fuquan/从零开始写python/Beautiful Soup 爬虫/电影图片/'+ name +'.png', 'wb+') as f:
            f.write(requests.get('http:'+img_url).content)


base_url = 'http://dianying.2345.com/top/'

if __name__ == '__main__':
    get_content(base_url)

