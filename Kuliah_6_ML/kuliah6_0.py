from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')


if __name__ == '__main__':
    app.run()
