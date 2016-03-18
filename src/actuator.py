#!/usr/bin/env python

from fake_actuator import FakeActuator 

import rospy
import actionlib
from std_msgs.msg import Float32

from RosTut.srv import Light,LightResponse
from sensors.msg import RotationAction,RotationFeedback,RotationResult

def volume_callback(msg):
	actuator.set_volume(min(100,max(0,int(msg.data*100))))

def light_callback(request):
	actuator.toggle_light(request.on)
	return LightResponse(actuator.light_on())

def rotation_callback(goal):
	feedback = RotationFeedback()
	result = RotationResult()
	actuator.set_position(goal.orientation)
	success = True

	rate = rospy.Rate(10)
	while fabs(goal.orientation - actuator.position()) > 0.01:
		if a.is_preempt_requested():
			success =False
			break;
		feedback.current_orientation = actuator.position()
		a.publish_feedback(feedback)
		rate.sleep()

	result.final_orientation =actuator.position()
	if success:
		a.set_succedded(result)
	else:
		a.set_preempted(result)





if __name__ == '__main__':
	actuator = FakeActuator()

	rospy.init_node('fake_actuator')

	t = rospy.Subscriber('fake/volume',Float32,volume_callback)

	s= rospy.Service('fake/light',Light,light_callback)

	a = actionlib.SimpleActionServer('fake/position',RotationAction,
		execute_cb = rotation_callback,auto_start = False)

	a.start()

	rospy.spin()