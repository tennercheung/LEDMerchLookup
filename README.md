# LEDMerchLookup

## Bill of Materials (BOM)
1. Raspberry Pi
2. 8GB+ Class 10 Micro SD card
3. USB Wifi dongle (for Pi's before model 3)
4. 5V PSU rated for 2.5A + 0.06A x number of RGB lights used + 1.5A for safety or any future plans
5. 1000uF 10V+ capacitor
6. Row of 20 female header pins
7. Protohat or 20×10 double sided perfboard
8. Two slot screw terminals x2
9. Three slot screw terminal 
10. Micro USB cable
11. 18-20 AWG Wire
12. 220-470 Ohm 0.25W+ resistor 

## Software 

* Flash SD card with newest Raspbian IMG
* Do general setup: wifi, password change from default, etc
* Install adafruit circuitpython for the RGB LEDs with:
*sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel*
* Disable login
* Enable VNC Server (note the IP addr for client connecting)
* Running boot.py at boot https://bit.ly/2Zp2eAo

## Hardware

* Capacitor goes parallel with the PSU, Micro USB cable and the RGB LEDs' power lines
* GND (third pin from the top row) connects to the ground of the parallel connections
* Resistor goes between GPIO8 (sixth pin from the top row) and the RGB LEDs' DATAIN cable
