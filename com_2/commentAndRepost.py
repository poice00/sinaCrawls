#coding: utf-8
'''
Created on 2016年8月5日

@author: ssy110
'''
from com_2.util import readBlogData
from com_2 import globals
import requests,re,json,util,uuid
def getDatas(url,page,type):
    cookies = open('user13').readline()#
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
    if(html.status_code==200):
        dataList=[]
        try:
            data = html.json()['data']
        except Exception,e:
            return dataList
        for d in data:
            tmpList=[d['user']['id'],d['text']]
            dataList.append(tmpList)
        return dataList
    else:
        return 'F'

if __name__ == '__main__':
    dataList = readBlogData(globals.conn)
    print 'start..'
    for data in dataList:
        print 'mid:',data[0]
        print 'uid',data[6]
        print 'commentConut',data[3]
#         print 'repostCount',data[5]#mid uid commentConut repostCount
        baseUrl = 'http://m.weibo.cn/article/rcMod?id=%s'%data[0]
#         commpage=0
#         repopage=0
#         if(int(data[3])!=0):
#             commpage = int(data[3])/20+1
#         if(int(data[5])!=0):
        #if(repopage==0 and commpage==0):
#         if(repopage==0):
#             print '没有回复和转发。。。'
#             util.changeBlogStateTohandle(data[0],globals.conn)
#             continue
#   转发开始
#         repopage = int(data[5])/20+1
#         print '。。。。。转发。。。。。'
#         try:
#             #处理转发
#             for page in range(1,repopage+1):
#                 print '..The current page is: ',page
#                 repodataList = getDatas(baseUrl,page,'repost')
#                 if(repodataList=='F'):
#                     raise Exception("break")
#                 else:
#                     #将转发存入数据库
#                     for repodata in repodataList:
    #                     try:
#                             params = (data[0],repodata[0],repodata[1])
#                             util.saveToRepoRelation(params,globals.conn)
    #                     except Exception,e:
#                             print 'saveToRepoRelation false!','exception is: ',e
#             util.changeBlogStateTohandle(data[0],globals.conn)
#         except:
#             print '..............................data false!...........................................'
#   转发结束
        commpage = int(data[3])/20+1
        print '。。。。。评论。。。。。'
        try:
            #处理评论
            print '评论。。。'
            for page in range(1,commpage+1):
                print '..The current page is: ',page
                commdataList = getDatas(baseUrl,page,'comment')
                if(commdataList=='F'):
                    raise Exception("break")
                else:
                    #将评论存入数据库
                    for commdata in commdataList:
                        try:
                            params = (str(uuid.uuid1()),data[0],commdata[0],commdata[1])
                            util.saveToCommRelation(params,globals.conn)
                        except Exception,e:
                            print 'saveToCommRelation false!','exception is: ',e
            util.changeBlogStateTohandle(data[0],globals.conn)
        except :
            print '..............................data false!...........................................'
    print 'end..'
    #http://m.weibo.cn/article/rcMod?id=4004080337260586&type=repost&hot=0&page=1 
    #http://m.weibo.cn/article/rcMod?id=3984875877141067&type=comment
    
    #/single/rcList?format=cards&id=3970627763485513&type=comment&hot=0&page=2
    #http://m.weibo.cn/1734959391/3971024683266746/rcMod?format=cards&type=comment&hot=0&page=1 
    
    #http://m.weibo.cn/5544721911/3984875877141067 #帖子地址