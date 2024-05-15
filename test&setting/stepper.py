import ASUS.GPIO as GPI
import time

GPIO.setmode(GPIO.ASUS)

StepPins = [73, 74, 8, 120]  # check order
interval = 0.0009

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

while True:
    pos = input("set position:")
    pos = float(pos) / 360 * 4096
    if pos > 0:
        stepcount = len(seq)
        stepcounter = 0
        stepdir = 1
        stepinitial = 0

    else:
        stepcounter = len(seq) - 1
        stepcount = -1
        stepdir = -1
        stepinitial = stepcounter

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

        time.sleep(interval)
