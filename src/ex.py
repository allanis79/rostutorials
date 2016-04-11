#!/usr/bin/env python

from math import pi
from threading import Lock
from fake_sensor import FakeSensor
import rospy
import tf
from geometry_msgs.msg import Quaternion

if __name__ == '__main__':
    sensor = FakeSensor()
    rospy.init_node('fake_sensor')

    pub = rospy.Publisher('angle', Quaternion, queue_size=10) 

    rate = rospy.Rate(10.0)
    v = sensor.value()
    print v

    #while not rospy.is_shutdown():
        #v = sensor.value()
        #print v
        #sensor.register_callback(publish_value(v))