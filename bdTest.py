#!usr/bin/env python3
from bluedot import BlueDot
import time
from signal import pause
import RPi.GPIO as IO

bd = BlueDot()
bd.square = True

def dot_is_active(pos):
    global p
    BDx = -pos.x
    BDy = pos.y
    DC = BDx * 4.5 + 6.5
    p.ChangeDutyCycle(DC)
    print("X: {}\tY: {}".format(BDx, BDy))

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(18, IO.OUT)
p = IO.PWM(18, 50) # Pin 18  Frequency= 50 Hertz

p.start(6.5)

# p.ChangeDutyCycle()
time.sleep(1)

bd.when_pressed = dot_is_active
bd.when_moved = dot_is_active
pause()


