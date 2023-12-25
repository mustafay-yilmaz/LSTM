import joblib
from lstm import predict
import numpy as np

model = joblib.load("trained_model.joblib")
cumleler = predict(model["Parametres"],model["Embeddings"],model["id_char"],model["vocab_size"],predict_size=30)
cumleler = np.array(cumleler).reshape(-1,1)
print(cumleler)