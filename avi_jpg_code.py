import sys
from cv2 import CAP_PROP_POS_FRAMES
import numpy as np
import cv2
from glob import glob

aa = 0
data_col = glob('*.avi')

for data in data_col:
    print(data)
    cap1 = cv2.VideoCapture(data)
    i = 0
    while True:
        co , img = cap1.read()
        
        if not co :
            break
        i +=1
        if i%900 ==0:
            cv2.imwrite('aa/{}_{}.jpg'.format(data[8:12],aa),img)
            aa += 1
        if cv2.waitKey(1) == 27:
            break
