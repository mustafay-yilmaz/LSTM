import joblib

# Eğitilmiş modelinizi ve diğer gerekli bilgileri içeren bir sözlük oluşturun
model_data = {
    'parameters': "a",
    'embeddings': "a",
    'J': 1,
    'P': 2,
    'A': 3
}

# Model verilerini dosyaya kaydedin
joblib.dump(model_data, 'trained_model.joblib')
