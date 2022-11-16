# Created by Emmanuel Quaye.
# modified by [NAME1, NAME2, NAME3...]
# This code Demos the test apparatus.
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION

# import your modules here
from time import sleep
import NEMA_Driver as Nema
import RPi.GPIO as GPIO

# use the set_Up_Board method to set up the rasbery pi
Nema.set_Up_Board()

# The pins are as follow:---> Please use this method of labeling the pins to keep code simple
# 17: Y-Motor1_PUL, 27: Y-Motor1_DIR, 5: Y-Motor2_PUL, 6: Y-Motor2_DIR, 20: X-Motor_PUL,
# 21: X-Motor_DIR, 23: Z-Motor_PUL, 24: Z-Motor_DIR, 22: Enable,
# 26: X-limit, 19: Y-limit,
# Leave DIR+ and ENA+ disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.

# The test bench location informations 1st and 2nd row (2nd row is @ X = 300) i.e 1st row in back, 2nd in front
Water_Meter_Location_1 = [100, 100, 100]
Water_Meter_Location_2 = [100, 100, 100]

meters_Per_Row = 3

Nema.Camera_X = c_X = 0
Nema.Camera_Y = c_Y = 0
Nema.Camera_Z = c_Z = 0

Motor_Pin = [17, 27, 5, 6, 20, 21, 23, 24, 22] # all the motor and enable pins you want initialized
limit_Switches = [26, 19, 1] # all the stop switch pins

# use the set_GPIO_Out method to set up GIO outputs
Nema.set_GPIO_Out(Motor_Pin)

# use the set_GPIO_In method to set up GIO inputs
Nema.set_GPIO_In(limit_Switches)

#Set the 8th number in the motor_Pin array as the enable pin correspinding to the real world pin
Nema.Enable = Motor_Pin[8]

rotation = 0 # define rotation
dTT = 0 # define distance to travel
i = 0
while True:
    # due to calculations Max speed = ?1, Min speed = ?2 dont use anything slower or faster for better stability
    # The demo will move the reader in an square fashion testing all the features, it will loop ?3 times taking
    # approximately 8-12 hrs to complete
    # add your functions concurrent with mine to complete the automation proccess..i.e camera_driver functions

    limit_Switches[0] = GPIO.input(limit_Switches[0])
    limit_Switches[1] = GPIO.input(limit_Switches[1])

    # Home the test bench
    Nema.home_Machine(100,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],Motor_Pin[5],Motor_Pin[4],Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # Set the camera location as homed
    c_X = 0
    c_Y = 0
    c_Z = 0


    # Move Z a camera zoom Length
    Nema.reverse(100,100,Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # update the new location
    c_Z += 100


    # Move Y a camera Length
    for y in range(meters_Per_Row):
        Nema.forward_2(100,Water_Meter_Location_1[y],Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location

        c_Y += Water_Meter_Location_1[y]

        # use camera methods to get the camera reading so the program can continue, append it to a list

    # Move Z back a camera zoom Length
    Nema.forward(100,100,Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # update the new location
    c_Z -= 100

    # Move X the camera to the front row
    Nema.forward(100,300,Motor_Pin[5],Motor_Pin[4],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # update the new location
    c_X += 300

    # Move Z a camera zoom Length
    Nema.reverse(100,100,Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # update the new location
    c_Z += 100

    # use camera methods to get the camera reading so the program can continue, append it to a list

    # Move Y back a camera Length
    for y in range(meters_Per_Row):
        Nema.reverse_2(100,Water_Meter_Location_2[y],Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_Y += Water_Meter_Location_2[y]

        # use camera methods to get the camera reading so the program can continue, append it to a list

    # Move Z back a camera zoom Length
    Nema.forward(100,100,Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.enable_Motor() # re-enable the motors
    # update the new location
    c_Z -= 100

    sleep(0.05)

#GPIO.cleanup()