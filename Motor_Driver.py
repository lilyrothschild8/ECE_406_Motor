# Emmanuel Quaye
# RPI 4B
# This code drive the NEMA 17 motor stepper motor using the TB6600 Driver
#
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
from time import sleep
import RPi.GPIO as GPIO
#
PUL = 17  # Stepper Drive Pulses
DIR = 27  # Controller Direction port (High for Controller default / LOW to Force a Direction Change).
Enable = 22  # The enable port
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
# 
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only. 
#
GPIO.setup(PUL, GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(Enable, GPIO.OUT)
#
print('PUL = GPIO 17 - RPi 3B-Pin #11')
print('DIR = GPIO 27 - RPi 3B-Pin #13')
print('ENA = GPIO 22 - RPi 3B-Pin #15')
#
print('Ready')
#
#
def forward(speed, distance):
    rotation = 0
    speed = (speed * 0.0000001) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    print('Speed set to ' + str(speed))
    GPIO.output(Enable, GPIO.HIGH)
    print('Enable set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.LOW)
    print('Moving Foward at ' + str(speed) + 'F/s')
    print('Distance Fwd set to ' + str(distance) + 'F')
    print('Controller PUL being driven.')
    #
    for x in range(distance): 
        GPIO.output(PUL, GPIO.HIGH)
        sleep(speed)
        GPIO.output(PUL, GPIO.LOW)
        sleep(speed)
        rotation = (rotation + 1)
    GPIO.output(Enable, GPIO.LOW)
    #
    print('Enable set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    print('running clock-wise')
    
    return rotation
#
#
def reverse(speed, distance):
    rotation = 0
    speed = (speed * 0.0000001) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    print('Speed set to ' + str(speed))
    GPIO.output(Enable, GPIO.HIGH)
    print('Enable set to HIGH - Controller Enabled')
    #
    sleep(.5) # pause due to a possible change direction
    GPIO.output(DIR, GPIO.HIGH)
    print('Moving Backward at ' + str(speed) + 'F/s')
    print('Distance Bwd set to ' + str(distance) + 'F')
    print('Controller PUL being driven.')
    #
    for y in range(distance):
        GPIO.output(PUL, GPIO.HIGH)
        sleep(speed)
        GPIO.output(PUL, GPIO.LOW)
        sleep(speed)
        rotation = (rotation + 1)
    GPIO.output(Enable, GPIO.LOW)
    #
    print('Enable set to LOW - Controller Disabled')
    sleep(.5) # pause for possible change direction
    print('running in counter clock-wise')
    return rotation

def stopMotor():
    GPIO.output(Enable, GPIO.LOW)
    print('Enable set to LOW - Controller Enabled')

GPIO.cleanup()
