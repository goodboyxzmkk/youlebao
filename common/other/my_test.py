import requests  # pip3 install requests
import re
import hashlib
import time
from concurrent.futures import ThreadPoolExecutor

pool = ThreadPoolExecutor(50)
movie_path = r'd:\mp4'


def get_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except Exception:
        pass


def parse_index(index_page):
    index_page = index_page.result()
    urls = re.findall('class="items".*?href="(.*?)"', index_page, re.S)
    for detail_url in urls:
        if not detail_url.startswith('http'):
            detail_url = 'http://www.xiaohuar.com' + detail_url
        pool.submit(get_page, detail_url).add_done_callback(parse_detail)


def parse_detail(detail_page):
    detail_page = detail_page.result()
    l = re.findall('id="media".*?src="(.*?)"', detail_page, re.S)
    if l:
        movie_url = l[0]
        if movie_url.endswith('mp4'):
            pool.submit(get_movie, movie_url)


def get_movie(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            m = hashlib.md5()
            m.update(str(time.time()).encode('utf-8'))
            m.update(url.encode('utf-8'))
            filepath = '%s\%s.mp4' % (movie_path, m.hexdigest())
            with open(filepath, 'wb') as f:
                f.write(response.content)
                print('%s 下载成功' % url)
    except Exception:
        pass


def main():
    base_url = 'http://www.xiaohuar.com/list-3-{page_num}.html'
    for i in range(5):
        url = base_url.format(page_num=i)
        pool.submit(get_page, url).add_done_callback(parse_index)


if __name__ == '__main__':
    main()
