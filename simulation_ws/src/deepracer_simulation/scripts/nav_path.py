#!/usr/bin/env python
import rospy
from nav_msgs.msg import Path
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Pose2D
from gazebo_msgs.msg import ModelStates
from std_msgs.msg import Header
from tf.transformations import quaternion_from_euler

path = Path()

def set_position(data):
    header = Header()
    header.frame_id='/map'
    header.stamp = rospy.Time.now()
    global path
    
    path.header = header
    pose = PoseStamped()
    pose.header = path.header
    pose.pose.position.x = data.x
    pose.pose.position.y = data.y
    pose.pose.position.z = 0.0

    q = quaternion_from_euler(0, 0, -data.theta)
    pose.pose.orientation.x = q[0]
    pose.pose.orientation.y = q[1]
    pose.pose.orientation.z = q[2]
    pose.pose.orientation.w = q[3]  

    path.poses.append(pose)
    path_pub.publish(path)

rospy.init_node('path_node')

rospy.Subscriber("/pose2D", Pose2D, set_position)
path_pub = rospy.Publisher('/path', Path, queue_size=10)

if __name__ == '__main__':
    rospy.spin()
