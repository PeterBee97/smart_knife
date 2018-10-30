#!/usr/bin/env python2

################################################################################
# COPYRIGHT(c) 2018 STMicroelectronics                                         #
#                                                                              #
# Redistribution and use in source and binary forms, with or without           #
# modification, are permitted provided that the following conditions are met:  #
#   1. Redistributions of source code must retain the above copyright notice,  #
#      this list of conditions and the following disclaimer.                   #
#   2. Redistributions in binary form must reproduce the above copyright       #
#      notice, this list of conditions and the following disclaimer in the     #
#      documentation and/or other materials provided with the distribution.    #
#   3. Neither the name of STMicroelectronics nor the names of its             #
#      contributors may be used to endorse or promote products derived from    #
#      this software without specific prior written permission.                #
#                                                                              #
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"  #
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE    #
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE   #
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE    #
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR          #
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF         #
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS     #
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN      #
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)      #
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE   #
# POSSIBILITY OF SUCH DAMAGE.                                                  #
################################################################################

################################################################################
# Author:  Davide Aliprandi, STMicroelectronics                                #
################################################################################


# DESCRIPTION
#
# This application example shows how to perform a Bluetooth Low Energy (BLE)
# scan, connect to a device, retrieve its exported features, and get push
# notifications from it.


# IMPORT

from __future__ import print_function
import sys
import os
import time
from abc import abstractmethod
from bluepy.btle import BTLEException

from blue_st_sdk.manager import Manager
from blue_st_sdk.manager import ManagerListener
from blue_st_sdk.node import NodeListener
from blue_st_sdk.feature import FeatureListener
from blue_st_sdk.features.feature_audio_adpcm import FeatureAudioADPCM
from blue_st_sdk.features.feature_audio_adpcm_sync import FeatureAudioADPCMSync
import rospy
from sensor_msgs.msg import Imu, MagneticField
# from madgwick_py.madgwickahrs import MadgwickAHRS

# PRECONDITIONS
#
# Please remember to add to the "PYTHONPATH" environment variable the location
# of the "BlueSTSDK_Python" SDK.
#
# On Linux:
#   export PYTHONPATH=/home/<user>/BlueSTSDK_Python


# CONSTANTS

# Presentation message.
INTRO = """##################
# BlueST Example #
##################"""

# Bluetooth Scanning time in seconds.
SCANNING_TIME_s = 5

# Number of notifications to get before disabling them.
NOTIFICATIONS = 10


# FUNCTIONS

#
# Printing intro.
#
def print_intro():
    rospy.loginfo('\n' + INTRO + '\n')


# INTERFACES

#
# Implementation of the interface used by the Manager class to notify that a new
# node has been discovered or that the scanning starts/stops.
#
class MyManagerListener(ManagerListener):

    #
    # This method is called whenever a discovery process starts or stops.
    #
    # @param manager Manager instance that starts/stops the process.
    # @param enabled True if a new discovery starts, False otherwise.
    #
    def on_discovery_change(self, manager, enabled):
        rospy.loginfo('Discovery %s.' % ('started' if enabled else 'stopped'))
        if not enabled:
            rospy.loginfo("\n")

    #
    # This method is called whenever a new node is discovered.
    #
    # @param manager Manager instance that discovers the node.
    # @param node    New node discovered.
    #
    def on_node_discovered(self, manager, node):
        rospy.loginfo('New device discovered: %s.' % (node.get_name()))


#
# Implementation of the interface used by the Node class to notify that a node
# has updated its status.
#
class MyNodeListener(NodeListener):

    #
    # To be called whenever a node changes its status.
    #
    # @param node       Node that has changed its status.
    # @param new_status New node status.
    # @param old_status Old node status.
    #
    def on_status_change(self, node, new_status, old_status):
        rospy.loginfo('Device %s went from %s to %s.' %
              (node.get_name(), str(old_status), str(new_status)))


#
# Implementation of the interface used by the Feature class to notify that a
# feature has updated its data.
#
class MyFeatureListener(FeatureListener):
    num = 0

    #
    # To be called whenever the feature updates its data.
    #
    # @param feature Feature that has updated.
    # @param sample  Data extracted from the feature.
    #
    def on_update(self, feature, sample):
        if (self.num < NOTIFICATIONS):
            rospy.loginfo(feature)
            self.num += 1


# MAIN APPLICATION

#
# Main application.
#
def main(argv):
    rospy.init_node('sensortile', anonymous=True)
    pub_data_raw = rospy.Publisher('imu/data_raw', Imu, queue_size=10)
    pub_mag = rospy.Publisher('imu/mag', MagneticField, queue_size=10)
    sample_freq = 100
    sample_period = 1.0/sample_freq
    rate = rospy.Rate(sample_freq)  # hz
    g = 9.81645  # Pittsburgh, PA (from WolframAlpha)
    mg = g*0.001
    seq = 0
    # Printing intro.
    print_intro()

    try:
        # Creating Bluetooth Manager.
        manager = Manager.instance()
        manager_listener = MyManagerListener()
        manager.add_listener(manager_listener)

        while True:
            # Synchronous discovery of Bluetooth devices.
            rospy.loginfo('Scanning Bluetooth devices...\n')
            manager.discover(False, SCANNING_TIME_s)

            # Getting discovered devices.
            devices = manager.get_nodes()

            # Listing discovered devices.
            if not devices:
                rospy.loginfo('\nNo Bluetooth devices found. Try again in 5 secs...')
                time.sleep(5)
                continue
            # rospy.loginfo('\nAvailable Bluetooth devices:')
            # i = 1
            for device in devices:
                # rospy.loginfo('%d) %s: [%s]' % (i, device.get_name(), device.get_tag()))
                if device.get_name().find('AM')==0:
                    break
                # i += 1
            if not device.get_name().find('AM')==0:
                continue
            # if (len(devices)>1):
            # # Selecting a device.
            #     while True:
            #         choice = int(input("\nSelect a device (\'0\' to quit): "))
            #         if choice >= 0 and choice <= len(devices):
            #             break
            #     if choice == 0:
            #     # Exiting.
            #         manager.remove_listener(manager_listener)
            #         rospy.loginfo('Exiting...\n')
            #         sys.exit(0)
            #     device = devices[choice - 1]

            # Connecting to the device.
            node_listener = MyNodeListener()
            device.add_listener(node_listener)
            while True:
                rospy.loginfo('\nConnecting to %s...' % (device.get_name()))
                try:
                    device.connect()
                    rospy.loginfo('Connection done.')
                    break
                except BTLEException as e:
                    rospy.loginfo(e)
                    time.sleep(1)
                    continue
            features = device.get_features()
            for feature in features:
                if feature.get_name()=="Magnetometer":
                    Mag = feature
                    mag_listener = MyFeatureListener()
                    Mag.add_listener(mag_listener)
                    device.enable_notifications(Mag)
                elif feature.get_name()=="Gyroscope":
                    Gyro = feature
                    gyro_listener = MyFeatureListener()
                    Gyro.add_listener(gyro_listener)
                    device.enable_notifications(Gyro)
                elif feature.get_name()=="Accelerometer":
                    Acc = feature
                    acc_listener = MyFeatureListener()
                    Acc.add_listener(acc_listener)
                    device.enable_notifications(Acc)

            # AHRS = MadgwickAHRS(sample_period)
            while not rospy.is_shutdown():
                if device.wait_for_notifications(sample_period):
                    print(Gyro, Mag, Acc)
                    gyro = [w*0.01745329252 for w in Gyro._last_sample._data]
                    mag = Mag._last_sample._data
                    acc = Acc._last_sample._data
                    # AHRS.update(gyro,acc,mag)
                    # q = AHRS.quaternion
                    IMU = Imu()
                    IMU.angular_velocity.x = -gyro[0]
                    IMU.angular_velocity.y = -gyro[1]
                    IMU.angular_velocity.z = gyro[2]
                    IMU.linear_acceleration.x = acc[0]*mg
                    IMU.linear_acceleration.y = acc[1]*mg
                    IMU.linear_acceleration.z = -acc[2]*mg
                    # IMU.orientation.w = q[0]
                    # IMU.orientation.x = q[1]
                    # IMU.orientation.y = q[2]
                    # IMU.orientation.z = q[3]
                    IMU.header.stamp = rospy.Time.now()
                    IMU.header.frame_id = "sensortile_imu"
                    IMU.header.seq = seq
                    pub_data_raw.publish(IMU)
                    MAG = MagneticField()
                    MAG.magnetic_field.x = mag[0]
                    MAG.magnetic_field.y = mag[1]
                    MAG.magnetic_field.z = mag[2]
                    MAG.header.stamp = rospy.Time.now()
                    MAG.header.frame_id = "sensortile_mag"
                    MAG.header.seq = seq
                    pub_mag.publish(MAG)
                    seq += 1
                    rate.sleep()
    except rospy.ROSInterruptException:
        pass
    except BTLEException as e:
        device.disable_notifications(Mag)
        device.disable_notifications(Gyro)
        device.disable_notifications(Acc)
        rospy.loginfo(e)
        # Exiting.
        rospy.loginfo('Exiting...\n')
        sys.exit(0)
    except KeyboardInterrupt:
        try:
            # Exiting.
            rospy.loginfo('\nExiting...\n')
            sys.exit(0)
        except SystemExit:
            os._exit(0)


if __name__ == "__main__":
    main(sys.argv[1:])
