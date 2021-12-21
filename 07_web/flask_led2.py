from flask import Flask, render_template
import RPi.GPIO as GPIO

LED_PIN = 22

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

#라우팅을 위한 뷰 함수
@app.route("/")
def output():
    return render_template("led.html")

@app.route("/led/<op>")
def led(op):
    print(op)
    if op == "on":
        GPIO.output(LED_PIN, GPIO.HIGH)
        return "LED ON"
    elif op == "off":
        GPIO.output(LED_PIN, GPIO.LOW)
        return "LED OFF"
    else:
        return "ERROR"


# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")

    finally:
        GPIO.cleanup()

