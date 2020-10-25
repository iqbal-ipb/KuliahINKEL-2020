import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)

# load model yg telah ditraining
model = pickle.load(open('model_aerator.pkl', 'rb'))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    '''
    mengambil nilai yg dikirim dari form
    '''
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)

    return render_template('index.html', prediction_text='Kecepatan Aerator seharusnya {}'.format(output))


@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    ini jika ingin menggunakan API
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run()
