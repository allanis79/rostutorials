#!/usr/bin/env python

import rospy
from nav_msgs.msg import Odometry


def callbacK(data):
	print 'krishna'
	print data.pose.pose.position


if __name__ =='__main__':
	print 'sai'
	rospy.init_node('sub_odom')
	rospy.Subscriber('/odom',Odometry,callbacK)
	rospy.spin()
