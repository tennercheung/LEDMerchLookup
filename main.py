####### sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
    
import csv

import board
import neopixel

# NeoPixels must be connected to D10, D12, D18 or D21 to work.
pixel_pin = board.D18

# The number of NeoPixels
num_pixels = 8

# The order of the pixel colors - RGB or7 GRB. Some NeoPixels have red and green reversed!
# For RGBW NeoPixels, simply change the ORDER to RGBW or GRBW.
ORDER = neopixel.GRB

pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
                           pixel_order=ORDER)

userIn = []
override = ['exit']

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
    with open('led.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for initrow in csv_reader: 
            ledArray.append(initrow)
    
    for item in userIn:
        for i in range(0, len(array)): #y
            for j in range (0, len(array[i]) ): #x
                if (item == array[i][j]):
                    print("Found: "+str(item)+ " at slot "+ledArray[i][j]+" of column "+str(j))
                    ##pixels[(ledArray[i][j])] = (255, 0, 0) #turn respective LED red
                    ##pixels.show() 
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
    
    if userIn != override:
        nofinputs+= len(userIn)
        findCounter+= check_input(userIn) 
        print(str(findCounter)+" of " +str(nofinputs)+" items found\n")
        
    elif userIn == override:
        print("Clearing LEDs")
        clear_LEDs()
        findCounter = 0
        nofinputs = 0
        
#     if userIn == "exit":
#         clear_LEDs()
#         overRide == True
#     elif overRide == False : 
#         timer = threading.Timer(LEDtimeout, clear_LEDs) 
#         timer.start() 

#     overRide == False
    
# def rainbow_cycle(wait):
#     for j in range(255):
#         for i in range(num_pixels):
#             pixel_index = (i * 256 // num_pixels) + j
#             pixels[i] = wheel(pixel_index & 255)
#         pixels.show()
#         time.sleep(wait)

# while True:
#     # Comment this line out if you have RGBW/GRBW NeoPixels
#     pixels.fill((255, 0, 0))
#     # Uncomment this line if you have RGBW/GRBW NeoPixels
#     # pixels.fill((255, 0, 0, 0))
#     pixels.show()
#     time.sleep(1)

#     # Comment this line out if you have RGBW/GRBW NeoPixels
#     pixels.fill((0, 255, 0))
#     # Uncomment this line if you have RGBW/GRBW NeoPixels
#     # pixels.fill((0, 255, 0, 0))
#     pixels.show()
#     time.sleep(1)

#     # Comment this line out if you have RGBW/GRBW NeoPixels
#     pixels.fill((0, 0, 255))
#     # Uncomment this line if you have RGBW/GRBW NeoPixels
#     # pixels.fill((0, 0, 255, 0))
#     pixels.show()
#     time.sleep(1)

#     rainbow_cycle(0.001)    # rainbow cycle with 1ms delay per step

