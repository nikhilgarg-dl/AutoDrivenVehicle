import numpy as np
import cv2

cap = cv2.VideoCapture('road.avi')

w = cap.get(cv2.CAP_PROP_FRAME_WIDTH);
h = cap.get(cv2.CAP_PROP_FRAME_HEIGHT); 

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(w),int(h)))
 
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        img_bur = cv2.blur(gray,(4,4))
        edges = cv2.Canny(img_bur,100,300)
        lines = cv2.HoughLinesP(edges,2,np.pi/180,100,minLineLength=50,maxLineGap=10)
        if lines == None: 
            continue
        for line in lines:
            x1,y1,x2,y2 = line[0]
            cv2.line(frame,(x1,y1),(x2,y2),(0,0,255),2)
        cv2.imshow('frame',frame)
        out.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
 
cap.release()
out.release()
cv2.destroyAllWindows()
