# -*- coding:UTF-8 -*-

from urllib import request
import requests
from bs4 import BeautifulSoup
import re

if __name__ == "__main__":
    download_url = "http://nurienomori.com/nurie.html"
    head = {}
    head['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    download_req = request.Request(url = download_url, headers = head)
    download_response = request.urlopen(download_req)
    download_html = download_response
    print(download_html)
    soup_texts = BeautifulSoup(download_html, 'lxml')
    print(type(soup_texts))

    for tag in soup_texts.find_all(href=re.compile("images/nurie/[a-z]+[0-9]+.pdf")):
        res = "http://nurienomori.com/" + tag["href"]
        name = re.search("[a-z]+[0-9]+.pdf", res, flags=0)
       
        path = './other/' + str(name.group())
        print(path)
        r = requests.get(res, stream=True)
        if r.status_code == 200:
            with open(path,'wb') as f:
                for chunk in r.iter_content(chunk_size=1024):
                    f.write(chunk)
                

