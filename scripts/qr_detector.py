#! /usr/bin/env python

import cv2
import rospy
import pyqrcode
import numpy as np
from pyzbar.pyzbar import decode
from std_msgs.msg import *
from sensor_msgs.msg import *

cap = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=(int)800, height=(int)600, format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv ! video/x-raw, format=(string)BGRx ! videoconvert !  appsink", cv2.CAP_GSTREAMER)

pub_found_qrcode = rospy.Publisher("/qr_detector_navigation/qr_found", Bool, queue_size=10)
pub_coordinates = rospy.Publisher("/qr_detector_navigation/qr_coordinates", String, queue_size=10)


def open_cam():
    if cap.isOpened():
	while cap.isOpened():
            ret, img = cap.read()
    	    cv2.imshow('CSI-camera', img)
            cv2.waitKey(10) 

    else:
        print "camera open failed"
    	    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    open_cam()
