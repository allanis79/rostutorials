#!/usr/bin/env python

import ros
import rospy
import actionlib
from smach import State,StateMachine
from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal
from smach_ros import SimpleActionState

waypoints = [
['one', (2.1, 2.2), (0.0, 0.0, 0.0, 1.0)],
['two', (6.5, 4.43), (0.0, 0.0, -0.984047240305, 0.177907360295)]
]

class Waypoint(State):
	def __init__(self, position, orientation):
		State.__init__(self, outcomes=['success'])
		# Get an action client
		self.client = actionlib.SimpleActionClient('move_base', MoveBaseAction)
		self.client.wait_for_server()
		# Define the goal
		self.goal = MoveBaseGoal()
		self.goal.target_pose.header.frame_id = 'map'
		self.goal.target_pose.pose.position.x = position[0]
		self.goal.target_pose.pose.position.y = position[1]
		self.goal.target_pose.pose.position.z = 0.0
		self.goal.target_pose.pose.orientation.x = orientation[0]
		self.goal.target_pose.pose.orientation.y = orientation[1]
		self.goal.target_pose.pose.orientation.z = orientation[2]
		self.goal.target_pose.pose.orientation.w = orientation[3]
	def execute(self, userdata):
		self.client.send_goal(self.goal)
		self.client.wait_for_result()
		return 'success'

if __name__ == '__main__':
	rospy.init_node('patrol')
	patrol = StateMachine('success')
	with patrol:
		for i,w in enumerate(waypoints):
			StateMachine.add(w[0],Waypoint(w[1], w[2]), \
				transitions={'success':waypoints[(i + 1) % \
			len(waypoints)][0]})
	patrol.execute()

'''
if __name__ == '__main__':
	patrol = StateMachine('success')
	with patrol:
		for i,w in enumerate(waypoints):
			goal_pose = MoveBaseGoal()
			goal_pose.target_pose.header.frame_id = 'map'
			goal_pose.target_pose.pose.position.x = w[1][0]
			goal_pose.target_pose.pose.position.y = w[1][1]
			goal_pose.target_pose.pose.position.z = 0.0
			goal_pose.target_pose.pose.orientation.x = w[2][0]
			goal_pose.target_pose.pose.orientation.y = w[2][1]
			goal_pose.target_pose.pose.orientation.z = w[2][2]
			goal_pose.target_pose.pose.orientation.w = w[2][3]
			StateMachine.add(w[0],
			SimpleActionState('move_base',
			MoveBaseAction,
			goal=goal_pose),
			transitions={'success':waypoints[(i + 1) % \
			len(waypoints)][0]})
	patrol.execute()
'''