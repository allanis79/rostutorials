#!/usr/bin/env python

import rospy

from geometry_msgs.msg import Twist

class GoAround:

	def __init__(self):
		self.publisher = rospy.Publisher('cmd_vel',Twist,queue_size=1)


	def function(self):
		red_light_twist = Twist()
		green_light_twist = Twist()
		green_light_twist.linear.x = 0.5

		driving_forward = False
		light_change_time = rospy.Time.now()
		rate = rospy.Rate(1)

		while not rospy.is_shutdown():
			if not driving_forward:
				print 'move'
				self.publisher.publish(green_light_twist)
				rate.sleep()
				driving_forward = True
			else:
				print 'stop'
				self.publisher.publish(red_light_twist)
				rate.sleep()
				driving_forward = False



if __name__ == '__main__':
	GA = GoAround()
	rospy.init_node('startstop')
	rospy.loginfo('startstop')

	try:
		GA.function()

	except rospy.ROSInterruptException:
		pass

