import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__) #Initialize the flask App
model = pickle.load(open('HD_RF.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home1',methods=['POST'])
def home1():
    return render_template('home1.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    prediction = model.predict(final_features)

    output = round(prediction[0], 2)
    if int(output)==1:
            prediction='You have Heart disease'
    else:
            prediction='Great! You Don\'t have Heart disease'
    return render_template('predict.html',prediction_text = ' {} '.format(prediction),output=output)

if __name__ == "__main__":
    app.run(debug='true')
