#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Pose 




def et():

	pub = rospy.Publisher('example', Pose, queue_size = 10)
	rospy.init_node('Exx')
	rate = rospy.Rate(10)

	while not rospy.is_shutdown():
		p = Pose()
		p.position.x = 1.0
		p.position.y = 1.0
		p.position.z = 1.0
		p.orientation.x = 1.0
		p.orientation.y = 1.0
		p.orientation.z = 1.0
		p.orientation.w = 1.0


		pub.publish(p)
		rate.sleep()



if __name__ == '__main__':
	et()
