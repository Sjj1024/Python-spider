import requests
import os
from hashlib import md5
from urllib.parse import urlencode
from multiprocessing.pool import Pool
def get_data(offset):
    #构造URL，发送请求
    params = {
        'aid': '24',
        'app_name': 'web_search',
        'offset': offset,
        'format': 'json',
        'autoload': 'true',
        'count': '20',
        'en_qc': '1',
        'cur_tab': '1',
        'from': 'search_tab',
    }
    base_url = 'https://www.toutiao.com/api/search/content/?keyword=%E8%A1%97%E6%8B%8D'
    url = base_url + urlencode(params)
    try:
        res = requests.get(url)
        if res.status_code == 200:
            return res.json()
    except requests.ConnectionError:
        return 'sorry.'
def get_img(data):
    if data.get('data'):
        page_data = data.get('data')
        for item in page_data:
            title = item.get('title')
            imgs = item.get('image_list')
            for img in imgs:
                yield {
                    'title': title,
                    'img': img.get('url')
                }
def save(item):
    img_path = 'img' + '/' + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
    try:
        res = requests.get(item.get('img'))
        if res.status_code == 200:
            file_path = img_path + '/' + '{name}.{suffix}'.format(
                name=md5(res.content).hexdigest(),
                suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, 'wb') as f:
                    f.write(res.content)
                print('Successful')
            else:
                print('Already Download')
    except requests.ConnectionError:
        print('Failed to save images')
def main(offset):
    data = get_data(offset)
    for item in get_img(data):
        print(item)
        save(item)
START = 0
END = 10


if __name__ == "__main__":
    pool = Pool()
    offsets = ([n * 20 for n in range(START, END + 1)])
    pool.map(main,offsets)
    pool.close()
    pool.join()