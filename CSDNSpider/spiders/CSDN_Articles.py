#-*- coding = utf-8 -*-
#@Time : 2021/4/18 20:55
#@Author : linovce

import hashlib
import hmac
from base64 import b64encode
import random
import requests
import http.cookiejar as cookielib
from urllib.parse import urlparse

def createUuid():
    text = ""
    char_list = []
    for c in range(97,97+6):
        char_list.append(chr(c))
    for c in range(49,58):
        char_list.append(chr(c))
    for i in "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx":
        if i == "4":
            text += "4"
        elif i == "-":
            text += "-"
        else:
            text += random.choice(char_list)
    return text

def get_sign(uuid,url):
    s = urlparse(url)
    ekey = "9znpamsyl2c7cdrr9sas0le9vbc3r6ba".encode()
    to_enc = f"GET\n*/*\n\n\n\nx-ca-key:203803574\nx-ca-nonce:{uuid}\n{s.path+'?'+s.query[:-1]}".encode()
    sign = b64encode(hmac.new(ekey, to_enc, digestmod=hashlib.sha256).digest()).decode()
    return sign

def getArticleDetail(url):
    uuid = createUuid()
    sign = get_sign(uuid,url)
    headers = {}
    headers['x-ca-key'] = "203803574"
    headers['x-ca-nonce'] = uuid
    headers['x-ca-signature'] = sign
    headers['x-ca-signature-headers'] = "x-ca-key,x-ca-nonce"
    session = requests.session()

    session.cookies = cookielib.LWPCookieJar(filename='cookie/csdn.txt')
    session.cookies.load()
    data = session.get(url,headers=headers).json()
    return data


def get_all(url):
    f = open("blogIdList.txt")  # 返回一个文件对象
    article_list = []
    line = f.readline()  # 调用文件的 readline()方法
    while line:
        article_list.append(line.strip())
        print(line, end = '')     # 在 Python 3 中使用
        line = f.readline()
    f.close()
    return article_list

if __name__ == '__main__':
    url = "https://blog.csdn.net/xxx"  # 更改为你自己的csdn博客主页地址
    article_list = get_all(url)

    for article in article_list:
        url = "https://bizapi.csdn.net/blog-console-api/v3/editor/getArticle?id=%s&model_type="%article
        text = getArticleDetail(url)
        markdown = text['data']['markdowncontent']
        title = text['data']['title']
        try:
            if markdown:
                for i in ["?", "、", "\\", "/", "*", '"', ":", "<", ">", "|"]:
                    title = title.replace(i, "-")
                print("文章\\%s.md" % title)
                with open("文章\\%s.md" % title, 'a',encoding='utf8') as f:
                    print(markdown)
                    f.write(markdown)
        except Exception as e:
            print("error", e)
