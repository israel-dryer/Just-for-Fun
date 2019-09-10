#!/usr/bin/env python3
########################################################################
# Filename    : izzy_stock_watch.py
# Description : Use the LCD display data
# Author      : Israel Dryer
# modification: 9-19-2019
########################################################################
from PCF8574 import PCF8574_GPIO
from Adafruit_LCD1602 import Adafruit_CharLCD
from time import sleep

def loop():
    mcp.output(3,1)     # turn on LCD backlight
    lcd.begin(16,2)     # set number of LCD lines and columns
    msg = ' S&P 500: 2,906.27 | Dow 26,118.02 | Nasdaq 7,874.16 |'
    size = len(msg)+1
    x = 0
    
    while(True):         
        #setup message 
        front = msg[:x]
        back = msg[x:]
        scroller = (back + front)[:16]
        
        #display message
        lcd.setCursor(0,0)  # set cursor position
        lcd.message('Izzy Stock Watch\n')
        lcd.message(scroller)
        sleep(.5)
        if x == size:
            x = 0
        else:
            x +=1
        
def destroy():
    lcd.clear()
    
PCF8574_address = 0x27  # I2C address of the PCF8574 chip.
PCF8574A_address = 0x3F  # I2C address of the PCF8574A chip.
# Create PCF8574 GPIO adapter.
try:
	mcp = PCF8574_GPIO(PCF8574_address)
except:
	try:
		mcp = PCF8574_GPIO(PCF8574A_address)
	except:
		print ('I2C Address Error !')
		exit(1)
# Create LCD, passing in MCP GPIO adapter.
lcd = Adafruit_CharLCD(pin_rs=0, pin_e=2, pins_db=[4,5,6,7], GPIO=mcp)

if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

