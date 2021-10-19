from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
from prediction import predictDisease

app = Flask(__name__)

app.config['CORS_HEADERS'] = 'Content-Type'

#model = pd.read_pickle(r'disease.pkl')

#with open('disease.pickle', 'rb') as f:
#    model = pickle.load(f)         

        
@app.route('/', methods=['GET'])
def home():
    return 'Apollo API<br>Version 1.0.0<br>© 2021'


@app.route("/disease", methods=["GET"])
def pred_disease():
    
    if request.method == 'GET':
        
        symptoms = request.args.get('symptoms') #np.array

        if symptoms is None:
            return ""
        
        prediction = predictDisease(str(symptoms))
        
    return str(prediction)
        

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)