# Import neccesary Libraries
import time
import digitalio # IO funtionality for the GPIO
import board # the borad library for using the board definition
from Ford_ST7735 import Intro, Clear_Screen, Draw_Main_Menu, Home, Camera_View, Check_Info, Run

# Compute The introdution.
Intro()
Draw_Main_Menu()
#Home()
#Camera_View()
#Run()
#Check_Info()