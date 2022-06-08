####### sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
    
import csv

import board
import neopixel

import os
# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 600

# The order of the pixel colors - RGB or7 GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

userIn = []
override = ['clear']
shutoff = ['off']
reboot = ['restart']
reset = ['reset']
blank = ['']

findCounter = 0
nofinputs = 0

def check_input(userIn):
    
    itemsFound = 0
    array = []
    ledArray = []
    with open('sheet.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for initrow in csv_reader: 
            array.append(initrow)
    with open('LED.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for initrow in csv_reader: 
            ledArray.append(initrow)
    
    for item in userIn:
        for i in range(0, len(array)): #y
            for j in range (0, len(array[i]) ): #x
                if (item == array[i][j]):
                    print( "Found: "+str(item)+ " @LED "+str( int(ledArray[i][j]) ) )
                    pixels[(int(ledArray[i][j])-1)] = (255, 0, 0) #turn respective LED red
                    #pixels[149]=(255,0,0)
                    pixels.show()
                    itemsFound+=1
                
    return itemsFound
    
def parse_input():
    userIn = (input("Please enter style numbers:\n")).split(",")

    return userIn

def clear_LEDs():
    pixels.fill((0, 0, 0))
    pixels.show()

clear_LEDs()
print("Welcome\n")

while len(userIn) != -1 :
    
    userIn = parse_input()
    
    if (userIn != override and userIn != shutoff and userIn != reboot and userIn != blank):
        nofinputs+= len(userIn)
        findCounter+= check_input(userIn) 
        print(str(findCounter)+" of " +str(nofinputs)+" items found\n")
        
    elif userIn == override:
        print("Clearing LEDs")
        clear_LEDs()
        findCounter = 0
        nofinputs = 0
        
    elif userIn == shutoff:
        print("Clearing LEDs")
        clear_LEDs()
        os.system("sudo shutdown -h now")

    elif userIn == reboot:
        print("Clearing LEDs")
        clear_LEDs()
        print("Updating..")
        os.system("git pull;sudo python3 main.py")
        
    elif userIn == blank:
        print("Please try again")
        
    elif userIn == reset:
        print("Clearing LEDs")
        clear_LEDs()
        print("Resetting..")
        os.system("sudo reboot")


#     if userIn == "exit":
#         clear_LEDs()
#         overRide == True
#     elif overRide == False : 
#         timer = threading.Timer(LEDtimeout, clear_LEDs) 
#         timer.start() 

#     overRide == False 
    

