import requests  # pip3 install requests
import re
import hashlib
import time

movie_path = 'd:\\mp4'
with open("d:\\mp4\\d77b4e633e12b9a71863e157dda58340.txt", "wb", encoding='UTF-8') as f:
    print('%s 下载成功')


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass


def parse_index(index_page):
    urls = re.findall('class="items".*?href="(.*?)"', index_page, re.S)
    for url in urls:
        if not url.startswith('http'):
            url = 'http://www.xiaohuar.com' + url
        yield url


def parse_detail(detail_page):
    l = re.findall('id="media".*?src="(.*?)"', detail_page, re.S)
    if l:
        movie_url = l[0]
        if movie_url.endswith('mp4'):
            yield movie_url


def get_movie(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            m.update(url.encode('utf-8'))
            filepath = '%s\\%s.mp4' % (movie_path, m.hexdigest())
            with open(filepath, 'wb') as f:
                f.write(response.content)
                print('%s 下载成功' % url)
    except Exception:
        pass


def main():
    base_url = 'http://www.xiaohuar.com/list-3-{page_num}.html'
    for i in range(2):
        url = base_url.format(page_num=i)
        index_page = get_page(url)
        detail_urls = parse_index(index_page)
        print(i)
        for detail_url in detail_urls:
            detail_page = get_page(detail_url)
            movie_urls = parse_detail(detail_page)
            for movie_url in movie_urls:
                get_movie(movie_url)


if __name__ == '__main__':
    main()
