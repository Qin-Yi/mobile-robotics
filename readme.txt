The analog data is sampled with 500Hz (limitations regarding transmission of those values over the serial line from the arduino). The bag files contain the time-stamped information and also the input commands given to the robot (500Hz) and the position estimate (based on the wheel odometry) (50 Hz). 

See scenario.jpg for the environment the data was taken in. 
All datasets start with the robot at the depicted position - directly ontop of the line.
Follow line is a dataset where the robot drives along the black line to the end (37 seconds).
Straight drives forward till is reaches the line again (15 seconds).
Static is the data of the robot standing still (24 seconds).

The according text files have two columns: The first is the photo-diode value and the second one is the distance sensor value. The data is sampled with 500 Hz. 

rawdata.png shows nice data from the beginning of the follow line dataset. Despite the name depicted in the image the data is actually raw data. The turqise line on top ("theta") is from the distance sensor that is at its maximum when the arm is pointing down. The red line ("y") is the data from the photo diode. Higher values mean less light.

Raw noise data show data from the follow line dataset with more noise present. The black line is to the right of the robot.

image.jpg shows the data of the light sensor collected when slowly driving forward.

tarp.mov is a video of one such run. It is made on white tarp because the floor in the lecture hall is dark. 


