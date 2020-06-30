#!/usr/bin/env python
import rospy
from std_msgs.msg import Float64
class TemperatureSensor:
    def read_temperature_sensor_data(self, event=None):
        # Here you read the data from your sensor
        # And you return the real value
        self.temperature = 30.0
    def __init__(self):
        # Create a ROS publisher
        self.temperature_publisher = rospy.Publisher("/temperature", Float64, queue_size=1)
        # Initialize temperature data
        self.temperature = 0
    def publish_temperature(self, event=None):
        msg = Float64()
        msg.data = self.temperature
        self.temperature_publisher.publish(msg)
if __name__ == '__main__':
    rospy.init_node("your_sensor_node")
    # Create an instance of Temperature sensor
    ts = TemperatureSensor()
    # Create a ROS Timer for reading data
    rospy.Timer(rospy.Duration(1.0/10.0), ts.read_temperature_sensor_data)
    # Create another ROS Timer for publishing data
    rospy.Timer(rospy.Duration(1.0/10.0), ts.publish_temperature)
    # Don't forget this or else the program will exit
    rospy.spin()
