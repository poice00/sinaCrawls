#-*- coding: UTF-8 -*- 。
""" 
Created on Fri Apr 08 17:10:36 2016 
 
@author: Administrator 
"""  
  
# coding=utf8  
import BeautifulSoup as bs  
import urllib  
import urllib2  
import cookielib  
import base64  
import re,requests
import json  
import hashlib  
import rsa  
import binascii
pubkey = 'EB2A38568661887FA180BDDB5CABD5F21C7BFD59C090CB2D245A87AC253062882729293E5506350508E7F9AA3BB77F4333231490F915F6D63C55FE2F08A49B353F444AD3993CACC02DB784ABBB8E42A9B1BBFFFB38BE18D78E87A0E41B9B8F73A928EE0CCEE1F6739884B9777E4FE9E88A1BBE495927AC4A799B3181D6442443'  
cj = cookielib.LWPCookieJar()  
cookie_support = urllib2.HTTPCookieProcessor(cj)  
opener = urllib2.build_opener(cookie_support, urllib2.HTTPHandler)  
urllib2.install_opener(opener)  
postdata = {  
    'entry': 'weibo',  
    'gateway': '1',  
    'from': '',  
    'savestate': '7',  
    'userticket': '1',  
    'ssosimplelogin': '1',  
    'vsnf': '1',  
    #'vsnval': '',  
    'su': '',  
    'service': 'miniblog',  
    'servertime': '',  
    'nonce': '',  
    #'pwencode': 'wsse',  
    'pwencode': 'rsa2',  
    'sp': '',  
    'pagerefer':'http://login.sina.com.cn/sso/logout.php?entry=miniblog&r=http%3A%2F%2Fweibo.com%2Flogout.php%3Fbackurl%3D%252F',  
    'raskv':'',  
    'sr':'1440*900',  
    'prelt':'94',  
    'encoding': 'UTF-8',  
    'url': 'http://weibo.com/ajaxlogin.php?framelogin=1&callback=parent.sinaSSOController.feedBackUrlCallBack',  
    'returntype': 'META'  
}  
  
def get_servertime():  
    url = 'http://login.sina.com.cn/sso/prelogin.php?entry=weibo&callback=sinaSSOController.preloginCallBack&su=dW5kZWZpbmVk&client=ssologin.js(v1.3.18)&_=1329806375939'  
    data = urllib2.urlopen(url).read()  
    p = re.compile('(.*)')  
    try:  
        json_data = p.search(data).group(1)  
        data = json.loads(json_data)  
        servertime = str(data['servertime'])  
        nonce = data['nonce']  
        rsakv=data['rsakv']  
        return servertime, nonce,rsakv  
    except:  
        print 'Get severtime error!'  
        return None  
  
def get_pwd(pwd, servertime, nonce):  
    global pubkey  
    rsaPublickey = int(pubkey, 16)  
    key = rsa.PublicKey(rsaPublickey, 65537) #创建公钥  
    message = str(servertime) + '\t' + str(nonce) + '\n' + str(pwd) #拼接明文js加密文件中得到  
    passwd = rsa.encrypt(message, key) #加密  
    passwd = binascii.b2a_hex(passwd) #将加密信息转换为16进制。  
    print passwd  
    return passwd  
  
  
def get_user(username):  
    username_ = urllib.quote(username)  
    username = base64.encodestring(username_)[:-1]  
    return username  
  
  
def login():  
    username = '18966901668'  
    pwd = '9446Yuss?'  
#     url = 'http://login.sina.com.cn/sso/login.php?client=ssologin.js(v1.4.18)'  
    url = 'https://login.sina.com.cn/'  
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    data={
          
        }
    html = requests.get(url,headers=headers,data ,timeout=1)
    html.encoding='utf-8'
if __name__=="__main__":  
    login()  