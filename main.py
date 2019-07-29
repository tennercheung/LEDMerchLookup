####### sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel

# >>> userIn = (input()).split(",")
# # 232pu-23,2321-03,23923-23
# >>> print(userIn)
# # ['232pu-23', '2321-03', '23923-23']

# Simple test for NeoPixels on Raspberry Pi
import time
import board
import neopixel

import threading 

# Choose an open pin connected to the Data In of the NeoPixel strip, i.e. board.D18
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
findCounter = 0
nofminutes = 1
LEDtimeout = 60*(nofminutes)
overRide = False
prodDb = ['25012PU-52',\
          '7782-60', \
          '32230-30', \
          '11103-64', \
          '7734-36', \
          '880F-20', \
          '9901-34', \
          '56430-64']

def check_input(userIn):
    findCounter_ = 0
    for i in userIn: 
        for j in prodDb: #checks if each element in the userIn list is in the database
            if i == j: 
                pixels[prodDb.index(i)] = (255, 0, 0) #turn LED red
                pixels.show()
                findCounter_+=1

    return findCounter_
    
def parse_input():
    userIn = (input()).split(",")
#    print("Finding: " + userIn + "\n")

    return userIn

def clear_LEDs():
    pixels.fill((0, 0, 0))
    pixels.show()

print("Welcome\n")

while len(userIn) != -1 :
    clear_LEDs()
    print("Please enter style number:\n")
    userIn = parse_input()
    nofinputs = len(userIn)
    findCounter = check_input(userIn) 
    print(str(findCounter) + "/" + str(nofinputs) + " items found\n")
    findCounter = 0

    userIn = input()
    if userIn == "exit":
        clear_LEDs()
        overRide == True
    elif overRide == False : 
        timer = threading.Timer(LEDtimeout, clear_LEDs) 
        timer.start() 

    overRide == False
    

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


#
##import time
##import board
##import neopixel
#
#import threading
#
#import csv
#
##pixel_pin = board.D18
##
##num_pixels = 8
##
##ORDER = neopixel.GRB
##
##pixels = neopixel.NeoPixel(pixel_pin, num_pixels, brightness=0.2, auto_write=False,
##                           pixel_order=ORDER)
#
#userIn = []
#findCounter = 0
#nofminutes = 1
#LEDtimeout = 60*(nofminutes)
#overRide = False
##prodDb = ['25012PU-52',\
##          '7782-60', \
##          '32230-30', \
##          '11103-64', \
##          '7734-36', \
##          '880F-20', \
##          '9901-34', \
##          '56430-64']
#
#def check_input(userIn):
#
##    with open('sheet.csv') as csv_file:
##        findCounter_ = 0
##        csv_reader = csv.reader(csv_file, delimiter=',')
##        line_count = 1 #reading begins at first line in file
##        for i in userIn: 
###            for j in prodDb: #checks if each element in the userIn list is in the database
##
##            for row in csv_reader:
###                if line_count == 0:
###                    print('Column names are ' + str(",".join(row))) #prints all the columns names in a row
###                    # print(f'Column names are {",".join(row)}')
###                    line_count += 1
##                if line_count > 0:
##                    if i == row[0]:
##                        print("Found: "+str(row[0]) + " at line "+str(line_count-1))
###                        pixels[line_count-1] = (255, 0, 0) #turn LED red
###                        pixels.show()
##                        findCounter_+=1
###                       print('\t'+str(row[0])) #prints every row in column "0"
##                    line_count += 1
##        print('Processed '+str(line_count-1)+' lines.')
#
#    Columns = 2
#    itemsFound = 0
##    line_count = 1 #reading begins at first line in file
#    for i in userIn:
#        line_count = 1
#        with open('sheet.csv') as csv_file:
#            csv_reader = csv.reader(csv_file, delimiter=',')
#            for row in csv_reader: #reads 2D list
#                for shelf in range (0,Columns):
#                    if i == row[shelf]: #shelf1
#                        pixelSlot = (line_count-1)*(shelf+1) - 1
#                        print("Found: "+str(row[shelf]) + " at line "+str(line_count-1)+" of shelf "+str(shelf+1))
##                        print("Found: "+str(row[element]) + " at line "+str(line_count*(element+1)))
##                        pixels[pixelSlot] = (255, 0, 0) #turn LED red
##                        pixels.show()
#                        itemsFound+=1
#                line_count += 1
#                
##    print('Processed '+str(line_count)+' lines.')
##                if i == row[shelf]: #shelf1
##                    print("Found: "+str(row[shelf]) + " at line "+str(line_count))
###                        pixels[line_count-1] = (255, 0, 0) #turn LED red
###                        pixels.show()
##                    itemsFound+=1
###                       print('\t'+str(row[0])) #prints every row in column "0"
##                if i == row[shelf+1]: #shelf2
##                    print("Found: "+str(row[shelf+1]) + " at line "+str(line_count))
###                        pixels[line_count-1] = (255, 0, 0) #turn LED red
###                        pixels.show()
##                    itemsFound+=1
###                       print('\t'+str(row[0])) #prints every row in column "0"
#
#    return itemsFound
#    
#def parse_input():
#    userIn = (input()).split(",")
#
#    return userIn
#
#def clear_LEDs():
##    pixels.fill((0, 0, 0))
##    pixels.show()
#    pass
#
#print("Welcome\n")
#
#while len(userIn) != -1 :
#    clear_LEDs()
#    print("Please enter style number:\n")
#    userIn = parse_input()
#    nofinputs = len(userIn)
#    findCounter = check_input(userIn) 
#    print(str(findCounter) + " of " + str(nofinputs) + " items found\n")
#    findCounter = 0
#
#    userIn = input()
#    if userIn == "exit":
#        clear_LEDs()
#        overRide == True
##    elif overRide == False : 
##        timer = threading.Timer(LEDtimeout, clear_LEDs) 
##        timer.start() 
#
#    overRide == False
