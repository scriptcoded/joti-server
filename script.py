from machine import Pin
import time

m1A = Pin(2, Pin.OUT)
m1B = Pin(3, Pin.OUT)
m2A = Pin(4, Pin.OUT)
m2B = Pin(5, Pin.OUT)

m1A.value(0)
m1B.value(1)
m2A.value(1)
m2B.value(0)

time.sleep(1)

m1A.value(0)
m1B.value(0)
m2A.value(0)
m2B.value(0)
