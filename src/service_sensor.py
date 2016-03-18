#!/usr/bin/env python

from math import pi
from fake_sensor import FakeSensor
import rospy, tf 
from geometry_msgs.msg import Quaternion
from RosTut.srv import FakeSensor,FakeSensorResponse 

def make_quaternion(angle):
	q =tf.transformations.quaternion_from_euler(0,0,angle)
	return Quaternion(q)


def callback(request):
	angle = sensor.value()*2*pi/100.0
	q = make_quaternion(angle)

	return FakeSensorResponse(q)


if __name__ == '__main__':
	sensor = FakeSensor()

	rospy.init_node('fake_sensor')

	service = rospy.Service('angle',FakeSensor,callback)