import os
import sys

# set the NEMA driver path to the system
current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

import time
import NEMA_Driver as nema
import subprocess
import digitalio # IO funtionality for the GPIO
import board # the borad library for using the board definition
from PIL import Image, ImageDraw, ImageFont # impporting the image drawing library
from adafruit_rgb_display import st7735 # the ST7735 library

# config the CS, DC and Reset pins
cs_pin = digitalio.DigitalInOut(board.CE0)
dc_pin = digitalio.DigitalInOut(board.D25)
reset_pin = digitalio.DigitalInOut(board.D12)

# config Baudrate
BAUDRATE = 24000000
x = "NULL"
# Setup SPI bus using hardware SPI
spi = board.SPI()

# Load a TTF Font
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

# setup the display
disp = st7735.ST7735R(spi, rotation = 90, height = 160, x_offset = 0, y_offset = 0, cs=cs_pin,dc=dc_pin)

# autoscale the image with RGB full color
if disp.rotation % 180 == 90:
    height = disp.width # we swap height and width to rotate it to landscape.
    width = disp.height
else:
    width = disp.width
    height = disp.height


def Intro():
    a = "NULL"
    # Check if the full intro already played.
    c = Intro_Check(a)
    Clear_Screen()
    if (c == "Not_Previously_Run"):
        #******Intro*******
        # Draw Initial Images
        message_1 = ["In","Collaboration", "With!"]
        message_2 = ["FORD", "Meter", "Box's"]
        message_3 = ["Water", "Meter", "Reader!"]
        image = Image.new("RGB", ((width), (height)))
        image = Image.open("Ford_Full.png")
        # scale image
        image = image.resize((160, 128), Image.BICUBIC)
        disp.image(image)

        time.sleep(2)

        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0, (width), (height)), outline = 0, fill = (255, 255, 255))

        # Draw the parts of  message_1
        x = 0
        while (x < 3):
            (font_width, font_height) = font.getsize(message_1[x])
            draw.text((width // 2 - font_width // 2, 30*(x+0.75)),message_3[x],font=font,fill=(0, 0, 0))
            x += 1

        disp.image(image)
        time.sleep(2)

        image = Image.open("Purdue_full.png")
        image = image.resize((160, 128), Image.BICUBIC)
        disp.image(image)
        time.sleep(2)

        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0, (width), (height)), outline = 0, fill = (255, 255, 255))

        # Draw the other message
        (font_width, font_height) = font.getsize("Present!")
        draw.text((width // 2 - font_width // 2, height // 2 - font_height // 2),"Present!",font=font,fill=(0, 0, 0))

        disp.image(image)
        time.sleep(2)

        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0, (width), (height)), outline = 0, fill = (255, 255, 255))

        # Draw the parts of  message_2
        y = 0
        while (y < 3):
            (font_width, font_height) = font.getsize(message_2[y])
            draw.text((width // 2 - font_width // 2, 30*(y+0.75)),message_3[y],font=font,fill=(0, 0, 0))
            y += 1

        disp.image(image)
        time.sleep(2)

        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0, (width), (height)), outline = 0, fill = (255, 255, 255))

        # Draw the parts of  message_3
        z = 0
        while (z < 3):
            (font_width, font_height) = font.getsize(message_3[z])
            draw.text((width // 2 - font_width // 2, 30*(z+0.75)),message_3[z],font=font,fill=(0, 0, 0))
            z += 1

        disp.image(image)
        time.sleep(2)
        with open("Check.bin",'w') as f:
         f.write("Previously_Run")

    else:
        Clear_Screen()
        print("The Full Intro was Previously_Run")
        message_4 = ["Water", "Meter", "Reader!"]
        image = Image.open("Ford_Full.png")
        image = image.resize((160, 128), Image.BICUBIC)
        disp.image(image)
        time.sleep(2)

        draw = ImageDraw.Draw(image)
        draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))

        # Draw the parts of  message_4
        y = 0
        while (y < 3):
            (font_width, font_height) = font.getsize(message_4[y])
            draw.text((width // 2 - font_width // 2, 30*(y+0.75)),message_4[y],font=font,fill=(0, 0, 0))
            y += 1

        disp.image(image)
        time.sleep(2)

def Intro_Check(x):
    try:
        with open("Check.bin",'r') as c:
            x = c.readline()
            if (x != "Previously_Run"):
                print("Was not previously run")
                x = "Not_Previously_Run"
            else:
                x = "Previously_Run"
    except FileNotFoundError:
        with open("Check.bin",'w') as f:
         f.write("Not_Previously_Run")
         x = "Not_Previously_Run"
        print("Creating new file")
    return x

def Clear_Screen():
    image = Image.new("RGB", ((width), (height)))
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (width), (height)), outline = 0, fill = (255, 255, 255))
    disp.image(image)

def Draw_Main_Menu():
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 15)
    Options = ["Home 1", "Run 2","Coord 3", "IP Conn 4"]
    Label = ["M","E","N","U"]
    image = Image.new("RGB", ((width), (height)))
    image = image.resize((160, 128), Image.BICUBIC)
    disp.image(image)
    time.sleep(2)

    #Draw Background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))

    z = 0
    while (z < 4):
        draw.rectangle((5,(10+(30*z)), (115), (30+(30*z))), outline = 2, fill = (255, 130, 40))
        draw.text((6, 30*(z+0.4)),Options[z],font=font,fill=(0, 0, 0))
        z = z+1
    draw.rectangle((155,(9), (120), (120)), outline = 2, fill = (0, 255, 128))

    x = 0
    while (x < 4):
        (font_width, font_height) = font.getsize(Label[x])
        draw.text((57+(width // 2 - font_width // 2), 20*(x+1)),Label[x],font=font,fill=(0, 0, 0))
        x = x+1
    disp.image(image)

def Home():
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    image = Image.new("RGB", ((width), (height)))
    image = image.resize((160, 128), Image.BICUBIC)
    disp.image(image)
    time.sleep(1.25)

    #Draw Background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))


    (font_width, font_height) = font.getsize("Homing..")
    draw.text((width // 2 - font_width // 2, height // 2 - font_height // 2),"Homing..",font=font,fill=(0, 0, 0))

    disp.image(image)

def Run():
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 28)
    image = Image.new("RGB", ((width), (height)))
    image = image.resize((160, 128), Image.BICUBIC)
    disp.image(image)
    time.sleep(1.25)

    #Draw Background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))


    (font_width, font_height) = font.getsize("Running..")
    draw.text((width // 2 - font_width // 2, height // 2 - font_height // 2),"Running..",font=font,fill=(0, 0, 0))

    disp.image(image)

def Check_Info():
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 18)
    # Draw a black filled box to clear the image.
    image = Image.new("RGB", ((width), (height)))
    image = image.resize((160, 128), Image.BICUBIC)
    disp.image(image)
    
    time.sleep(1.25)
    
    #Draw Background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))
    # Shell scripts for system monitoring from here:
    # https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d' ' -f1"
    IP =  subprocess.check_output(cmd, shell=True).decode("utf-8")
    
    #cmd = "cat /sys/class/thermal/thermal_zone0/temp |  awk '{printf \"CPU Temp: %.1f C\", $(NF-0) / 1000}'"  # pylint: disable=line-too-long
    #Temp = subprocess.check_output(cmd, shell=True).decode("utf-8")
    
    (font_width, font_height) = font.getsize("WIFI IP: ")
    draw.text((width // 2 - font_width // 2, (height/2) // 2 - font_height // 2),"WIFI IP:",font=font,fill=(0, 0, 0))
    
    (font_width, font_height) = font.getsize(IP)
    draw.text((width // 2 - font_width // 2, height // 2 - font_height // 2),(" " + IP),font=font,fill=(0, 0, 0))
    
    # Display image.
    disp.image(image)
    
    time.sleep(0.1)
    
def Coordinates(moving):
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
    image = Image.new("RGB", ((width), (height)))
    image = image.resize((160, 128), Image.BICUBIC)
    disp.image(image)
    time.sleep(1.25)

    #Draw Background
    draw = ImageDraw.Draw(image)
    draw.rectangle((0,0, (160), (128)), outline = 0, fill = (255, 255, 255))
    while moving:
        # Draw a black filled box to clear the image.
        draw.rectangle((0, 0, width, height), outline=0, fill=(255,255,255))
        X = nema.get_Coordinate("X")
        Y = nema.get_Coordinate("Y")
        Z = nema.get_Coordinate("Z")
        (font_width, font_height) = font.getsize("X: "+ str(X))
        draw.text((width // 2 - font_width // 2, (height/3) // 2 - font_height // 2),"X: " + str(X),font=font,fill=(0, 0, 0))
        
        (font_width, font_height) = font.getsize("Y: "+ str(Y))
        draw.text((width // 2 - font_width // 2, (height) // 2 - font_height // 2),"Y: " + str(Y),font=font,fill=(0, 0, 0))
        
        (font_width, font_height) = font.getsize("Z: "+ str(Z))
        draw.text((width // 2 - font_width // 2, (height*1.6) // 2 - font_height // 2),"Z: " + str(Z),font=font,fill=(0, 0, 0))

        disp.image(image)
        time.sleep(0.1)
def Configure():
    # config the CS, DC and Reset pins
    cs_pin = digitalio.DigitalInOut(board.CE0)
    dc_pin = digitalio.DigitalInOut(board.D25)
    reset_pin = digitalio.DigitalInOut(board.D12)

    # config Baudrate
    BAUDRATE = 24000000
    x = "NULL"
    # Setup SPI bus using hardware SPI
    spi = board.SPI()

    # Load a TTF Font
    font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 22)

    # setup the display
    disp = st7735.ST7735R(spi, rotation = 90, height = 160, x_offset = 0, y_offset = 0, cs=cs_pin,dc=dc_pin)

    # autoscale the image with RGB full color
    if disp.rotation % 180 == 90:
        height = disp.width # we swap height and width to rotate it to landscape.
        width = disp.height
    else:
        width = disp.width
        height = disp.height
