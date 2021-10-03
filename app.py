from flask import Flask, request
from flask_cors import CORS, cross_origin
import numpy as np
import pickle
import pandas as pd

from prediction import predictDisease

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

#model = pd.read_pickle(r'disease.pkl')

#with open('disease.pickle', 'rb') as f:
#    model = pickle.load(f)         

        
@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello World!"


@app.route("/disease", methods=["GET"])
def predDisease():
    
    if request.method == 'GET':
        
        symptoms = str(request.args.get('symptoms')) #np.array
        
        prediction = predictDisease(symptoms) 
        
    return (str(prediction))
        

if __name__ == '__main__':
    app.run(debug=True)