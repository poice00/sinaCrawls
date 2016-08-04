#coding: utf-8
'''
Created on 2016年8月3日

@author: ssy110
'''
import util,globals
if __name__ == '__main__':
    print '\u897f\u5b89\u8eab\u8fb9\u4e8b'.decode('unicode-escape')
    rows = util.selectFromOrigindata(globals.conn)
    for row in rows:
        print row[0],row[1],row[2],row[3]
#     row = util.getByMid('E1zIW2nhQ', globals.conn)
#     print row[0],row[1],row[2],row[3]