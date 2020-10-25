from flask import Flask, render_template, url_for, request, redirect, make_response
import random
import json
from time import time
from datetime import date
from datetime import datetime
from random import random
from flask import Flask, render_template, make_response
from flask_mysqldb import MySQL

app = Flask(__name__)

# -----Setting Database----------------
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inkel2020'
# khusus untuk MACOS X
app.config['MYSQL_UNIX_SOCKET'] = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
mysql = MySQL(app)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Humidity]
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM sensor_1 order by no desc limit 1")
    if resultValue > 0:
        datasensor = cur.fetchall()
        print(datasensor[0][0])  # No
        print(datasensor[0][1])  # TanggalJam
        print(datasensor[0][2])  # Nilai
        print(datasensor[0][3])  # Nilai2
        Temperature = datasensor[0][2]
        Humidity = datasensor[0][3]
        data = [time() * 1000, Temperature, Humidity]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    else:
        Temperature = 0
        Humidity = 0
        data = [time() * 1000, Temperature, Humidity]
        response = make_response(json.dumps(data))
        response.content_type = 'application/json'
    return response

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
            "INSERT INTO sensor_1(tgljam, nilai, nilai2) VALUES (%s,%s, %s)", (tgl, sensor1, sensor2))
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


if __name__ == "__main__":
    app.run()
