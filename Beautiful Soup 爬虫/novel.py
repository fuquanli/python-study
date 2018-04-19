#爬取小说
import requests
from bs4 import BeautifulSoup

#获取网页
def get_html(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = 'utf-8'
        return r.text
    except:
        return 'ERROR'

def get_content(url):
    #爬取每一种类型小说排行榜，按顺序写入文件，文件内容为 小说名字+小说链接，将内容保存到列表，并且返回一个装满url的列表
    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    category_list = soup.find_all('div', class_='index_toplist mright mbottom')
    history_finished_list = soup.find_all('div', class_='index_toplist mbottom')
    for cate in category_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a+', encoding='utf-8') as f:
            f.write('\n小说种类：{} \n'.format(name))
        #通过style属性来定位总排行版
        general_list = cate.find(style='display: block;')
        if general_list != None:
            book_list = general_list.find_all('li')
        for book in book_list:
            link = 'http://www.qu.la/'+book.a['href']
            title = book.a['title']
            url_list.append(link)
            with open('novel_list.csv', 'a', encoding='utf-8') as f:
                f.write('小说名：{} 小说地址：{} \n'.format(title, link))
    for cate in history_finished_list:
        name = cate.find('div', class_='toptab').span.string
        with open('novel_list.csv', 'a', encoding='utf-8') as f:
            f.write('\n小说种类：{} \n'.format(name))
        general_list = cate.find(style='display:block')
        if general_list != None:
            book_list = general_list.find_all('li')
        for book in book_list:
            link = 'http://www.qu.la/'+book.a['href']
            title = book.a['title']
            url_list.append(link)
            with open('novel_list.csv', 'a', encoding='utf-8') as f:
                f.write('小说名：{} 小说地址：{}\n'.format(title, link))
    return url_list

#获取单本小说所以章节链接
def get_txt_url(url):
    url_list = []
    html = get_html(url)
    soup = BeautifulSoup(html, 'lxml')
    lista = soup.find_all('dd')
    txt_name = soup.find('h1').text
    with open('/Users/Lifuquan.ET/Desktop/temp/从零开始写python/Beautiful Soup 爬虫/小说/{}.txt'.format(txt_name), 'a+', encoding='utf-8') as f:
        f.write('小说标题：{} \n'.format(txt_name))
    for u in lista:
        url_list.append(url+u.a['href'])
    return url_list, txt_name

#获取单页文章内容到本地
def get_one_txt(url, txt_name):
    html = get_html(url).replace('<br/>', '\n')
    soup = BeautifulSoup(html, 'lxml')
    try:
        txt = soup.find('div', id='content').text.replace('chaptererror();', '')
        title = soup.find('title').text
        with open('/Users/Lifuquan.ET/Desktop/temp/从零开始写python/Beautiful Soup 爬虫/小说/{}.txt'.format(txt_name), 'a+', encoding='utf-8') as f:
            f.write(title + '\n')
            f.write(txt)
            print('当前小说：{} 当前章节{} 已经下载完毕'.format(txt_name, title))
    except:
        print('someting wrong')

base_url = 'https://www.qu.la/paihangbang/'

if __name__ == '__main__':
    novel_url_list = get_content(base_url)
    for novel in novel_url_list:
        urls, name = get_txt_url(novel)
        for url in urls:
            get_one_txt(url, name)
