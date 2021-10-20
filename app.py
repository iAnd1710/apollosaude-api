from flask import Flask, request
from flask_cors import CORS, cross_origin

from prediction import predict_disease

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

# O PAI TA ON BIR

@app.route('/', methods=['GET'])
@cross_origin()
def home():
    return 'Apollo API<br>Version 1.0.0<br>© 2021'


@app.route("/disease", methods=["GET"])
def pred_disease():
    prediction = ""
    if request.method == 'GET':

        symptoms = request.args.get('symptoms')  # np.array

        if symptoms is None:
            return ""

        prediction = predict_disease(str(symptoms))

    return str(prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
