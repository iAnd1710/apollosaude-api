from flask import Flask
from flask.globals import request
from flask_cors import CORS, cross_origin
import numpy as np
import pickle

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

model = pickle.load(open('model.pickle', 'rb'))


@app.route("/")
@cross_origin()
def helloWorld():
    return "Hello World!"


@app.route("/disease", methods=["GET"])
def predDisease():
    
    if request.method == 'GET':
        
        symptoms = np.array(request.args.get('symptoms'))
        
        prediction = model.predict(symptoms) 
        
    return (str(prediction))
        


if __name__ == '__main__':
    app.run(debug=True)
     