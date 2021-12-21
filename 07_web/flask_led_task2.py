from flask import Flask, render_template
import RPi.GPIO as GPIO

RED = 13
BLUE = 19
GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

app = Flask(__name__)

@app.route("/")
def hello_world():
  return render_template("led2.html")

@app.route("/led/<color>/<status>")
def led(color, status):
    if color == "red":
        if status == "on":
            GPIO.output(RED, GPIO.HIGH)
            return "RED LED ON"
        elif status == "off":
            GPIO.output(RED, GPIO.LOW)
            return "RED LED OFF"

    elif color == "blue":
        if status == "on":
            GPIO.output(BLUE, GPIO.HIGH)
            return "BLUE LED ON"
        elif status == "off":
            GPIO.output(BLUE, GPIO.LOW)
            return "BLUE LED OFF"

# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()
