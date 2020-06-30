## roslab2
Timer Python examples

How to Use a ROS Timer in Python to Publish Data at a Fixed Rate

Suppose, you have a sensor from which you read data in a ROS node, and you want to publish this data on a ROS topic.

The easiest and most straightforward way to do that is simply to setup a ROS rate, and then to read and publish the data.

But there is a better way so you have more control over the data you read, the computation you can make on the data (for example: oversampling + averaging), and the rate at which you publish the data.

In this lab I will show you how to do that using a ROS Timer in Python.

Let’s go step by step through code iterations so you can easily understand. To give more clarity, let’s say that the sensor we’re using is a temperature sensor.

# 1. The easiest way (no Timer): pub_sensor.py


