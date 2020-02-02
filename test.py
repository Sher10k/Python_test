import sys 

import numpy as np 
import cv2 as cv
import open3d as o3d

#print(sys.prefix)

cap = cv.VideoCapture(0)

while( True ):
    ret, frame = cap.read()
    cv.imshow( 'frame', frame )
    if cv.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()

img = cv.imread('/home/roman/python_test/RGBD1.jpg',0)

cv.imshow( 'image', img )
cv.waitKey(0)
cv.imshow( 'image', img )
cv.destroyAllWindows()

