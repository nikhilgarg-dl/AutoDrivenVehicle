
import cv2
import numpy as np
import time
from cv2 import CV_8U, line
x=y=20
cap = cv2.VideoCapture('test.mp4')
def writeMouse(evt, m_x, m_y, a, b):
    global x,y
    x = m_x
    y = m_y

cv2.namedWindow('Output')
cv2.setMouseCallback('Output', writeMouse)
while(cap.isOpened()):
    ret, img = cap.read()
    h,w,_ = img.shape
    mask = img*0 #create a black image having same dimensions as the current frame
    
    #represents the probable zone in which the lane may be found in an image captured by a camera mounted on the front of the vehicle
    pts = np.float32([[.45*w, .65*h], [.6*w, .65*h], [1*w,1*h],[.0*w,1*h]]) 
    cv2.fillPoly(mask, np.int32([pts]), 255) #create a white trapezoid
    mask = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
    roi = cv2.bitwise_and(img, img, mask=mask) #extract the roi from our captured image
    grayed = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    grayed = cv2.GaussianBlur(grayed,(9,9),0)
    avg = 0.0
    # find the average color in our roi
    for i in range(int(h*.65), h):
        if(grayed[i][int(w*.5)]>0):
            avg = (avg+grayed[i][int(w*.5)])*.5
    _, binary_roi = cv2.threshold(grayed, avg+35, 255, cv2.THRESH_BINARY) 
    im, contours, hierarchy = cv2.findContours(binary_roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(img, contours, -1, (0, 255, 255), 2)
    cv2.putText(img, str(x)+", "+str(y), (x,y),cv2.FONT_HERSHEY_PLAIN,1,(0,0,0,.5))
    cv2.imshow('Output', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27: break

cv2.destroyAllWindows()
cap.release()
