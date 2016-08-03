#coding: utf-8
'''
Created on 2016��7��21��

@author: ssy110

'''

import requests

def user_timeline(access_token):
    #url='https://api.weibo.com/2/users/show.json'
#     url='https://api.weibo.com/2/friendships/friends.json'
    url='https://api.weibo.com/2/friendships/followers.json'
    data={
           'access_token' :access_token,
           'screen_name':'听心跳的声音ssy'
          }
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'}
    html = requests.get(url,headers=headers,params=data ,timeout=1)
    html.encoding='utf-8'
    return html
if __name__ == '__main__':
    access_token='2.00kP71BGHwqboC771034272a03fKwv'
    print user_timeline(access_token).text