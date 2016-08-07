#coding: utf-8
'''
Created on 2016年8月5日

@author: ssy110
'''
from com_2.util import readBlogData
from com_2 import globals
import requests,re,json
def getDatas(url,page,type):
    print page,type
    cookies = open('ssy').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies,
    }
    data = {
              'format':'cards',
              'hot':'0',
              'type':type,
              'page':page
          }
    html = requests.get(url,headers=headers,params=data,timeout=5)
    print html.text
    data = html.json()['data']
    for d in data:
        print '.............'
        print d['text']
        print d['user']['id']
        print d['user']['screen_name']
#     reg=r''
#     dataList = re.findall(reg, html.text, re.S)
#     return dataList

if __name__ == '__main__':
    dataList = readBlogData(globals.conn)
    print 'start..'
    for data in dataList:
        print data[0],data[6],data[3],data[5]#mid uid commentConut repostCount
        baseUrl = 'http://m.weibo.cn/article/rcMod?id=%s'%data[0]
        commpage=0
        repopage=0
        if(int(data[3])!=0):
            commpage = int(data[3])/20+1
        if(int(data[5])!=0):
            repopage = int(data[5])/20+1
        if(repopage==0 and commpage==0):
            print '没有回复和转发。。。'
            continue
        #处理转发
        for page in range(1,repopage+1):
            getDatas(baseUrl,page,'repost')
            break
        #处理评论
#         for page in range(1,commpage+1):
#             getDatas(baseUrl,page,'comment')
#             break
        print commpage,repopage
        break;
    #http://m.weibo.cn/article/rcMod?id=4004080337260586&type=repost&hot=0&page=1 
    #http://m.weibo.cn/article/rcMod?id=3984875877141067&type=comment
    
    #/single/rcList?format=cards&id=3970627763485513&type=comment&hot=0&page=2
    #http://m.weibo.cn/1734959391/3971024683266746/rcMod?format=cards&type=comment&hot=0&page=1 
    
    #http://m.weibo.cn/5544721911/3984875877141067 #帖子地址