#!/usr/bin/env python3

# Raspberry Pi Servo Motor Control.
# Output PWM signal from GPIO_18 to servo motor
# Caution: Adjust pwMin and pwMax microSecond values to the limits of your servo
# Pulse Width updates every 20 mS
#
# Author: Darrell Harriman harrimand@gmail.com

import RPi.GPIO as IO
from time import sleep

IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(18, IO.OUT)
pwmFreq = 50
p = IO.PWM(18, pwmFreq) # Pin 18  Frequency = 50 Hertz
# (pwMax - pwMin) / pwStepSize = steps_for_full_travel
# (2200  -  600 ) /   20   =  80 steps
# 80 steps at 20 mS per step = 1600 mS = 1.6 Sec.

pwmPeriod = 1 / pwmFreq
pwStepTime = pwmPeriod

pwStepSize= 20 
pwMin = 600      # Minimum Pulse Width in microSeconds.
pwMax = 2200     # Maximum Pulse Width in microSeconds.
pwMid = int(pwMin + (pwMax - pwMin)/2)

pwDCmin = pwMin * 1E-6 / pwmPeriod * 100 # Duty Cycle 0.0 - 100.0 percent
pwDCmax = pwMax * 1E-6 / pwmPeriod * 100 # Duty Cycle 0.0 - 100.0 percent

# Map Function: outVal = (inVal - inMin) / (inMax - inMin) * (outMax - outMin) + outMin
dc = lambda pw: (pw - pwMin) / (pwMax - pwMin) * (pwDCmax - pwDCmin)  + pwDCmin

print("\n\t\tStarting Servo at {:.2f}% duty cycle.\n".format (dc(pwMid)))
p.start(dc(pwMid))

sleep(1)

print("\nServo Started:", end='')
print("\tPulse Width: {:d} uS\tDuty Cycle: {:.2f}%\n".format(pwMid, dc(pwMid)))

try:
    for count in range(0,25): # Sweep Servo 25 times.
        for rd in range(pwMid, pwMin, -pwStepSize):
            p.ChangeDutyCycle(dc(rd))
            sleep(pwStepTime)
        print("At Min:\t\tPulse Width: {:d} uS\tDuty Cycle: {:.2f}%".format(rd, dc(rd)))
        sleep(2)

        for ld in range(pwMin, pwMax, pwStepSize):
            p.ChangeDutyCycle(dc(ld))
            sleep(pwStepTime)
        print("At Max:\t\tPulse Width: {:d} uS\tDuty Cycle: {:.2f}%".format(ld, dc(ld)))
        sleep(2)
        
        for md in range(pwMax, pwMid - pwStepSize, -pwStepSize):
            p.ChangeDutyCycle(dc(md))
            sleep(pwStepTime)
        print("At Mid:\t\tPulse Width: {:d} uS\tDuty Cycle: {:.2f}%".format(md, dc(md)))
    
except KeyboardInterrupt:
    print("Stopped by User\n\n")
finally:
    p.stop()
    IO.cleanup()

