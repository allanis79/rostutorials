#!/usr/bin/env python

import rospy
from sensor_msgs.msg import Image
import cv2, cv_bridge
import numpy as np
from geometry_msgs.msg import Twist



class Follower:
	def __init__(self):
		self.sub = rospy.Subscriber('/camera/rgb/image_raw',Image,self.callback)
		self.pub = rospy.Publisher('cmd_vel_mux/input/teleop',Twist,queue_size=1)
		self.bridge = cv_bridge.CvBridge()
		cv2.namedWindow('window',1)
		self.twist = Twist()



	def callback(self,msg):
		image = self.bridge.imgmsg_to_cv2(msg, desired_encoding = 'bgr8')
		hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
		lower_yellow = np.array([10,10,10])
		upper_yellow = np.array([255,255,250])
		mask = cv2.inRange(hsv,lower_yellow,upper_yellow)
		h,w,d = image.shape

		search_top = 3*h/4
		search_bot = search_top + 20
		mask[0:search_top, 0:w] = 0
		mask[search_bot:h, 0:w] = 0

		M = cv2.moments(mask)

		if M['m00'] > 0:
			cx = int(M['m10']/M['m00'])
			cy =  int(M['m01']/M['m00'])
			cv2.circle(image,(cx,cy),20,(0,0,255), -1)
			err = cx - w/2
			self.twist.linear.x = 0.2
			self.twist.angular.z = -float(err)/100
			self.pub.publish(self.twist)

		cv2.imshow('window',image)
		cv2.waitKey(3)




if __name__ == '__main__':
	rospy.init_node('follower')
	Follower()
	rospy.spin()