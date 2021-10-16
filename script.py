from machine import Pin
import time

ma1 = Pin(2, Pin.OUT)
ma2 = Pin(3, Pin.OUT)
mb1 = Pin(4, Pin.OUT)
mb2 = Pin(5, Pin.OUT)

turnDelay = (1 / 1000) * 450

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

def moveBackward():
  ma1.value(1)
  ma2.value(0)
  mb1.value(0)
  mb2.value(1)
  time.sleep(1)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

def turnRight():
  ma1.value(0)
  ma2.value(1)
  mb1.value(0)
  mb2.value(1)
  time.sleep(turnDelay)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

turnRight()
