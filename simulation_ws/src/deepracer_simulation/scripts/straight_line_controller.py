#!/usr/bin/env python3
import rospy
import time
from std_msgs.msg import Bool
from std_msgs.msg import Float32
from std_msgs.msg import Float64
from ackermann_msgs.msg import AckermannDriveStamped

def servo_commands():
    rospy.init_node('servo_commands', anonymous=True)    

    x_pub = rospy.Publisher('/vesc/low_level/ackermann_cmd_mux/output',AckermannDriveStamped,queue_size=1)
    msg = AckermannDriveStamped()    
    
    while not rospy.is_shutdown():
      msg.drive.speed = 1.0
      x_pub.publish(msg)
	
    time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = 1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)
  
  	msg.drive.speed = -1.0
      	x_pub.publish(msg)
  	time.sleep(1)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    try:
        servo_commands()
    except rospy.ROSInterruptException:
        pass
