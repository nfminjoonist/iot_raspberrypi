import cv2
import spidev
import RPi.GPIO as GPIO
import time

BUZZER = 6
SWITCH = 7

GPIO.setmode(GPIO.BCM)
GPIO.setup(BUZZER, GPIO.OUT)
GPIO.setup(SWITCH, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

pwm = GPIO.PWM(BUZZER, 800)

spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 100000

def analog_read(channel):
    ret = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_out = ((ret[1] & 3) << 8)  + ret[2]
    return adc_out

start_frame = 0

try:
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print('Camera open failed')
        exit()

    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    out = cv2.VideoWriter('output.avi', fourcc, 20, (640, 480))
    status = 0
    totalframe=0
    while True:
        totalframe+=1
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('frame', frame)
        out.write(frame)

        value = GPIO.input(SWITCH)
        if value == 1 or cv2.waitKey(1) == 13:
            break

        reading = analog_read(0)
        start_frame = totalframe - reading / 340 * 1000
        if 0 <= reading and reading < 340 and status is not 1:
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            status = 1
        elif 340 <= reading and reading < 680 and status is not 2:
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            time.sleep(0.2)
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            status = 2
        elif 680 <= reading and status is not 3:
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            time.sleep(0.2)
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            time.sleep(0.2)
            pwm.start(75)
            time.sleep(0.2)
            pwm.stop()
            status=3
        print("Minutes = %f" % (reading*3.3/1024))

    cap.release()
    out.release()
    cv2.destroyAllWindows()
    print(start_frame)
    frameCount = 0
    cap = cv2.VideoCapture('output.avi')

    if not cap.isOpened():
        print('Camera open failed')
        exit()

    while True:
        frameCount = frameCount + 1
        ret, frame = cap.read()
        if not ret:
            break

        if frameCount > start_frame:
            cv2.imshow('frame', frame)

        if cv2.waitKey(1) == 13:
            break
    cap.release()
    cv2.destroyAllWindows()


finally : 
    spi.close()
    GPIO.cleanup()