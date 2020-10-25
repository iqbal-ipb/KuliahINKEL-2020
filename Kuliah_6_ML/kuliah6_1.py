from flask import Flask, render_template, request, redirect, Response
# ----untuk database-------------
from flask_mysqldb import MySQL
# -----untuk data tanggal dan jam
from datetime import date
from datetime import datetime

app = Flask(__name__)

# -----Setting Database----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inkel2020'
# khusus untuk MACOS X
app.config['MYSQL_UNIX_SOCKET'] = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
mysql = MySQL(app)


@app.route('/')
def index():
    return render_template('starter.html')


@app.route('/index3')
def index3():
    return render_template('index3.html')

# -------Sensor--------
@app.route('/sensor1', methods=['GET', 'POST'])
def sensor1():
    if request.method == 'POST':
        # mengambil nilai yg dikirimkan
        sensor1 = request.values.get('sensor1')
        sensor2 = request.values.get('sensor2')
        tgl = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO sensor_1(tgljam, nilai, nilai2) VALUES (%s,%s,%s)", (tgl, sensor1, sensor2))
        mysql.connection.commit()
        cur.close()
        return redirect('/')
    elif request.method == 'GET':
        cur = mysql.connection.cursor()
        resultValue = cur.execute(
            "SELECT * FROM sensor_1 order by no desc limit 20")
        if resultValue > 0:
            datasensor = cur.fetchall()
        return render_template('starter.html', data=datasensor)


if __name__ == '__main__':
    app.run()
