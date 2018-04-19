# 爬取音乐榜单

import requests
from bs4 import BeautifulSoup

def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'UTF-8'
        return r.text
    except:
        return 'Error'

def get_content(url):
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    dmv_list = soup.find_all('li', class_='vitem J_li_toggle_date ')
    for dmv in dmv_list:
        point = dmv.find('h3').text
        top_num = dmv.find('div', class_='top_num').text
        name = dmv.find('a', class_='mvname').text
        singer = dmv.find('a', class_='special').text
        time = dmv.find('p', class_='c9').text
        print('排名:{}  分数:{}  歌曲名:{}  歌手:{}  {} \n'.format(top_num, point, name, singer, time))

base_url = 'http://vchart.yinyuetai.com/vchart/trends?area='

if __name__ == '__main__':
    area = ('ML', 'HT', 'US', 'JP', 'KR')
    dic = {'内地':'ML', '港台':'HT', '欧美':'US', '日本':'JP', '韩国':'KR'}
    for k in dic:
        print(k+'排行榜 \n')
        get_content(base_url+dic[k])