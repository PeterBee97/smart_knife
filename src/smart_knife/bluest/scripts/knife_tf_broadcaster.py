#!/usr/bin/env python2

import rospy, tf
from sensor_msgs.msg import Imu


def imu_data_callback(data):
    br = tf.TransformBroadcaster()
    br.sendTransform((0, 0, 0),
                     data.orientation,
                     rospy.Time.now(),
                     "knife_link",
                     "knife_base")


def knife_tf_broadcaster():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('imu_data_tf_broadcaster', anonymous=True)

    rospy.Subscriber('/imu/data', Imu, imu_data_callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    knife_tf_broadcaster()
