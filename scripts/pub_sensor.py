#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
#class TemperatureSensor:
def read_temperature_and_publish():
     # Start a new node
     rospy.init_node('your_sensor_node', anonymous=True)

     # Create a ROS publisher
     temperature_publisher = rospy.Publisher("/temperature", Float64, queue_size=1)

     # Here you read the data from your sensor
     # And you return the real value
     temperature = 30.0

     # Set temperature for msg
     msg = Float64()
     msg.data = temperature

     rate = rospy.Rate(10)
  
     while not rospy.is_shutdown():

         temperature_publisher.publish(msg)
         rospy.loginfo("Temperature published: %f", temperature)
         rate.sleep()
 
if __name__ == '__main__':

    read_temperature_and_publish()
