#!/usr/bin/env python

import rospy
import sys,select,tty,termios

from std_msgs.msg import String

class Key_Publish:
	def __init__(self):
		self.publisher = rospy.Publisher('keys',String,queue_size=1)


	def key(self):
		old_attr = termios.tcgetattr(sys.stdin)
		tty.setcbreak(sys.stdin.fileno())
		rate = rospy.Rate(100)
		print 'publishing keystrokes. press ctrl+C to exit: '

		while not rospy.is_shutdown():
			if select.select([sys.stdin],[],[],0)[0] == [sys.stdin]:
				a=sys.stdin.read(1)
				self.publisher.publish(a)
			rate.sleep()


		termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_attr)



if __name__ == '__main__':
	KP = Key_Publish()
	rospy.init_node('keyboard_driver')
	KP.key()
