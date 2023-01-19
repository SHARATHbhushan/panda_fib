#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
import numpy as np
from std_msgs.msg import Bool
class firos:


    def __init__(self):
        #noise = np.random.normal(10,1,1)
        #print(noise)
        self.goal_state_subscriber = rospy.Subscriber("goal_state", Bool, self.goal_callback)
        self.joint_state_publisher = rospy.Publisher("joint_states", JointState, queue_size=10)
        self.joint_state_fake_subscriber = rospy.Subscriber("joint_states_fake", JointState, self.callback)
        self.goal = False
        
        
    def goal_callback(self,goal):   
        self.goal = goal.data

    def callback(self,data):       
        self.joint_data = data        
        #print(data.position[1])
        if self.goal == True:
            self.list_joint_data = list(self.joint_data.position)
            #print(self.list_joint_data)
            self.list_joint_data[2] = self.list_joint_data[2] + np.random.normal(10,1,1)[0]
            print("noise error injected")
            self.joint_data.position = tuple(self.list_joint_data)
            #self.joint_data.position[1] = error_data
            #self.joint_state_publisher.publish(self.joint_data)
            #self.joint_state_publisher.publish(data)
            self.goal = False
        #print(self.joint_data)
        self.joint_state_publisher.publish(self.joint_data)

           
        
        


if __name__ == '__main__':
    rospy.init_node('FIB')
    firos()
    rospy.spin()