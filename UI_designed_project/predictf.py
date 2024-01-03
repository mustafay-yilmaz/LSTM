import joblib
import numpy as np
import sys

import sys
sys.path.append("../LSTM_Manual")
# sys.path.append("../LSTM_new/")
from lstm import predict
# import LSTM_new.lstm_predict
import lstm_predict


def predict_cumle(cumle_sayisi,proje,kelime="kız",kelime_sayi=7):
    if(proje=="manuel"):
        model = joblib.load("../LSTM_Manual/trained_model.joblib")
        # print(model["Parametres"])
        cumleler = predict(parameters=model["Parametres"],embeddings=model["Embeddings"],id_char=model["id_char"],vocab_size=model["vocab_size"],predict_size=cumle_sayisi)
        cumleler = np.array(cumleler).reshape(-1,1)
        return cumleler
    else:
        text = lstm_predict.load(kelime,kelime_sayi)
        return text
    