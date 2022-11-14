# Created by Emmanuel Quaye.
# modified by [NAME1, NAME2, NAME3...]
# This code drives the NEMA 17 motor stepper motor using the TB6600 Driver
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION
# JUST FOR TEST POURPOSES, IMPORT THIS DRIVER INTO YOUR OWN PYTHON CODE
from time import sleep

HOME = False

Camera_X = 0
Camera_Y = 0
Camera_Z = 0

def set_Up_Board():
    # setup the board
    #GPIO.setwarnings(False)
    #GPIO.setmode(GPIO.BCM)
    print("PYTHON GPIO Setup")

def set_GPIO_Out(pin_array):
    for x in pin_array:
        #GPIO.setup(x, GPIO.OUT)
        print(("Pin") + (" ") + str(x) + (" ") + ("set as GPIO.OUT"))

def set_GPIO_In(pin_array):
    for x in pin_array:
        #GPIO.setup(x, GPIO.IN)
        print(("Pin") + (" ") + str(x) + (" ") + ("set as GPIO.IN"))

def forward(speed, distance, dir, pul,stop_pin_Array):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir, GPIO.HIGH)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul, GPIO.HIGH)
        #GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        #print('rotations = ' + str(rotations))
        for x in stop_pin_Array:
            if(HOME):
                print("Homing Enabled")
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    enable_Motor()
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)
            else:
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)


def forward_2( speed, distance,dir1, pul1, dir2, pul2, stop_pin_Array):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir1, GPIO.HIGH)# set rotation counter clock-wise
    #GPIO.output(dir2, GPIO.LOW)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul1, GPIO.HIGH)
        #GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        #GPIO.output(pul2, GPIO.HIGH)
        #GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        for x in stop_pin_Array:
            if(HOME):
                print("Homing Enabled")
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    enable_Motor()
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)
            else:
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)

def reverse( speed, distance,dir, pul, stop_pin_Array):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir, GPIO.LOW)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul, GPIO.HIGH)
        #GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        for x in stop_pin_Array:
            if(HOME):
                print("Homing Enabled")
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    enable_Motor()
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)
            else:
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)

def reverse_2( speed, distance,dir1, pul1, dir2, pul2, stop_pin_Array):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir1, GPIO.LOW)# set rotation counter clock-wise
    #GPIO.output(dir2, GPIO.HIGH)# set rotation counter clock-wise
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        #GPIO.output(pul1, GPIO.HIGH)
        #GPIO.output(pul2, GPIO.HIGH)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        #GPIO.output(pul2, GPIO.LOW)
        rotations += 1 # increment rotation
        for x in stop_pin_Array:
            if(HOME):
                print("Homing Enabled")
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    enable_Motor()
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)
            else:
                if(x == 0):
                    stop_Motor()
                    print(("limit switch") + str(x) + (" Hit"))
                    return(("False"))
                if(rotations == distance):
                    stop_Motor()
                    print(("Rotated") + (" ") + str(distance))
                    return(rotations)

# Begin debug section
# The debug section of the methods, these ignore the saftey of the limit switches

def forward_I(speed, distance, dir, pul):
    #this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir, GPIO.HIGH)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul, GPIO.HIGH)
        #GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(rotations == distance):
            stop_Motor()
            print(("Rotated") + (" ") + str(distance))
            return(rotations)


def forward_2_I( speed, distance, dir1, pul1, dir2, pul2):
    # this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir1, GPIO.HIGH)# set rotation counter clock-wise
    #GPIO.output(dir2, GPIO.LOW)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul1, GPIO.HIGH)
        #GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        #GPIO.output(pul2, GPIO.HIGH)
        #GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(rotations == distance):
            stop_Motor()
            print(("Rotated") + (" ") + str(distance))
            return(rotations)

def reverse_I(speed, distance, dir, pul):
    #this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir, GPIO.LOW)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul, GPIO.HIGH)
        #GPIO.output(pul, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(rotations == distance):
            stop_Motor()
            print(("Rotated") + (" ") + str(distance))
            return(rotations)

def reverse_2_I( speed, distance, dir1, pul1, dir2, pul2):
    # this method ignores the stop pin status
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    #GPIO.output(dir1, GPIO.LOW)# set rotation counter clock-wise
    #GPIO.output(dir2, GPIO.HIGH)# set rotation counter clock-wise
    # use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        #GPIO.output(pul1, GPIO.HIGH)
        #GPIO.output(pul1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        #GPIO.output(pul2, GPIO.HIGH)
        #GPIO.output(pul2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        if(rotations == distance):
            stop_Motor()
            print(("Rotated") + (" ") + str(distance))
            return(rotations)

# End debug section

def home_Machine(speed, dir1, dir2, dir3, dir4, pul1, pul2, pul3, pul4, stop_pin_Array):
    HOME = True
    print("Homing")
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    # move Z motor home first
    forward(speed,100000,dir1,pul1,stop_pin_Array)
    reverse_I(1000,20,dir1,pul1)

    # move X motor home third
    forward(speed,100000,dir4,pul4,stop_pin_Array)
    reverse_I(1000,20,dir4,pul4)
    
    # move Y motors home second
    forward_2(speed,100000,dir2,pul2,dir3,pul3,stop_pin_Array)
    reverse_2_I(1000,20,dir2,pul2,dir3,pul3)

    HOME = False
    print("Finished Homing")

def stop_Motor():
    #GPIO.output(Enable, GPIO.LOW) # Disable the motors
    print('Enable set to LOW - Motors Disabled')

def enable_Motor():
    #GPIO.output(Enable, GPIO.HIGH) # Enable the motors
    print('Enable set to LOW - Motors Disabled')
