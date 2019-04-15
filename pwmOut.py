import RPi.GPIO as IO
import time
import os
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
dc = lambda DC: (DC - pwMin) / (pwMax - pwMin) * pwDCrange  + pwDCmin

print("Starting Servo at {}% duty cycle.".format (dc(pwMid)))
p.start(dc(pwMid))

p.ChangeDutyCycle(dc(pwMid))
time.sleep(1)
os.system("espeak -ven-us+f4 -s150 \"Commence Sweep!\" 2>/dev/null")

print("\nServo Started:", end='')
print("\tPulse Width: {} uS\tDuty Cycle: {}".format(pwMid, dc(pwMid)))

try:
    for rd in range(pwMid, pwMin, -pwStep):
        p.ChangeDutyCycle(dc(rd))
#        print("Duty Cycle: {}".format(dc(rd)))
        time.sleep(pwStepTime)
    print("At Min:\t\tPulse Width: {} uS\tDuty Cycle: {}".format(rd, dc(rd)))

    for ld in range(pwMin, pwMax, pwStep):
        p.ChangeDutyCycle(dc(ld))
#        print("Duty Cycle: {}".format(dc(ld)))
        time.sleep(pwStepTime)
    print("At Max:\t\tPulse Width: {} uS\tDuty Cycle: {}".format(ld, dc(ld)))

    for md in range(pwMax, pwMid, -pwStep):
        p.ChangeDutyCycle(dc(md))
#        print("Duty Cycle: {}".format(dc(md)))
        time.sleep(pwStepTime)
    print("At Mid:\t\tPulse Width: {} uS\tDuty Cycle: {}".format(md, dc(md)))

except KeyboardInterrupt:
    print("Stopped by User\n\n")
finally:
    os.system("espeak -ven-us+f2 -s150 \"Stopping Now!\" 2>/dev/null")
    p.stop()
    IO.cleanup()

'''
for td in range(pwMid, pwMin, -100):
    print('Duty Cycle: {} '.format(dc(td)))
for td in range(pwMin, pwMax, 100):
    print('Duty Cycle: {} '.format(dc(td)))
for td in range(pwMax, pwMin, -100):
    print('Duty Cycle: {}'.format(dc(td)))
for td in range(pwMin, pwMid, 100):
    print('Duty Cycle: {}'.format(dc(td)))
'''
'''
p.ChangeDutyCycle(dc(1250)
time.sleep(.5)
p.ChangeDutyCycle(dc(1750)
time.sleep(.5)
p.ChangeDutyCycle(dc(1250)
'''
