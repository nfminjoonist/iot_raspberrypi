from flask import Flask
import RPi.GPIO as GPIO

RED = 22
BLUE = 27

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

#라우팅을 위한 뷰 함수
@app.route("/")
def output():
    return '''
    <p>Hello, Flask</p>
    <br>
    <a href="/led/red/on">RED LED ON</a>
    <a href="/led/red/off">RED LED OFF</a>
    <br>
    <a href="/led/blue/on">BLUE LED ON</a>
    <a href="/led/blue/off">BLUE LED OFF</a>
    '''

@app.route("/led/<color>/<status>")
def led(color, status):
    if color == "red":
        if status == "on":
            GPIO.output(RED, GPIO.HIGH)
            return '''
            <p>RED LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif status == "off":
            GPIO.output(RED, GPIO.LOW)
            return '''
            <p>RED LED OFF</p>
            <a href="/">Go Home</a>
        '''
    elif color == "blue":
        if status == "on":
            GPIO.output(BLUE, GPIO.HIGH)
            return '''
            <p>BLUE LED ON</p>
            <a href="/">Go Home</a>
            '''
        elif status == "off":
            GPIO.output(BLUE, GPIO.LOW)
            return '''
            <p>BLUE LED OFF</p>
            <a href="/">Go Home</a>
        '''


# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    try:
        app.run(host="0.0.0.0")
    finally:
        GPIO.cleanup()

