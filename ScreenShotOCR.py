#/usr/bin/env python
#coding=utf8

import time
from youdao1 import OCR
import sys,os
import FindResult
import cv2
reload(sys)
sys.setdefaultencoding('utf8')


while 0:
#        time.sleep(0.1)
        os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
        os.system("adb pull /sdcard/screenshot.png screenshot.png")
        image = cv2.imread("screenshot.png")           # 从指定路径读取图像
        cropImg = image[400:1150,0:700] #获取感兴趣区域
        cv2.imwrite("screenshot.png",cropImg)
        ocr = OCR()
        text = ocr.startWithFile('screenshot.png')

        print text
        if text:
            if len(text) > 3:
                FindResult.FindShowBaidu(text)
                time.sleep(0.2)

while 1:

    os.system("adb shell /system/bin/screencap -p /sdcard/screenshot.png")
    os.system("adb pull /sdcard/screenshot.png screenshot.png")
    image = cv2.imread("screenshot.png")           # 从指定路径读取图像

    cropImg = image[73:855,30:690] #获取感兴趣区域
#    cropImg = image[90:1170,40:1040] #获取感兴趣区域
    cv2.imwrite("screenshot.png",cropImg)
    ocr = OCR()
    text = ocr.startWithFile('screenshot.png')

    print text
    
    if text:
        if len(text) > 3:
                FindResult.FindShowBaiduFromXiGua(text)
                time.sleep(0.2)


