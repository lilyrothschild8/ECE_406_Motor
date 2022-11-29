# Created by Emmanuel Quaye.
# modified by [NAME1, NAME2, NAME3...]
# This is the main code to run the the test apparatus.
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION

# set the NEMA driver path to the system
import NEMA_Driver as Nema
# import your modules here
from time import sleep


import RPi.GPIO as GPIO

# use the set_Up_Board method to set up the rasbery pi
Nema.set_Up_Board()

# The Motor pins are as follow:---> Please use this method of labeling the pins to keep code simple
# 17: Y-Motor1_PUL, 27: Y-Motor1_DIR, 5: Y-Motor2_PUL, 6: Y-Motor2_DIR, 20: X-Motor_PUL,
# 21: X-Motor_DIR, 23: Z-Motor_PUL, 24: Z-Motor_DIR, 22: Enable, 12: LED,
# 26: X-limit, 19: Y-limit, 4: Z_limit

# The ST7735 pins are as follow:---> Please use this method of labeling the pins to keep code simple
# 12: Reset, GND: GND, 3v: VIN, 25: D/C, 8: CS, 10: MOSI, 11: CLK, 13: Lite
# Leave DIR+ and ENA+ disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.

# The test bench location informations 1st and 2nd row (2nd row is @ X = 300) i.e 1st row in back, 2nd in front
dspwmr1 = 300
dspwmr2 = 300
Water_Meter_Location_1 = [dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1,dspwmr1]
Water_Meter_Location_2 = [dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2,dspwmr2]
inactive_Meters_R1 = [-1,-2]

meters_Per_Row = 12

Nema.Camera_X  = 0
Nema.Camera_Y  = 0
Nema.Camera_Z  = 0

Motor_Pin = [17, 27, 5, 6, 20, 21, 23, 24, 22, 12] # all the motor and enable pins you want initialized
limit_Switches = [4, 26, 19] # all the limit switch pins
ST7735_Pins = [13, 8] # all the st7735 pins to be intialized
progress_Percentage = 0
jog_Speed = 0
jog_Distance = 0

# use the set_GPIO_Out method to set up GIO outputs
Nema.set_GPIO_Out(Motor_Pin)

# use the set_GPIO_In method to set up GIO inputs
Nema.set_GPIO_In(limit_Switches)

# use the set_GPIO_In method to set up GIO inputs
Nema.set_GPIO_Out(ST7735_Pins)

# Set the ith number in the motor_Pin array as the enable pin correspinding to the real world pin
Nema.Enable = Motor_Pin[8] # 8 as 22 is the enable pin

def turn_LED_On():
    GPIO.output(Motor_Pin[9], GPIO.HIGH) # Enable the LED
    print('Led turned on')

def turn_LED_Off():
    GPIO.output(Motor_Pin[9], GPIO.LOW) # Disable the LED
    print('Led turned off')
    
def turn_LCD_On():
    GPIO.output(ST7735_Pins[0], GPIO.HIGH) # Enable the LED
    print('Lcd turned on')

def turn_LCD_Off():
    GPIO.output(ST7735_Pins[0], GPIO.LOW) # Disable the LED
    print('Lcd turned off')

def enable_Motors():
    Nema.enable_Motor()

def disable_Motors():
    Nema.disable_Motor()

def set_Speed(speed):
    jog_Speed = speed

def set_Distance(distance):
    jog_Distance = distance

def stop_program():
    Nema.disable_Motor()

def get_Reading():
    print("Getting Reading")

def home():
    Nema.home_Machine(600,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],Motor_Pin[5],Motor_Pin[4],Motor_Pin[7],Motor_Pin[6],limit_Switches)
    Nema.Camera_X = 0
    Nema.Camera_Y = 0
    Nema.Camera_Z = 0

def increment_Y():
    #Move the Y axis mototors reverse
    speed = jog_Speed
    distance = jog_Distance
    Nema.forward_2(speed,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches[2])
    # update the new location
    Nema.Camera_Y += distance
    print("moved the Y motors " + str(distance) + " millimeters")
    
def decrement_Y():
    #Move the Y axis mototors forward
    speed = jog_Speed
    distance = jog_Distance
    Nema.reverse_2(speed,distance,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches[2])
    # update the new location
    Nema.Camera_Y -= distance
    print("moved the Y motors " + str(distance) + " millimeters")

def increment_X():
    #Move the X axis mototors reverse
    speed = jog_Speed
    distance = jog_Distance
    Nema.reverse(speed,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
    # update the new location
    Nema.Camera_X += distance
    print("moved the Y motors " + str(distance) + " millimeters")

def decrement_X():
    #Move the X axis mototors forward
    speed = jog_Speed
    distance = jog_Distance
    Nema.reverse(speed,distance,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
    # update the new location
    Nema.Camera_X -= distance
    print("moved the Y motors " + str(distance) + " millimeters")

def increment_Z():
    #Move the Z axis mototors forward
    speed = jog_Speed
    distance = jog_Distance
    Nema.forward(speed,distance,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    # update the new location
    Nema.Camera_Z += distance
    print("moved the Y motors " + str(distance) + " millimeters")

def decrement_Z():
    #Move the Z axis mototors reverse
    speed = jog_Speed
    distance = jog_Distance
    Nema.reverse(speed,distance,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    # update the new location
    Nema.Camera_Z -= distance
    print("moved the Z motors " + str(distance) + " millimeters")

def show_Intro():
    print("showing Intro")
    FST7735.Intro()
    
def show_Main_Menu():
    print("showing Main Menu")
    FST7735.Draw_Main_Menu()
    
def show_Home():
    print("shwoing Home")
    FST7735.Home()
    
def show_Run():
    print("showing Run")
    FST7735.Run()
    
def show_IP_Info():
     print("showing IP info")
     FST7735.Check_Info()
     
def start_Program():
    
    # due to calculations Max speed = 600, Min speed = 900 dont use anything slower or faster for better stability
    # The demo will move the reader in an square fashion testing all the features, it will loop ?3 times taking
    # approximately 8-12 hrs to complete
    # add your functions concurrent with mine to complete the automation proccess..i.e camera_driver functions
    Nema.enable_Motor() # re-enable the motors
    
    # Home the test bench
    Nema.home_Machine(600,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],Motor_Pin[5],Motor_Pin[4],Motor_Pin[7],Motor_Pin[6],limit_Switches)
    # Set the camera location as homed
    Nema.Camera_X = 0
    Nema.Camera_Y = 0
    Nema.Camera_Z = 0
    
    # Move Z a camera zoom Length
    Nema.reverse(900,3400,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    # update the new location
    Nema.Camera_Z += 3400 #need way to get camera height
    
    # Move X a camera Length
    for y in range(meters_Per_Row):
        Nema.reverse(900,Water_Meter_Location_1[y],Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
        # update the new location

        Nema.Camera_X += Water_Meter_Location_1[y]

        # use camera methods to get the camera reading so the program can continue, append it to a list
        
    # Move Z back a camera zoom Length
    Nema.forward(900,3400,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    #Nema.enable_Motor() # re-enable the motors
    # update the new location
    Nema.Camera_Z -= 3400
    
    # Move Y the camera to the front row
    Nema.forward_2(600,2600,Motor_Pin[1],Motor_Pin[0],Motor_Pin[3],Motor_Pin[2],limit_Switches[2])
    #Nema.enable_Motor() # re-enable the motors
    # update the new location
    Nema.Camera_Y += 2600
    # Move Z a camera zoom Length
    Nema.reverse(900,3400,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    #Nema.enable_Motor() # re-enable the motors
    # update the new location
    Nema.Camera_Z += 3400

    # use camera methods to get the camera reading so the program can continue, append it to a list

    # Move X back a camera Length
    for y in range(meters_Per_Row):
        Nema.forward(900,Water_Meter_Location_2[y],Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
        #Nema.enable_Motor() # re-enable the motors
        # update the new location
        Nema.Camera_X += Water_Meter_Location_2[y]

    # use camera methods to get the camera reading so the program can continue, append it to a list

    # Move Z back a camera zoom Length
    Nema.forward(900,3400,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    #Nema.enable_Motor() # re-enable the motors
    # update the new location
    Nema.Camera_Z -= 3400
    
    # Move X back to orignal location
    Nema.reverse(900,6500,Motor_Pin[5],Motor_Pin[4],limit_Switches[1])
    #Nema.enable_Motor() # re-enable the motors
    Nema.Camera_X -6500
    
    # Move Z back a camera zoom Length
    Nema.reverse(900,3400,Motor_Pin[7],Motor_Pin[6],limit_Switches[0])
    #Nema.enable_Motor() # re-enable the motors
    # update the new location
    Nema.Camera_Z -= 3400
    
    sleep(0.05)
    
    Nema.disable_Motor()
#GPIO.cleanup()


