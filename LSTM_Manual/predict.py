import joblib
import numpy as np


def predict(cumle_sayisi):
    model = joblib.load("../LSTM_Manual/trained_model.joblib")
    cumleler = predict(model["Parametres"],model["Embeddings"],model["id_char"],model["vocab_size"],predict_size=cumle_sayisi)
    cumleler = np.array(cumleler).reshape(-1,1)
    return cumleler