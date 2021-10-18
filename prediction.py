import pandas as pd
import numpy as np
from scipy.stats import mode
from sklearn.preprocessing import LabelEncoder
import pickle

final_rf_model = pickle.load(open('rf_model.pkl', 'rb'))
final_nb_model = pickle.load(open('nb_model.pkl', 'rb'))
final_svm_model = pickle.load(open('svm_model.pkl', 'rb'))

data = pd.read_csv("./datasets/training.csv", encoding = "ISO-8859-1").dropna(axis=1)

encoder = LabelEncoder()
data["prognosis"] = encoder.fit_transform(data["prognosis"])

X = data.iloc[:, :-1]

# --------------

symptoms = X.columns.values

symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index
    

data_dict = {
    "symptom_index": symptom_index,
    "prediction_classes": encoder.classes_
}


def predictDisease(symptoms):
    symptoms = symptoms.split(",")
    
    #criando dados de input
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1
        
    input_data = np.array(input_data).reshape(1,-1)
    
    rf_prediction = data_dict["prediction_classes"][final_rf_model.predict(input_data)[0]]
    nb_prediction = data_dict["prediction_classes"][final_nb_model.predict(input_data)[0]]
    svm_prediction = data_dict["prediction_classes"][final_svm_model.predict(input_data)[0]]

    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])[0][0]
    predictions = {
        "Previsão do modelo 'Random Forest'": rf_prediction,
        "Previsão do modelo 'Naive Bayes": nb_prediction,
        "Previsão do modelo 'SVM'": nb_prediction,
        "Previsão Final": final_prediction
    }
    return predictions

    
            