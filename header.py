from machine import Pin
import time

ma1 = Pin(2, Pin.OUT)
ma2 = Pin(3, Pin.OUT)
mb1 = Pin(4, Pin.OUT)
mb2 = Pin(5, Pin.OUT)

leftDelay = (1 / 1000) * 470
rightDelay = (1 / 1000) * 440

def move_forward_on():
  ma1.value(0)
  ma2.value(1)
  mb1.value(1)
  mb2.value(0)

def move_forward():
  ma1.value(0)
  ma2.value(1)
  mb1.value(1)
  mb2.value(0)
  time.sleep(1)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

def move_backward_on():
  ma1.value(1)
  ma2.value(0)
  mb1.value(0)
  mb2.value(1)  

def move_backward():
  ma1.value(1)
  ma2.value(0)
  mb1.value(0)
  mb2.value(1)
  time.sleep(1)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

def turn_left_on():
  ma1.value(1)
  ma2.value(0)
  mb1.value(1)
  mb2.value(0)

def turn_left():
  ma1.value(1)
  ma2.value(0)
  mb1.value(1)
  mb2.value(0)
  time.sleep(leftDelay)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

def turn_right_on():
  ma1.value(0)
  ma2.value(1)
  mb1.value(0)
  mb2.value(1)

def turn_right():
  ma1.value(0)
  ma2.value(1)
  mb1.value(0)
  mb2.value(1)
  time.sleep(rightDelay)
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)

def all_off():
  ma1.value(0)
  ma2.value(0)
  mb1.value(0)
  mb2.value(0)
