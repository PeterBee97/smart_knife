#!/usr/bin/env python2

import rospy
from geometry_msgs.msg import Vector3Stamped
from sensor_msgs.msg import JointState

def callback(data):
    pub = rospy.Publisher('/imu_rpy_filtered',JointState, queue_size=10);
    JS = JointState()
    JS.position = [data.vector.x, data.vector.y, data.vector.z]
    JS.name = ['joint_knife_x', 'joint_knife_y', 'joint_knife_z']
    JS.header = data.header
    pub.publish(JS)
    rospy.loginfo(JS.position)

def rpy_translator():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('rpy_translator', anonymous=True)

    rospy.Subscriber('/imu/rpy/filtered', Vector3Stamped, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    rpy_translator()
