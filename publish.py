# !/usr/bin/env python

import rospy
from std_msgs.msg import String

rospy.init_node('publisher_node', anonymous=True)
pub = rospy.Publisher('chatter', String, queue_size=10)
rate = rospy.Rate(1)  # 1 Hz

while not rospy.is_shutdown():
    message = "Hello, ROS!"
    rospy.loginfo(message)
    pub.publish(message)
    rate.sleep()
