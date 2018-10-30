#!/usr/bin/env python2
import rospy
from sensor_msgs.msg import Imu, MagneticField

def faker():
    imu_pub = rospy.Publisher('/imu/data_raw', Imu, queue_size=10)
    mag_pub = rospy.Publisher('/imu/mag', MagneticField, queue_size=10)
    rospy.init_node('imu_faker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        IMU = Imu()
        IMU.header.stamp = rospy.Time.now()
        IMU.linear_acceleration.x = 0.0
        IMU.linear_acceleration.y = 0.0
        IMU.linear_acceleration.z = 0.0
        IMU.angular_velocity.x = 0.0
        IMU.angular_velocity.y = 0.0
        IMU.angular_velocity.z = 0.0
        imu_pub.publish(IMU)
        MAG = MagneticField()
        MAG.header.stamp = rospy.Time.now()
        MAG.magnetic_field.z = 1.00
        MAG.magnetic_field.x = 0.01
        MAG.magnetic_field.y = 0.01
        mag_pub.publish(MAG)
        rate.sleep()

if __name__ == '__main__':
    try:
        faker()
    except rospy.ROSInterruptException:
        pass
