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

Nema.Camera_X = c_X = 0
Nema.Camera_Y = c_Y = 0
Nema.Camera_Z = c_Z = 0

Motor_Pin = [17, 27, 5, 6, 20, 21, 23, 24, 22] # all the motor and enable pins you want initialized
limit_Switches = [4, 26, 19] # all the stop switch pins

distance_Array = [Nema.small_Amount, Nema.medium_Amount, Nema.large_Amount, Nema.small_Amount]# all distance values to use
speed_Array = [500,700,900,500] # all speed values to use

# use the set_GPIO_Out method to set up GIO outputs
Nema.set_GPIO_Out(Motor_Pin)

# use the set_GPIO_In method to set up GIO inputs
Nema.set_GPIO_In(limit_Switches)


#Set the 8th number in the motor_Pin array as the enable pin correspinding to the real world pin
Nema.Enable = Motor_Pin[8]

Homed = False

distance_Int = 1
speed_Int = 1

speed = 0
distance = 0

Nema.enable_Motor() # re-enable the motors

while True:
    # This file will move the x axis a set amount..just for jogging pourposes
    
    if(Homed != True):
        # Home the test bench
        Nema.home_Machine(600,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],Motor_Pin[5],Motor_Pin[4],Motor_Pin[7],Motor_Pin[6],limit_Switches)
        # Set the camera location as homed
        c_X = 0
        c_Y = 0
        c_Z = 0
        Homed = True
        Nema.enable_Motor() # re-enable the motors

    if(speed_Int > 2 or speed_Int < 0):
        speed_Int = 0
    if(distance_Int > 2 or distance_Int < 0 ):
        distance_Int = 0
    char = input()
    
    if(char == 'e'):
        speed_Int += 1
        speed = speed_Array[speed_Int]
        print("speed = " + str(speed))
    
    if(char == 'q'):
        distance_Int += 1
        distance = distance_Array[distance_Int]
        print("distance = " + str(distance))
        
    if(char == 'w'):
        #Move the Y axis mototors forward
        Nema.reverse_2(speed,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches[2])
        # update the new location
        c_Y -= distance
        print("moved the Y motors " + str(distance) + " millimeters")
        
    if(char == 's'):
        #Move the Y axis mototors reverse
        Nema.forward_2(speed,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches[2])
        # update the new location
        c_Y += distance
        print("moved the Y motors " + str(distance) + " millimeters")
        
    if(char == 'a'):
        #Move the X axis mototors forward
        Nema.forward(speed,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
        # update the new location
        c_X -= distance
        print("moved the Y motors " + str(distance) + " millimeters")
        
    if(char == 'd'):
        #Move the X axis mototors reverse
        Nema.reverse(speed,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
        # update the new location
        c_X += distance
        print("moved the Y motors " + str(distance) + " millimeters")
        
    if(char == 'r'):
        #Move the Z axis mototors forward
        Nema.forward(speed,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
        # update the new location
        c_Z += distance
        print("moved the Y motors " + str(distance) + " millimeters")
        
    if(char == 'f'):
        #Move the Z axis mototors reverse
        Nema.reverse(speed,distance,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
        # update the new location
        c_Z -= distance
        print("moved the Z motors " + str(distance) + " millimeters")
        
    Nema.Camera_X = c_X
    Nema.Camera_Y = c_Y
    Nema.Camera_Z = c_Z
        
    print("X = " + str(c_X) + ": " + "Y = " + str(c_Y) + ": " + "Z = " + str(c_Z) + ": ")
    sleep(0.05)

    
GPIO.cleanup()


