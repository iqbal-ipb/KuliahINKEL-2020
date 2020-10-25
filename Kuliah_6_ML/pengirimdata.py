import requests
import random
import time


url = 'http://localhost:5000/sensor1'
i = 0
while(1):
    sensor_suhu = random.random() * 100
    sensor_kelembaban = random.random() * 100
    myobj = {'sensor1': sensor_suhu, 'sensor2': sensor_kelembaban}

    # -------kirim data ke server
    # -------------------------------------------------
    x = requests.post(url, data=myobj)
    print(x.text)
    time.sleep(2)
    i = i+1
