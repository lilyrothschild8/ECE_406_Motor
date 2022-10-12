# Emmanuel Quaye
# RPI 4B
# This code drives the NEMA 17 motor stepper motor using the TB6600 Driver
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION
# JUST FOR TEST POURPOSES, IMPORT THIS DRIVER INTO YOUR OWN PYTHON CODE 
from time import sleep
import RPi.GPIO as GPIO
#
PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction port (High for Controller default / LOW to Force a Direction Change).
Enable = 22  # The enable port
dTT =0; # the distance to travel
rotation = 0; # rotations completed
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
#
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only.
#
GPIO.setup(PUL, GPIO.OUT)
print('PUL = GPIO 17')
GPIO.setup(DIR, GPIO.OUT)
print('DIR = GPIO 27')
GPIO.setup(Enable, GPIO.OUT)
print('ENA = GPIO 22')
#
#
GPIO.output(Enable, GPIO.LOW); #for enable LOW == Enabled, HIGH = disabled.
print("Enable set to LOW - Controller Enabled");
print('Ready')
#
#
def forward(speed, distance, direction, pull):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotation++ # increment rotation
    dTT = distance # distance to travel is set to distance

    GPIO.output(direction, GPIO.HIGH)# set rotation clock-wise
    
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    GPIO.output(pull, GPIO.HIGH)
    GPIO.output(pull, GPIO.LOW)
    sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    
    # check if the distance was traveled and stop.
    if rotation == dTT:
        stopMotor() # stops the motor and prints note
        sleep(1) # delay 1n milisecond for stability
    return
#
#
def reverse(speed, distance,direction, pull):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotation++ # increment rotation
    dTT = distance # distance to travel is set to distance

    GPIO.output(direction, GPIO.LOW)# set rotation counter clock-wise
    
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    GPIO.output(pull, GPIO.HIGH)
    GPIO.output(pull, GPIO.LOW)
    sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    
    # check if the distance was traveled and stop.
    if rotation == dTT:
        stopMotor() # stops the motor and prints note
        sleep(1) # delay 1n milisecond for stability
    return
#
#
def stopMotor():
    GPIO.output(Enable, GPIO.HIGH) # Disable the motor
    print('Enable set to LOW - Controller Disabled')
#
#
# this is the same as a loop function it is here just for test pouposes, comment it out if importing this library...
while True:
    #The Distance per revolution = 200 steps/rev you can look on the mototr driver to verify.
    #we know that the diameter of the 16 tooth belt pulley is 0.200" the radious is then .100"/10 = 0.01"
    #with (200 * 12)/0.01 = 240000 steps/ft or 20000 steps/inch
    #due to calculations Max spped = 10, Min speed = 600 dont use anything slower for better stability
    forward(10,20000,DIR,PUL)

GPIO.cleanup()
