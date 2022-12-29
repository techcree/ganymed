#programm for Ganymed Dev Board by StSkanta (TechCree) 838375

import machine
from machine import Pin
import utime
import clock
import os
import time
from breakout_bme280 import BreakoutBME280
from pimoroni_i2c import PimoroniI2C
from machine import Pin, PWM
from machine import ADC
from utime import sleep

#PINS_BREAKOUT_GARDEN = {"sda": 0, "scl": 1}
PINS_PICO_EXPLORER = {"sda": 0, "scl": 1}

i2c = PimoroniI2C(**PINS_BREAKOUT_GARDEN)
bme = BreakoutBME280(i2c)

#Buzzer
buzzer = Pin(16, Pin.OUT)

buzzer.value(1)
utime.sleep(0.2)
buzzer.value(0)
utime.sleep(1)

#LEDs
ledmain =  Pin(25, Pin.OUT) #mainboard
ledone =  Pin(6, Pin.OUT) #LED 1
ledtwo =  Pin(10, Pin.OUT) #LED 2


ledmain.value(1)
utime.sleep(1)
ledmain.value(0)

ledone.value(1)
utime.sleep(1)
ledone.value(0)

ledtwo.value(1)
utime.sleep(1)
ledone.value(0)

#Sensor BME280
reading = bme.read()
print(reading)
#time.sleep(1.0)

#Servo
#step to 90 Grad
MID190 = 400000   #-10
MID180 = 500000   #-5
MID170 = 600000   #0
MID160 = 700000   #2
MID150 = 800000   #4
MID140 = 900000   #6
MID130 = 1000000  #8
MID120 = 1100000  #10
MID110 = 1200000  #12
MID100 = 1300000  #14
MID90 = 1400000   #16
MID80 = 1500000   #18
MID70 = 1600000   #20
MID60 = 1700000   #22
MID50 = 1800000   #24
MID40 = 1900000   #26
MID30 = 2000000   #28
MID20 = 2100000   #30
MID10 = 2200000   #32

#0 Grad
MIN = 300000 #0

##ranges
# 90 Grad
MID = 1200000

#180 Grad
MAXA = 2200000

#maximum
MAX = 2600000

##trimm
pwm = PWM(Pin(15))
pwm.freq(50)


# Initialisierung des ADC4
sensor = ADC(4)
conversion_factor = 3.3 / (65535)

# Wiederholung einleiten (Schleife)
while True:
    #input Grad
    #grad = int(input("Wie viel Grad? "))
    #print(grad)
    
    # Temparatur-Sensor als Dezimalzahl lesen
    value_a = sensor.read_u16()
    # Dezimalzahl in eine reele Zahl umrechnen
    spannung = value_a * conversion_factor
    # Spannung in Temperatur umrechnen
    temperatur = 27 - (spannung - 0.706) / 0.001721
    grad = (temperatur)
    print(grad)
    
    if grad >= 34 and grad <= 36:
        pwm.duty_ns(MID10)

    if grad >= 32 and grad <= 34:   
        pwm.duty_ns(MID20)
    
    if grad >= 30 and grad <= 32:
        pwm.duty_ns(MID30)

    if grad >= 28 and grad <= 30:
        pwm.duty_ns(MID40)

    if grad >= 26 and grad <= 28:
        pwm.duty_ns(MID50)

    if grad >= 24 and grad <= 6:
        pwm.duty_ns(MID60)

    if grad >= 22 and grad <= 24:
        pwm.duty_ns(MID70)

    if grad >= 20 and grad <= 22:
        pwm.duty_ns(MID80)

    if grad >= 18 and grad <= 16:
        pwm.duty_ns(MID90)

    if grad >= 16 and grad <= 18:
        pwm.duty_ns(MID100)

    if grad >= 14 and grad <= 16:
        pwm.duty_ns(MID110)

    if grad >= 12 and grad <= 14:
        pwm.duty_ns(MID120)

    if grad >= 10 and grad <= 12:
        pwm.duty_ns(MID130)

    if grad >= 8 and grad <= 10:
        pwm.duty_ns(MID140)
    
    if grad >= 6 and grad <= 8:
        pwm.duty_ns(MID150)

    if grad >= 4 and grad <= 6:
        pwm.duty_ns(MID160)

    if grad >= 2 and grad <= 4:    
        pwm.duty_ns(MID170)

    #if grad >= "-5"and grad <= 2:
    #    pwm.duty_ns(MID180)

    #if grad >= "-10"and grad <= "-5":
    #    pwm.duty_ns(MID190)
    
        #pwm.duty_ns(MAXA)
    
    #if grad >= 200:
     #   print("Gradangabe nicht umsetbar!")
    
    
    if grad == 0:
        pwm.duty_ns(MIN)
        
    time.sleep(10)
    pwm.duty_ns(MIN)
    time.sleep(1)
