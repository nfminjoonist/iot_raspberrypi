from flask import Flask, render_template

# Flask 객체 생성
# __name__은 파일명
app = Flask(__name__)

#라우팅을 위한 뷰 함수
@app.route("/")
def output():
    return render_template("hello.html",
        title="Hello, Flask!!")

@app.route("/first")
def firstpage():
    return render_template("first.html",
        title="First Page")

@app.route("/second")
def secondpage():
    return render_template("second.html",
        title="Second Page")

# 터미널에서 직접 실행시킨 경우
if __name__=="__main__":
    app.run(host="0.0.0.0")

