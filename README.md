# Deepracer_PID_Control
PID tracking of waypoints by Amazon Deepracer in Gazebo simulation and visualizing in rviz.

## To run the simulation without Joystick </br>
Modify the Gazebo world in `racecar_indoorenvironment_nojoystick.launch` launch file 
```roslaunch deepracer_simulation racecar_indoorenvironment_nojoystick.launch```</br>

## To launch the ROS node for publishing a path
```rosrun deepracer_simulation nav_path.py```

## To run PID tracking on a list of waypoints
Modify the waypoints in `route_smooth.csv` file
```rosrun deepracer_simulation pid_controller.py```

## Visualize the navigated path in rviz
https://youtu.be/zqGjBnYuFS0


