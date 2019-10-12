import requests
from bs4 import BeautifulSoup
import os
import json
import time
import sys
import globalvar


# user_pages = sys.argv[2]
# user_query = sys.argv[1]
# print(len(sys.argv))

folder_path = f'/Users/seankolev/Downloads/unsplush/test/'
headers = {'User-Agent': 'Mozilla/5.0'}


def get_json(query):
    pages = 0
    pages = str(pages+1)
    perpage = '10'
    url = f'https://unsplash.com/napi/search/photos?query={query}&xp=&per_page={perpage}&page={pages}'
    api_respond = requests.get(url, headers=headers)
    respond_json = (json.loads(api_respond.text))
    return respond_json
    # img_url = respond_json[0]
    # print(img_url)


def make_path():
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)


def img_downloader(query):
    respond_json = get_json(query)
    results = respond_json['results']
    for i in range(len(results)):
        if globalvar.spyderstatu == True:
            try:
                image_name = folder_path + \
                    results[i]['alt_description'] + '.jpg'
            except TypeError:
                break
            image = requests.get(
                results[i]['urls']['raw'], headers=headers)
            with open(image_name, 'wb') as file:
                file.write(image.content)
                file.flush()
            file.close()
            globalvar.message = f'下载第{i+1}张图片'
            print(globalvar.message)
            time.sleep(0.5)
            #print('i='+str(i)+'\n', 'count='+str(counts)+'\n')
            set_globalstatu(i)
        else:
            print('下载终止')
            break


def set_globalstatu(i):
    if int(i+1) >= int(globalvar.user_count):
        globalvar.spyderstatu = False


def auto_download(counts, query):
    globalvar.spyderstatu = True
    globalvar.user_count = counts
    img_downloader(query)
    # print(str(globalvar.spyderstatu))
    if globalvar.spyderstatu == True:
        img_downloader(query)
    print('下载完成啦！')
