from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('kolam.csv')
dataset

X = dataset.iloc[:, :4]
y1 = dataset.iloc[:, -1]
y2 = dataset.iloc[:, -2]
y2

plt.plot(X, y1)
plt.plot(X, y2)
# training untuk model pompa (y1)
regressor = LinearRegression()
regressor.fit(X, y1)
pickle.dump(regressor, open('model_pompa.pkl', 'wb'))

# training untuk model aerator (y2)
regressor = LinearRegression()
regressor.fit(X, y2)
pickle.dump(regressor, open('model_aerator.pkl', 'wb'))


# tes model
model = pickle.load(open('model_aerator.pkl', 'rb'))
print(model.predict([[30.12, 35.39, 8.10, 8.56]]))
