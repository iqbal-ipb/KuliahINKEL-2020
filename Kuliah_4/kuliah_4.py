import pandas as pd

#tinggi_air = pd.read_csv('hasilrata_crop.csv', delimiter=',')
tinggi_air = pd.read_csv('hasilrata_crop.csv', delimiter=',', names=[
    'no', 'tanggalJam', 'tinggiAir'])
tinggi_air.head()
tinggi_air.tail()
tinggi_air.sample(10)
tinggi_air[['tanggalJam', 'tinggiAir']]
tinggi_air.tinggiAir
tinggi_air['usertinggiAir']
tinggi_air.tinggiAir <= 200
tinggi_air[tinggi_air.tinggiAir <= 200]
