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
Water_Meter_Location_1 = [1500, 1500, 1500]
Water_Meter_Location_2 = [1500, 1500, 1500]

meters_Per_Row = 3

Nema.Camera_X = c_X = 0
Nema.Camera_Y = c_Y = 0
Nema.Camera_Z = c_Z = 0

Motor_Pin = [17, 27, 5, 6, 20, 21, 23, 24, 22] # all the motor and enable pins you want initialized
#limit_Switches = [4, 26, 19] # all the stop switch pins
limit_Switches = [4, 26, 19] # all the stop switch pins pin 4 needs a resistor

# use the set_GPIO_Out method to set up GIO outputs
Nema.set_GPIO_Out(Motor_Pin)

# use the set_GPIO_In method to set up GIO inputs
Nema.set_GPIO_In(limit_Switches)

#Set the 8th number in the motor_Pin array as the enable pin correspinding to the real world pin
Nema.Enable = Motor_Pin[8]

rotation = 0 # define rotation
dTT = 0 # define distance to travel

Homed = False

def toggle_distance(control_Pin):
    #use keyboard button to send input
    if(1==1)

while True:
    # This file will move the x axis a set amount..just for jogging pourposes

    if(control_Pins[6] == 1):
        distance = Nema.small_Amount
    if(control_Pins[7] == 1):
        distance = Nema.medium_Amount
    if(control_Pins[8] == 1):
        distance = Nema.large_Amount

    if(Homed != True):
        # Home the test bench
        Nema.home_Machine(600,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],Motor_Pin[5],Motor_Pin[4],Motor_Pin[7],Motor_Pin[6],limit_Switches)
        # Set the camera location as homed
        c_X = 0
        c_Y = 0
        c_Z = 0

    # move the X foward the jog amount
    if(control_Pins[0] == 1):meters_Per_Row
        Nema.forward(100,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_X += Nema.small_Amount

    # move the X reverse the jog amount
    if(control_Pins[1] == 1):
        Nema.reverse(100,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_X -= Nema.small_Amount

    # Move the Y foward the jog amount
    if(control_Pins[2] == 1):
        Nema.forward_2(100,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_Y += distance

    # Move the Y foward the jog amount
    if(control_Pins[3] == 1):
        Nema.reverse_2(100,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_Y -= distance

    # Move the Z forward the jog amount
    if(control_Pins[4] == 1):
        Nema.reverse(100,distance,Motor_Pin[7],Motor_Pin[6],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_Z += 100

    if(control_Pins[5] == 1):
        Nema.forward(100,distance,Motor_Pin[7],Motor_Pin[6],limit_Switches)
        Nema.enable_Motor() # re-enable the motors
        # update the new location
        c_Z -= 100

    sleep(0.05)

GPIO.cleanup()
