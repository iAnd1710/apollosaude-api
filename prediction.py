import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
import pickle
import json

# Opening JSON file
dpt = open('./datasets/pt.json', )

# returns JSON object as
# a dictionary
ptdata = json.load(dpt)

final_rf_model = pickle.load(open('rf_model.pkl', 'rb'))
final_nb_model = pickle.load(open('rf_model.pkl', 'rb'))
final_svm_model = pickle.load(open('svm_model.pkl', 'rb'))

data = pd.read_csv("./datasets/training.csv", encoding="ISO-8859-1").dropna(axis=1)

encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:, :-1]

# --------------

symptoms = X.columns.values

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom_index[value] = index

data_dict = {
    "symptom_index": symptom_index,
    "prediction_classes": encoder.classes_
}


def predict_disease(symptoms):
    symptoms = symptoms.split(",")

    # criando dados de input
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        x = list(k for k, v in data_dict["symptom_index"].items() if symptom.lower() in k.lower())
        if len(x) <= 0:
            x = ['headache']
        index = data_dict["symptom_index"][x[0]]
        input_data[index] = 1

    input_data = np.array(input_data).reshape(1, -1)

    rf_prediction = data_dict["prediction_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["prediction_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["prediction_classes"][final_svm_model.predict(input_data)[0]]

    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]

    dataPrec = pd.read_csv("./datasets/symptom_precaution.csv", encoding="ISO-8859-1")
    prec1 = dataPrec.loc[dataPrec['Disease'] == final_prediction, 'Precaution_1'].iloc[0]
    prec1 = prec1[:1].upper() + prec1[1:]
    prec2 = dataPrec.loc[dataPrec['Disease'] == final_prediction, 'Precaution_2'].iloc[0]
    prec2 = prec2[:1].upper() + prec2[1:]
    prec3 = dataPrec.loc[dataPrec['Disease'] == final_prediction, 'Precaution_3'].iloc[0]
    prec3 = prec3[:1].upper() + prec3[1:]
    prec4 = dataPrec.loc[dataPrec['Disease'] == final_prediction, 'Precaution_4'].iloc[0]
    prec4 = prec4[:1].upper() + prec4[1:]
    predictions = {
        "disease": final_prediction,
        "description": '%s. %s. %s. %s.' % (prec1, prec2, prec3, prec4)
    }
    return predictions
