#/usr/bin/env python
#coding=utf8

import cv2,time
from youdao1 import OCR
import sys
import FindResult
reload(sys)
sys.setdefaultencoding('utf8')


cap = cv2.VideoCapture(0)

cap.set(3,1920)
cap.set(4,1080)
cap.set(1, 10.0)

while cap.isOpened():
    isSuccess,frame = cap.read()
    if isSuccess:
        cv2.namedWindow('myCapture',0)
        cv2.startWindowThread() #加在这个位置
        cv2.imshow("myCapture",frame)
        cv2.imwrite("opencvPic.jpeg", frame)
        time.sleep(0.1)
        ocr = OCR()
        text = ocr.startWithFile('opencvPic.jpeg')
        print text
        if text:
            if len(text) > 3:
                FindResult.FindShowBaidu(text)
                time.sleep(0.2)
        
    if cv2.waitKey(1)&0xff == ord('q'):
        cv2.imwrite("opencvPic.jpeg", frame)


cap.release()
cv2.destroyAllWindows()


