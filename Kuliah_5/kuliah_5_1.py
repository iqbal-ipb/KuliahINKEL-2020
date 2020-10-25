import pandas as pd
from matplotlib import pyplot as plt
import matplotlib
from datetime import datetime
data_mentah = pd.read_csv('hasilrata_crop.csv', delimiter=',', names=[
                          'no', 'tanggal', 'jarak'])

#datetime_object = datetime.strptime(data_mentah[:]['tanggal'][1], '%Y-%m-%d %H:%M:%S')


data_filter = data_mentah['jarak']+abs(min(data_mentah['jarak']))
tgljam = pd.to_datetime(data_mentah['tanggal'])

dates = matplotlib.dates.date2num(tgljam)
plt.plot_date(dates, data_filter, 'b-')

# -----
fig = plt.figure(figsize=(8, 2), dpi=100)
ax = fig.add_axes([0, 0, 1, 1])
ax.plot_date(dates, data_filter, 'b-')
