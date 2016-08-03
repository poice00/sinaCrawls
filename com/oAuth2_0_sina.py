#coding: utf-8
'''

@author: ssy110
'''
import requests
def confirm(access_token):
    url='https://api.weibo.com/oauth2/get_token_info';
    data={
          'access_token' :access_token
        }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    html = requests.post(url,data,headers)
    html.encoding='utf-8'
    return html
def getRes(appkey,client_secret,redirect_uri,code):
    url='https://api.weibo.com/oauth2/access_token'
    data={
          'client_id' :appkey,
          'client_secret':client_secret,
          'grant_type':'authorization_code',
          'redirect_uri': redirect_uri,
          'code':code
          }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    html = requests.post(url,data,headers)
    html.encoding='utf-8'
    return html
if __name__ == '__main__':
#     code=''
#     res = getRes(2580104091,'4ce20339961cd783372142281d7215aa','https://api.weibo.com/oauth2/default.html',code)
#     print res.text
    #2.00kP71BGHwqboC771034272a03fKwv
    print confirm('2.00kP71BGHwqboC771034272a03fKwv').text









