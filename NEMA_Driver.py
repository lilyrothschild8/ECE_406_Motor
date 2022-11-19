# Created by Emmanuel Quaye.
# modified by [NAME1, NAME2, NAME3...]
# This code drives the NEMA 17 motor stepper motor using the TB6600 Driver
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION
# JUST FOR TEST POURPOSES, IMPORT THIS DRIVER INTO YOUR OWN PYTHON CODE
from time import sleep
import RPi.GPIO as GPIO

HOME = False

Enable = 22

small_Amount = 20
medium_Amount = 100
large_Amount = 200

Camera_X = 0
Camera_Y = 0
Camera_Z = 0

def set_Up_Board():
    # setup the board
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    print("PYTHON GPIO Setup")

def set_GPIO_Out(pin_array):
    for x in pin_array:
        GPIO.setup(x, GPIO.OUT)
        print(("Pin") + (" ") + str(x) + (" ") + ("set as GPIO.OUT"))

def set_GPIO_In(pin_array):
    for x in pin_array:
        GPIO.setup(x, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        print(("Pin") + (" ") + str(x) + (" ") + ("set as GPIO.IN"))

def forward(speed, distance, dir, pul,stop_pin):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir, GPIO.HIGH)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul, GPIO.HIGH)
        GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(GPIO.input(stop_pin) == 0):
            print(("limit switch") + str(stop_pin) + (" Hit = ") + str(GPIO.input(stop_pin)))
            return(("False"))
    if(rotations == distance):
        sleep(1)
        return(rotations)


def forward_2( speed, distance,dir1, pul1, dir2, pul2, stop_pin):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir1, GPIO.HIGH)# set rotation counter clock-wise
    GPIO.output(dir2, GPIO.HIGH)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul1, GPIO.HIGH)
        GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pul2, GPIO.HIGH)
        GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(GPIO.input(stop_pin) == 0):
            print(("limit switch") + str(stop_pin) + (" Hit = ") + str(GPIO.input(stop_pin)))
            return(("False"))
    if(rotations == distance):
        sleep(1)
        return(rotations)

def reverse( speed, distance,dir, pul, stop_pin):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir, GPIO.LOW)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul, GPIO.HIGH)
        GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(GPIO.input(stop_pin) == 0):
            print(("limit switch") + str(stop_pin) + (" Hit = ") + str(GPIO.input(stop_pin)))
            return(("False"))
    if(rotations == distance):
        sleep(1)
        return(rotations)

def reverse_2( speed, distance,dir1, pul1, dir2, pul2, stop_pin):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir1, GPIO.LOW)# set rotation counter clock-wise
    GPIO.output(dir2, GPIO.LOW)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul1, GPIO.HIGH)
        GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pul2, GPIO.HIGH)
        GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(GPIO.input(stop_pin) == 0):
            print(("limit switch") + str(stop_pin) + (" Hit = ") + str(GPIO.input(stop_pin)))
            return(("False"))
    if(rotations == distance):
        sleep(1)
    return(rotations)

# Begin debug section
# The debug section of the methods, these ignore the saftey of the limit switches

def forward_I(speed, distance, dir, pul):
    #this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir, GPIO.HIGH)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul, GPIO.HIGH)
        GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
    if(rotations == distance):
        sleep(1)
    return(rotations)


def forward_2_I( speed, distance, dir1, pul1, dir2, pul2):
    # this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir1, GPIO.HIGH)# set rotation counter clock-wise
    GPIO.output(dir2, GPIO.HIGH)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul1, GPIO.HIGH)
        GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pul2, GPIO.HIGH)
        GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
    if(rotations == distance):
        sleep(1)
    return(rotations)

def reverse_I(speed, distance, dir, pul):
    #this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir, GPIO.LOW)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul, GPIO.HIGH)
        GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
    if(rotations == distance):
        sleep(1)
    return(rotations)

def reverse_2_I( speed, distance, dir1, pul1, dir2, pul2):
    # this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(dir1, GPIO.LOW)# set rotation counter clock-wise
    GPIO.output(dir2, GPIO.LOW)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pul1, GPIO.HIGH)
        GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pul2, GPIO.HIGH)
        GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
    if(rotations == distance):
        sleep(1)
    return(rotations)

# End debug section

def home_Machine(speed, dir1, pul1, dir2, pul2, dir3, pul3, dir4, pul4, stop_pin_Array):
    HOME = True
    print("Homing")
    # move Z motor home first
    #forward(speed,100000,dir1,pul1,stop_pin) # Use this when limit_Switch is installed
    forward(speed,3500,dir4,pul4,stop_pin_Array[0]) # Use this when limit_Switch is not installed
    reverse_I(900,30,dir4,pul4)

    # move X motor home second
    #forward(speed,100000,dir4,pul4,stop_pin)# Use this when limit_Switch is installed
    forward(speed,6500,dir3,pul3,stop_pin_Array[1]) # Use this when limit_Switch is not installed
    reverse_I(900,30,dir3,pul3)

    # move Y motors home third
    #forward_2(speed,100000,dir2,pul2,dir3,pul3,stop_pin)# Use this when limit_Switch is installed
    reverse_2(600,2600,dir1,pul1,dir2,pul2,stop_pin_Array[2])# Use this when limit_Switch is not installed
    forward_2_I(900,30,dir1,pul1,dir2,pul2)

    HOME = False
    print("Finished Homing")

def enable_Motor():
    GPIO.output(Enable, GPIO.LOW) # Disable the motors
    print('Enable set to LOW - Motors enabled')

def disable_Motor():
    GPIO.output(Enable, GPIO.HIGH) # Enable the motors
    print('Enable set to HIGH - Motors disabled')
