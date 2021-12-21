import RPi.GPIO as GPIO

LED = [14, 15, 18]
SWITCH = [13, 6, 5]
VALUE = [0, 0, 0]

GPIO.setmode(GPIO.BCM)

for i in LED:
    GPIO.setup(i, GPIO.OUT)
for i in SWITCH:
    GPIO.setup(i, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        for i in range(3):
            VALUE[i] = GPIO.input(SWITCH[i])
            GPIO.output(LED[i], VALUE[i])

finally:
    GPIO.cleanup()
    print('clean up and exit')