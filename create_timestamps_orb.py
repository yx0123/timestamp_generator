#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Creates rgb.txt file which associates a timestamp with each image file. for use with orbslam. 
"""

import os
import argparse
import rospy
def main():
    parser = argparse.ArgumentParser(description="Extract timestamps from a ROS bag.")
    parser.add_argument("frequency", help="Frequency (fps)")
    parser.add_argument("image_folder", help="Image Directory.")

    args = parser.parse_args()

    rospy.init_node('create_timestamps')

    file = open('rgb.txt', "w+")
    time = rospy.Time.now()
    freq = float(args.frequency)
    T = 1.0/freq
    d = rospy.Duration(T)
    print(str(d.secs) + '.' + str(d.nsecs).zfill(9))
    path = args.image_folder
    num_files = len([f for f in os.listdir(path)if os.path.isfile(os.path.join(path, f))])
    print(num_files)
    file.write("# color images\n# file: #tartanair\n# timestamp filename\n")

    for i in range(num_files):
        file.write(str(time.secs) + '.' + str(time.nsecs).zfill(9)+ " image_left/" + str(i).zfill(6) + "_left.png\n")
        time = time+d
    file.close

    return

if __name__ == '__main__':
    main()
