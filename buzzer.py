#by StSkanta (TechCree) 838375
import machine
from machine import Pin
import utime
import time
import os

buzzer = Pin(16, Pin.OUT)

buzzer.value(1)
utime.sleep(0.2)
buzzer.value(0)
utime.sleep(1)
