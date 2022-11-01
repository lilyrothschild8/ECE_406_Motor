# Emmanuel Quaye
# RPI 4B
# This code drives the NEMA 17 motor stepper motor using the TB6600 Driver
# 3.3 -> to the controller "+" input for each: ENA, PUL+, and DIR+
# RASBERRY-PI VERSION
# JUST FOR TEST POURPOSES, IMPORT THIS DRIVER INTO YOUR OWN PYTHON CODE 
from time import sleep
import RPi.GPIO as GPIO
#
YAxisMotor1_PUL = 17  # Drive Pulses for Motor1 (Front Left Y Axis motor)
YAxisMotor1_DIR = 27  # Drive Direction for Motor1 (Front Left Y Axis motor)
#
YAxisMotor2_PUL = 5  # Drive Pulses for Motor1 (Front Left Y Axis motor)
YAxisMotor2_DIR = 6  # Drive Direction for Motor1 (Front Left Y Axis motor)
#
XAxis_Motor_PUL = 20  # Drive Pulses for Motor3 ( Front Left X axis motor)
XAxis_Motor_DIR = 21  # Drive Direction for Motor3 (Side Front X axis Left motor)
#
ZAxis_Motor_PUL = 23  # Drive Pulses for Motor4 (Z axis  motor)
ZAxis_Motor_DIR = 24  # Drive Direction for Motor4 (Z axis Right motor)

X_Stop = 26
Y_Stop = 19
#
Enable = 22  # The enable port
rotation = 0 # rotations completed
dTT =0 # the distance to travel
# NOTE: Leave DIR and ENA disconnected, and the controller WILL drive the motor in Default direction if PUL is applied.
#
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
# GPIO.setmode(GPIO.BOARD) # Do NOT use GPIO.BOARD mode. Here for comparison only.
#
GPIO.setup(YAxisMotor1_PUL, GPIO.OUT)
print('YAxisMotor1_PUL = GPIO 17')
GPIO.setup(YAxisMotor1_DIR, GPIO.OUT)
print('YAxisMotor1_DIR = GPIO 27')
GPIO.setup(YAxisMotor2_PUL, GPIO.OUT)
print('YAxisMotor2_PUL = GPIO 5')
GPIO.setup(YAxisMotor2_DIR, GPIO.OUT)
print('YAxisMotor2_DIR = GPIO 6')                  
GPIO.setup(ZAxis_Motor_PUL, GPIO.OUT)
print('ZAxis_Motor_PUL = GPIO 23')
GPIO.setup(ZAxis_Motor_DIR, GPIO.OUT)
print('ZAxis_Motor_DIR = GPIO 24')
GPIO.setup(XAxis_Motor_PUL, GPIO.OUT)
print('XAxis_Motor_PUL = GPIO 20')
GPIO.setup(XAxis_Motor_DIR, GPIO.OUT)
print('XAxis_Motor_DIR = GPIO 21')
GPIO.setup(X_Stop, GPIO.IN)
print('X_Stop = GPIO 26')
GPIO.setup(Y_Stop, GPIO.IN)
print('Y_Stop = GPIO 19')
GPIO.setup(Enable, GPIO.OUT)
print('Enable = GPIO 22')
#
#
GPIO.output(Enable, GPIO.HIGH) #for enable LOW == Enabled, HIGH = disabled.
print("Enable set to LOW - Controller Enabled")
print('Ready')
#
#
def forward(speed, distance, direction, pull):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(direction, GPIO.HIGH)# set rotation counter clock-wise
    print(distance)
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pull, GPIO.HIGH)
        GPIO.output(pull, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        #print('rotations = ' + str(rotations))
    
    # check if the distance was traveled and stop.
    if (stop_X == 0):
        stopMotor()
        sleep(0.05)
    if (rotations == distance):
        stopMotor() # stops the motor and prints note
        sleep(0.05) # delay 1n milisecond for stability
#
#

def forward_2( speed, distance,direction1, pull1, direction2, pull2):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(direction1, GPIO.HIGH)# set rotation counter clock-wise
    GPIO.output(direction2, GPIO.LOW)# set rotation counter clock-wise
    print(distance)
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pull1, GPIO.HIGH)
        GPIO.output(pull1, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pull2, GPIO.HIGH)
        GPIO.output(pull2, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        #print('rotations = ' + str(rotations))
    
    # check if the distance was traveled and stop.
    if (rotations == distance or stop_X == 0 or stop_Y == 0):
        stopMotor() # stops the motor and prints note
        sleep(1) # delay 1n milisecond for stability


def reverse( speed, distance,direction, pull):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(direction, GPIO.LOW)# set rotation counter clock-wise
    print(distance)
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        GPIO.output(pull, GPIO.HIGH)
        GPIO.output(pull, GPIO.LOW)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        rotations += 1 # increment rotation
        #print('rotations = ' + str(rotations))
    
    # check if the distance was traveled and stop.
    if (rotations == distance or stop_X == 0 or stop_Y == 0):
        stopMotor() # stops the motor and prints note
        sleep(1) # delay 1n milisecond for stability
       
#
#

def reverse_2( speed, distance,direction1, pull1, direction2, pull2):
    speed = (speed/1000000)# This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
    rotations = 0
    GPIO.output(direction1, GPIO.LOW)# set rotation counter clock-wise
    GPIO.output(direction2, GPIO.HIGH)# set rotation counter clock-wise
    print(distance)
    #use simple PWM to drive motor by enabeling disabling PUL pin at speed
    for i in range(distance):
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pull1, GPIO.HIGH)
        GPIO.output(pull2, GPIO.HIGH)
        sleep(speed) # This is actualy a delay between PUL pulses - effectively sets the mtor rotation speed.
        GPIO.output(pull2, GPIO.LOW)
        rotations += 1 # increment rotation
        #print('rotations = ' + str(rotations))
    
    # check if the distance was traveled and stop.
    if (rotations == distance or stop_X == 0 or stop_Y == 0):
        stopMotor() # stops the motor and prints note
        sleep(0.05) # delay 1n milisecond for stability
        
def stopMotor():
    GPIO.output(Enable, GPIO.LOW) # Disable the motor
    print('Enable set to LOW - Controller Disabled')
#
#
# this is the same as a loop function it is here just for test pouposes, comment it out if importing this library...

while True:
    #The Distance per revolution = 200 steps/rev you can look on the mototr driver to verify.
    #we know that the diameter of the 16 tooth belt pulley is 0.200" the radious is then .100"/10 = 0.01"
    #with (200 * 12)/0.01 = 240000 steps/ft or 20000 steps/inch
    #due to calculations Max spped = 10, Min speed = 600 dont use anything slower for better stability
    stop_X = GPIO.input(X_Stop)
    stop_Y = GPIO.input(Y_Stop)
    #forward(1000,1000,ZAxis_Motor_DIR,ZAxis_Motor_PUL)
    reverse(1000,50,XAxis_Motor_DIR,XAxis_Motor_PUL)
    #forward_2(100,200,YAxisMotor1_DIR,YAxisMotor1_PUL,YAxisMotor2_DIR,YAxisMotor2_PUL)
    print(stop_X)
    sleep(0.05)
    #
    
GPIO.cleanup()
