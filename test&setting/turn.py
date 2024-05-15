# stepper mortor for long time test
# set pos proper value for your test

import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.ASUS)

StepPins = [73, 74, 8, 120]
interval = 0.0009
pos = 2950

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

seq = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
]

stepcount = len(seq)
stepcounter = 0
stepdir = 1
stepinitial = 0
cnt = 1

while True:
    if cnt > 0:
        stepcount = len(seq)
        stepcounter = 0
        stepdir = 1
        stepinitial = 0
        cnt = 0
        pos = 2930
        pos = float(pos) / 360 * 4096

    else:
        stepcounter = len(seq) - 1
        stepcount = -1
        stepdir = -1
        stepinitial = stepcounter
        cnt = 1
        pos = -2950
        pos = float(pos) / 360 * 4096

    for i in range(0, abs(int(pos))):
        for j in range(0, 4):
            pinx = StepPins[j]
            if seq[stepcounter][j] == 1:
                GPIO.output(pinx, True)
            else:
                GPIO.output(pinx, False)

        stepcounter += stepdir
        if stepcounter == stepcount:
            stepcounter = stepinitial

        time.sleep()
