#coding: utf-8
'''
Created on 2016年8月2日

@author: ssy110
'''
import requests,re,util,globals,time,datetime
def getFromMid1(url):
    cookies = open('user1').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=3)
    reg=r'"text".+?/a> (.+?)",.+?h5icon.+?reposts_count":(.+?),"comments_count":(.+?),"attitudes_count":(.+?),.+?"created_timestamp":(.+?),.+?mid":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
    for data in dataList:
        print 'weibo-text:',data[0].decode('unicode-escape')
        print 'reposts_count: ',data[1]
        print 'comments_count: ',data[2]
        print 'attitudes_count: ',data[3]
        print 'created_timestamp: ',util.timestamp2string(float(data[4]))
        print 'mid: ',data[5]  
        print 'uid: ',url.split("/")[-2]  
        print 'bid: ',url.split("/")[-1] 
    return dataList
#         #writer(data,'D:/eclipse_workspace/Crawls/com_2/data')
#         try:
#             dateString = util.timestamp2string(float(data[1]))
#             postTime = datetime.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
#             params = (data[2],postTime,data[0])
#             util.saveOrigindata(params,globals.conn)
#         except Exception,e:
#             print 'saveOrigindata-failed!..','exception is: ',e
def getFromMid2(url):
    cookies = open('user1').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    html = requests.get(url,headers=headers,timeout=3)
    reg=r'<span class="time">(.+?)</span>.+?class="weibo-text".+?/a> (.+?)</div>.+?<span node-type="zfCount">(.+?)</span>.+?<span node-type="cmtCount">(.+?)</span>.+?<i node-type="zanCount">(.+?)</i>.+?"mid":"(.+?)"}'
    dataList = re.findall(reg, html.text, re.S)
    for data in dataList:
        print '.....................'
        print 'created_timestamp: ',data[0]
        print 'weibo-text: ',data[1]
        print 'reposts_count: ',data[2]
        print 'comments_count: ',data[3]
        print 'attitudes_count: ',data[4]  
        print 'mid: ',data[5]  
        print 'uid: ',url.split("/")[-2]  
        print 'bid: ',url.split("/")[-1]  
    return dataList
#         #writer(data,'D:/eclipse_workspace/Crawls/com_2/data')
#         try:
#             dateString = util.timestamp2string(float(data[1]))
#             postTime = datetime.datetime.strptime(dateString,'%Y-%m-%d %H:%M:%S')
#             params = (data[2],postTime,data[0])
#             util.saveOrigindata(params,globals.conn)
#         except Exception,e:
#             print 'saveOrigindata-failed!..','exception is: ',e
def getFromUid(url):
    cookies = open('user1').readline()#
    headers = {
               'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0',
               'cookie': cookies
    }
    data={
          'containerid' :'2305301008080f2b0e1930f5b30eae8d2b95f3c58232__timeline__mobile_guide_-_pageapp:23055763d3d983819d66869c27ae8da86cb176',
          'uid' :'5621836332'#user1
    }
    html = requests.get(url,headers=headers,timeout=3)
    reg=r'h5icon.+?id":"(.+?)",.+?"attNum":"(.+?)",.+?"mblogNum":"(.+?)","fansNum":"(.+?)",.+?"name":"(.+?)",.+?"mbrank":"(.+?)",'
    dataList = re.findall(reg, html.text, re.S)
    for data in dataList:
        print '.....................'
        print 'id: ',data[0]
        print 'attNum: ',data[1]
        print 'mblogNum: ',data[2]
        print 'fansNum: ',data[3]    
        print 'name: ',data[4].decode('unicode-escape') 
        print 'mbrank: ',data[5]  
if __name__ == '__main__':
    baseurl = 'http://m.weibo.cn/'
    dataList=open('zsina','r').readlines()
    i = 0 ;
    for data in dataList:
        print '.................'
        if i==5:
            break;
        authorUrl = baseurl + 'u/' + data.rstrip().split('\t')[2];
        blogUrl = baseurl + data.rstrip().split('\t')[2] + '/' + data.rstrip().split('\t')[0]
        print data.rstrip(),authorUrl,blogUrl
        getFromUid(authorUrl)
        if(getFromMid1(blogUrl)):
            print '.'
        elif(getFromMid2(blogUrl)):
            print '..'
        else:
            print 'not exist！'
#         break;
        i+=1
    