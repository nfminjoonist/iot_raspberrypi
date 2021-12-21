import RPi.GPIO as GPIO

LED = 4
SWITCH = 5

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

try:
    while True:
        value = GPIO.input(SWITCH) # 누르지 않은 경우 0, 누른 경우 1
        print(value)
        GPIO.output(LED, value)
finally:
    GPIO.cleanup()
    print('clean up and exit')