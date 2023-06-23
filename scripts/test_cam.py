#! /usr/bin/env python

import numpy as np
import cv2

cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)1280, height=(int)720, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !  appsink", cv2.CAP_GSTREAMER)

def open_cam():
    if cap.isOpened():
	while(True):
            ret, img = cap.read()
    	    cv2.imshow('camera', img)
            cv2.waitKey(10)

    else:
        print "camera open failed"
    	    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_cam()
