import ASUS.GPIO as GPIO
import time

GPIO.setmode(GPIO.ASUS)

StepPins = [73, 74, 8, 120]

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
steptime = 0.0007


def stepper(angle):
    angle = float(angle) / 360 * 4096
    if angle > 0:
        stepcount = len(seq)
        stepcounter = 0
        stepdir = 1
        stepinitial = 0

    else:
        stepcounter = len(seq) - 1
        stepcount = -1
        stepdir = -1
        stepinitial = stepcounter

    for i in range(0, abs(int(angle))):
        for j in range(0, 4):
            pinx = StepPins[j]
            if seq[stepcounter][j] == 1:
                GPIO.output(pinx, True)
            else:
                GPIO.output(pinx, False)

        stepcounter += stepdir
        if stepcounter == stepcount:
            stepcounter = stepinitial

        time.sleep(steptime)

