import cv2
import numpy as np
 
img = cv2.imread('road.jpeg')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
img_bur = cv2.blur(gray,(4,4))
edges = cv2.Canny(img_bur,100,300)
lines = cv2.HoughLinesP(edges,2,np.pi/180,100,minLineLength=50,maxLineGap=10)
for line in lines:
    x1,y1,x2,y2 = line[0]
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('HoughP4.jpg',img)
cv2.namedWindow('img1',cv2.WINDOW_NORMAL)
cv2.imshow('img1',img)
cv2.namedWindow('img2',cv2.WINDOW_NORMAL)
cv2.imshow('img2',edges)
cv2.namedWindow('img3',cv2.WINDOW_NORMAL)
cv2.imshow('img3',img_bur)
cv2.waitKey(0) & 0xFF
cv2.destroyAllWindows()

