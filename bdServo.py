
import RPi.GPIO as IO
import time
import os

from bluedot import BlueDot
from signal import pause

dc = lambda DC: (DC - pwMin) / (pwMax - pwMin) * pwDCrange  + pwDCmin

def dot_was_pressed(pos):
    global p
    BDx = -pos.x
    BDy = pos.y
    DC = BDx * 4.5 + 6.5
    p.ChangeDutyCycle(DC)
    print("The Blue Dot was pressed at pos x={} y={}".format(BDx, BDy))

bd = BlueDot()
bd.square = True

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(18, IO.OUT)
p = IO.PWM(18, 50) # Pin 18  Frequency= 50 Hertz
pwStepTime = .02
pwStep = 10

pwMin = 400
pwMax = 2200
pwMid = int(pwMin + (pwMax - pwMin)/2)
pwDCmin = pwMin / 200
pwDCmax = pwMax / 200
pwDCrange = pwDCmax - pwDCmin

print("Starting Servo at {}% duty cycle.".format (dc(pwMid)))
p.start(dc(pwMid))

p.ChangeDutyCycle(dc(pwMid))
time.sleep(1)
os.system("espeak -ven-us+f4 -s150 \"Commence Sweep!\" 2>/dev/null")

bd.when_pressed = dot_was_pressed
pause()

