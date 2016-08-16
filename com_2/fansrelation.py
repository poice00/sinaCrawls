#coding: utf-8
'''
Created on 2016年8月5日

@author: ssy110
'''
from com_2.util import readBlogData
from com_2 import globals
import requests,re,json,util,uuid
def getDatas(url,page,id):
    cookies = open('user1').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    data = {
                'containerid':'100505'+id+'_-_FANS',
                'page':page
          }
    html = requests.get(url,headers=headers,params=data,timeout=5)
    if(html.status_code==200):
        dataset=set()
        try:
            datas = html.json()['cards']
        except Exception,e:
            return dataset
        for d in datas:
            for d1 in d['card_group']:
                dataset.add(d1['user']['id'])
        return dataset
    else:
        return 'F'

if __name__ == '__main__':
    userIdData = util.readUserData(globals.conn)
    print 'start..'
    #处理每一个用户
    for data in userIdData:
        baseUrl = 'http://m.weibo.cn/page/json'
        print data[0]#id
        #计算页数
        page = 20
        try:
            for page in range(1,page+1):
                print '..The current page is: ',page
                userIdList = getDatas(baseUrl,page,data[0])
                if(userIdList=='F'):
                    #如果返回值不是200
                    raise Exception("break")
                else:
                    #将评论存入数据库
                    if(userIdList):
                        for userId in userIdList:
                            #遍历用户的粉丝
                            if(userId in userIdData):
                                print '=====================================its in user!'
                                try:
                                    params = (userId,data[0])
                                    util.saveToUserRelation(params,globals.conn)
                                except Exception,e:
                                    print 'saveToUserRelation false!','exception is: ',e
                            else: 
                                print 'not in user!'
                    else:
                        break
            util.changeUserStateTohandle(data[0],globals.conn)
        except :
            print '.....data false!...........................................'
    print 'end..'
    #http://m.weibo.cn/article/rcMod?id=4004080337260586&type=repost&hot=0&page=1 
    #http://m.weibo.cn/article/rcMod?id=3984875877141067&type=comment
    
    #/single/rcList?format=cards&id=3970627763485513&type=comment&hot=0&page=2
    #http://m.weibo.cn/1734959391/3971024683266746/rcMod?format=cards&type=comment&hot=0&page=1 
    
    #http://m.weibo.cn/5544721911/3984875877141067 #帖子地址