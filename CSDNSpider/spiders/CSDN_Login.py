#-*- coding = utf-8 -*-
#@Time : 2021/4/18 20:55
#@Author : linovce

import re
from threading import Thread
import time
import requests
from io import BytesIO
import http.cookiejar as cookielib
from PIL import Image

requests.packages.urllib3.disable_warnings()

class show_code(Thread):
    def __init__(self,url):
        Thread.__init__(self)
        self.url = url

    def run(self):
        response = requests.get(self.url)
        img = Image.open(BytesIO(response.content))  # 打开图片，返回PIL image对象
        img.show()

def login():
    session = requests.session()
    session.cookies = cookielib.LWPCookieJar(filename='cookie/csdn.txt')##将cookie保存至文件
    ##获取微信登录的二维码的url
    response = session.get('https://open.weixin.qq.com/connect/qrconnect?appid=wx0ae11b6a28b4b9fc&scope=snsapi_login&redirect_uri=https%3A%2F%2Fpassport.csdn.net%2Fv1%2Fregister%2FpcAuthCallBack%3FpcAuthType%3Dweixin&state=csdn&login_type=jssdk&self_redirect=default&style=white&href=https://csdnimg.cn/release/passport/history/css/replace-wx-style.css',verify=False)
    uuid = re.findall('<img class="qrcode lightBorder" src="(.*?)" />',response.text)[0]
    img_url = 'https://open.weixin.qq.com' + uuid
    t= show_code(img_url)
    t.start()
    uuid = uuid.split('/')[-1]
    url = 'https://long.open.weixin.qq.com/connect/l/qrconnect?uuid='+uuid
    while 1:
        print(url)
        response = session.get(url,verify=False)
        code = re.findall("window.wx_code='(.*?)'",response.text)
        print(code)
        if code != ['']:
            break
        time.sleep(1)

    url = 'https://passport.csdn.net/v1/register/pcAuthCallBack?pcAuthType=weixin&code=%s&state=csdn' % code[0]
    print(url)
    session.get(url)
    session.cookies.save()
    print('登录成功！')

if __name__ == '__main__':
    login()