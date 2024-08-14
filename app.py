import pickle
#import numpy as np
#import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import *

# from sklearn.linear_model import LassoCV
# from sklearn.linear_model import Lasso

app = Flask(__name__)
#app=applications


#import loaas and scalering pickle
loass_molde=pickle.load(open('models/model.pkl','rb'))
scaler_model=pickle.load(open('models/sc.pkl','rb'))






@app.route("/")

def index():
    return render_template('index.html')

@app.route('/getusersdata',methods=['GET','POST'])
def predict_datapoint():
    if request.method=='POST':
        Temperature=float(request.form.get('temperature'))
        RH=float(request.form.get('rh'))
        #print(RH)
        Ws=float(request.form.get('ws'))
        Rain=float(request.form.get('rain'))
        FFMC=float(request.form.get('ffmc'))
        DMC=float(request.form.get('dmc'))
        DC=float(request.form.get('dc'))
        ISI=float(request.form.get('isi'))
        BUI=float(request.form.get('bui'))
        classes=float(request.form.get('classes'))
        Region=float(request.form.get('region'))
        new_scled_data=scaler_model.transform([[Temperature,RH,Ws,Rain,FFMC,DMC,DC,ISI,BUI,classes,Region]])
        result=loass_molde.predict(new_scled_data)
        #print(result)
        #app.logger.error('testing error log',result)
        return render_template('home.html',results=result[0])
    else:
        return render_template('home.html')


if __name__=="_main__":
    app.run(host="127.0.0.1", port="3000",debug=True)