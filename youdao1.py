#/usr/bin/env python
#coding=utf8
 
import httplib
import md5
import urllib
import urllib2
import random
import json
import base64

appKey = '6c879f8e026eb131'
secretKey = 'cDtx76PNuKzSGzHn4p6bGfodWNbq62no'
httpClient = None

class OCR():
    def __init__(self):
        pass
    def __del__(self):
        pass
    def startWithFile(self,path = 'testpng.png'):
        try:
            f=open(path,'rb')
            img=base64.b64encode(f.read()) #读取文件内容，转换为base64编码
            f.close()
    
            detectType = '10011'
            imageType = '1'
            langType = 'zh-en'
            salt = random.randint(1, 65536)
    
            sign = appKey+img+str(salt)+secretKey
            m1 = md5.new()
            m1.update(sign)
            sign = m1.hexdigest()
            data = {'appKey':appKey,'img':img,'detectType':detectType,'imageType':imageType,'langType':langType,'salt':str(salt),'sign':sign}
            data = urllib.urlencode(data)
            req = urllib2.Request('http://openapi.youdao.com/ocrapi',data)
    
            #response是HTTPResponse对象
            response = urllib2.urlopen(req)
            res = response.read()
            r = json.loads(res)
            k = r['Result']['regions']
            #           print k[0]['lines']
            text = ''
            for i in k:
                item = i
                lines = item['lines']
                #                print "============"
                #      print lines
                for j in lines:
                    words = j['words']
                    #                    print "***********"
                    for t in words:
                        #                        print t['text']
                        text = text + t['text']
                    text = text + '\r\n'
            return text
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

    def startWithData(self,data):
        try:
#            f=open(path,'rb')
            img=base64.b64encode(data) #读取文件内容，转换为base64编码
#            f.close()

            detectType = '10011'
            imageType = '1'
            langType = 'zh-en'
            salt = random.randint(1, 65536)
            
            sign = appKey+img+str(salt)+secretKey
            m1 = md5.new()
            m1.update(sign)
            sign = m1.hexdigest()
            data = {'appKey':appKey,'img':img,'detectType':detectType,'imageType':imageType,'langType':langType,'salt':str(salt),'sign':sign}
            data = urllib.urlencode(data)
            req = urllib2.Request('http://openapi.youdao.com/ocrapi',data)
            
            #response是HTTPResponse对象
            response = urllib2.urlopen(req)
            res = response.read()
            print "=========>"
            print res
            r = json.loads(res)
            k = r['Result']['regions']
            #           print k[0]['lines']
            text = ''
            for i in k:
                item = i
                lines = item['lines']
                #                print "============"
                #      print lines
                for j in lines:
                    words = j['words']
                    #                    print "***********"
                    for t in words:
                        #                        print t['text']
                        text = text + t['text']
                    text = text + '\r\n'
            return text
        except Exception, e:
            print e
        finally:
            if httpClient:
                httpClient.close()

if __name__ == "__main__":
    path = 'opencvPic.jpeg'
    f=open(path,'rb')
    ocr = OCR()
    
    text = ocr.startWithFile('opencvPic.jpeg')
    f.close()
    print text


