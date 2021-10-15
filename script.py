from machine import Pin
import time

ma1 = Pin(2, Pin.OUT)
ma2 = Pin(3, Pin.OUT)
mb1 = Pin(4, Pin.OUT)
mb2 = Pin(5, Pin.OUT)

def moveForward():
  ma1.value(0)
  ma2.value(1)
  mb1.value(1)
  mb2.value(0)
  time.sleep(1)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

moveForward()
