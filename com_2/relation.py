#coding: utf-8
'''
Created on 2016年8月9日

@author: ssy110
'''
import requests,re,util,globals,time,datetime
import threading
def getFromUid(url):
    cookies = open('user16').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=1)
    reg=r'h5icon.+?id":"(.+?)",.+?"attNum":"(.+?)",.+?"mblogNum":"(.+?)","fansNum":"(.+?)",.+?"name":"(.+?)",.+?"mbrank":"(.+?)",'
    if(html.status_code==200):
        dataList = re.findall(reg, html.text, re.S)
        return dataList
    else:
        return 'F'
def crawls():
    baseurl = 'http://m.weibo.cn/'
    datalist = util.selectFromComment(globals.conn)
    for data in datalist:
#         authorUrl = baseurl + 'u/' + data[1];
        authorUrl = baseurl + 'u/' + data[3];
        print '.................',authorUrl
        try:
            #抓取用户内容
            userList = getFromUid(authorUrl)
            if(userList=='F'):
                    raise Exception("break")
            else:
                if(userList):
                    for user in userList:#id,attnum,mblogNum,mbrank,name
                        try:
                            params = (user[0],user[1],user[2],user[3],user[4].decode('unicode-escape') ,user[5])
                            util.saveUser2(params,globals.conn)
                        except Exception,e:
                            print 'saveUser-failed!..','exception is: ',e
                    #util.changeRepoStateToYes(data[0],data[1], globals.conn)
                    util.changeCommStateToYes(data[0], globals.conn)
                else:
                    print '....................user not exist!..............................'
        except :
            print '........................data false!................................'
if __name__ == '__main__':
    crawls()
            
            