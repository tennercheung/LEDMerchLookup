#from gpiozero import Button
#import os
#Button(21).wait_for_press()

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(21,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)

if GPIO.input(21) == GPIO.HIGH:
    os.system("sudo poweroff")