from flask import Flask, render_template, request, redirect, Response
from flask_mysqldb import MySQL
from datetime import date
from datetime import datetime
import pygal
from pygal.maps.world import World

# setting untuk database
app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'inkel2020'
# khusus untuk MACOS X
app.config['MYSQL_UNIX_SOCKET'] = '/Applications/XAMPP/xamppfiles/var/mysql/mysql.sock'
mysql = MySQL(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        Nama = details['name']
        Alamat = details['address']
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO profil(nama, alamat) VALUES (%s, %s)", (Nama, Alamat))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')


@app.route('/sensor1', methods=['GET', 'POST'])
def sensor1():
    if request.method == 'POST':
        print("----------")
        sensor1 = request.values.get('sensor1')
        print(sensor1)
        now = datetime.now()
        tgl = now.strftime("%Y-%m-%d %H:%M:%S")
        print(tgl)
        jam = datetime.now().time()
        print(jam)
        cur = mysql.connection.cursor()
        cur.execute(
            "INSERT INTO sensor_1(tgljam, nilai) VALUES (%s,%s)", (tgl, sensor1))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    elif request.method == 'GET':
        cur = mysql.connection.cursor()
        resultValue = cur.execute(
            "SELECT * FROM sensor_1 order by no desc limit 20")
        if resultValue > 0:
            datasensor = cur.fetchall()
        return render_template('datasensor.html', data=datasensor)


@app.route('/graph/')
def graph():
    """ render svg graph """
    cur = mysql.connection.cursor()
    resultValue = cur.execute(
        "SELECT * FROM sensor_1 order by no desc limit 20")
    if resultValue > 0:
        datasensor = cur.fetchall()
        nilai = []
        for row in datasensor:
            nilai.append(row[2])
    line_chart = pygal.StackedLine(fill=True)
    line_chart.title = 'Realtime Data'
    line_chart.add('Data Sensor', nilai)
    return Response(response=line_chart.render(), content_type='image/svg+xml')


@app.route('/users')
def users():
    cur = mysql.connection.cursor()
    resultValue = cur.execute("SELECT * FROM profil")
    if resultValue > 0:
        userDetails = cur.fetchall()
        return render_template('users.html', userDetails=userDetails)


if __name__ == '__main__':
    app.run()
