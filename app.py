from flask import Flask,render_template,request
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application

with open('regre.pkl','rb') as file:
    model = pickle.load(file)
with open('scaler.pkl','rb') as file:
    sc=pickle.load(file)

model
@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/predict_data',methods=['GET','POST'])
def predict():
    if request.method=='POST':
        rd_spend = float(request.form.get('R&D_Spend'))
        administration = float(request.form.get('Administration'))
        marketing_spend = float(request.form.get('Marketing_Spend'))
        state_california = float(request.form.get('State_California'))
        state_new_york = float(request.form.get('State_New_York'))
        state_florida = float(request.form.get('State_Florida'))
        
        sc_data = sc.transform([[rd_spend,administration,marketing_spend,state_california,state_new_york,state_florida]])
        result = model.predict(sc_data)
        return render_template('predict_profit.html',results=result[0])
        
    else:
        return render_template('predict_profit.html')

if __name__=='__main__':
    app.run()