# 爬取电影排行

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'Error'

def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    nowplaying_ul = soup.find('div', id='nowplaying').ul
    nowplaying_lis = nowplaying_ul.find_all('li', class_='list-item')
    print('*********************************正在上映********************************* \n')
    for movie in nowplaying_lis:
        name = movie['data-title']#电影名
        score = movie['data-score']#分数
        star = movie['data-star']#星
        duration = movie['data-duration']#时长
        region = movie['data-region']#国家
        director = movie['data-director']#导演
        actors = movie['data-actors']#主演
        print('电影名:{}  星:{}  分数:{}  国家:{}  导演:{}  主演:{}  时长:{} \n'.format(name, star, score, region, director, actors, duration))
    print('\n')
    upcoming_ul = soup.find('div', id='upcoming').ul
    upcoming_lis = upcoming_ul.find_all('li', class_='list-item')
    print('*********************************即将上映********************************* \n')
    for movie in upcoming_lis:
        name = movie['data-title']#电影名
        duration = movie['data-duration']#时长
        region = movie['data-region']#国家
        director = movie['data-director']#导演
        actors = movie['data-actors']#主演
        print('电影名:{}  国家:{}  导演:{}  主演:{}  时长:{} \n'.format(name, region, director, actors, duration))
    print('\n')


base_url = 'https://movie.douban.com/cinema/nowplaying/shanghai/'


if __name__ == '__main__':
    get_content(base_url)
    print('*********************************爬取结束*********************************')
    input('任意键退出!')

