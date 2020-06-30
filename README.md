## roslab2
Timer Python examples

How to Use a ROS Timer in Python to Publish Data at a Fixed Rate

Suppose, you have a sensor from which you read data in a ROS node, and you want to publish this data on a ROS topic.

The easiest and most straightforward way to do that is simply to setup a ROS rate, and then to read and publish the data.

But there is a better way so you have more control over the data you read, the computation you can make on the data (for example: oversampling + averaging), and the rate at which you publish the data.

In this lab I will show you how to do that using a ROS Timer in Python.

Let’s go step by step through code iterations so you can easily understand. To give more clarity, let’s say that the sensor we’re using is a temperature sensor.

#### 1. The easiest way (no Timer): pub_sensor.py

In this example, you first initialize your node and create a publisher for the data. Then, with a ROS Rate, you read and publish the temperature data at a given frequency (fixed at 10 Hz for this example).

Note that the read_temperature_sensor_data() function is not implemented. This is your job to write the code here, depending on the sensor you’re using (maybe you need to read with an I2C library, maybe it’s over serial communication, etc). For the sake of this example I have fixed the value at 30.0 (°C, °F, whatever you want).

#### 2. The easy way (but with a class): pub_sensor_class.py

This code has the exact same behavior as the previous one, except that here we’ll use a class instead. This is a preparation for what comes next.

As you can see the temperature is now an attribute of the TemperatureSensor class. We are still reading the data, publishing the data, and waiting for the next iteration with the ROS Rate.

#### 3. Read data and publish asynchronously with a ROS Timer: pub_sensor_class_timer.py

Time to use the ROS Timer functionality!

A ROS Timer allows you to set a callback that will be triggered at a given rate. To create a timer, you need to give it the duration to wait between 2 callback triggers, and of course the function to call.

As you can see, I have created one Timer to read the temperature data from the sensor, and another one to publish this data.

So, what has changed ?

Well, you are now reading data and publishing data asynchronously! Here we kept 10 Hz for both actions, but you can easily modify the value for both Timers.

Let’s see that with another iteration of the code.

#### 4. Improvement: Oversampling and averaging: timer_example.py

Oversampling means that we’ll increase the frequency at which we read the data. This will allow you to get a more updated value when you publish it.

With more data samples between each publication on the ROS topic, you also have the possibility to filter the data (ex: with a complementary filter or a Kalman filter). In this example, we’ll simply add a filter that updates the temperature with the average of the 2 last read values.

Now we are reading the temperature data at 100 Hz, while still publishing the data at 10 Hz.

With the filter that we added to compute the average of the last 2 read data, the frequency at which we update the “temperature” attribute is 50 Hz.

It means we have a 5x oversampling on a value which is already filtered.

As you can see it’s not really hard to get to this result with the ROS Timer functionality.

### Conclusion: 
Using this code structure is an efficient way to manage your sensors. By separating the reading, processing, and publishing of the data, you gain more control over your application, which also becomes more scalable.

