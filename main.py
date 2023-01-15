# Lets blink LEDs conected with your Raspberry Pi Pico over a Ganymed Dev Board by SKANTA (TechCree) 
import machine
from machine import Pin
import utime

led25 =  Pin(25, Pin.OUT) #LED mainboard 
ledgruen =  Pin(10, Pin.OUT) #LED gruen
ledrot =  Pin(6, Pin.OUT) #LED rot

count = 0

if count <= 5:
    #start blink LED mainboard 
    led25.value(1)
    utime.sleep(0.5)
    led25.value(0)
    utime.sleep(1)

    #LED rot
    ledrot.value(1)
    utime.sleep(0.3)
    ledrot.value(0)
    utime.sleep(0.3)
    ledrot.value(1)
    utime.sleep(0.3)
    ledrot.value(0)
    utime.sleep(0.3)
    ledrot.value(1)
    utime.sleep(0.3)
    ledrot.value(0)
    utime.sleep(0.3)

    #Blink LED gruen
    ledgruen.value(1)
    utime.sleep(0.3)
    ledgruen.value(0)
    utime.sleep(0.3)
    ledgruen.value(1)
    utime.sleep(0.3)
    ledgruen.value(0)
    utime.sleep(0.3)
    ledgruen.value(1)
    utime.sleep(0.3)
    ledgruen.value(0)
    utime.sleep(0.3)
    
    count = (count + 1)

if count >= 6:
    led25.value(0)
    ledrot.value(0)
    ledgruen.value(0)
