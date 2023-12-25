import numpy as np
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense

from nltk.corpus import movie_reviews
from nltk import word_tokenize

# NLTK'nin movie_reviews veri setini kullanalım
nltk.download('movie_reviews')

# Veri setini yükle ve pozitif/negatif olarak etiketle
reviews = [(list(movie_reviews.words(fileid)), category)
           for category in movie_reviews.categories()
           for fileid in movie_reviews.fileids(category)]

# Veri setini karıştır
np.random.shuffle(reviews)

# Metin ve etiketleri ayır
texts, labels = zip(*reviews)

# Tokenizer kullanarak metinleri sayılara dönüştür
max_words = 10000
tokenizer = Tokenizer(num_words=max_words)
tokenizer.fit_on_texts(texts)
sequences = tokenizer.texts_to_sequences(texts)

# Metinleri aynı uzunluğa getir (pad_sequences kullanarak)
maxlen = 200
data = pad_sequences(sequences, maxlen=maxlen)

# Etiketleri numpy dizisine çevir
labels = np.array([0 if label == 'neg' else 1 for label in labels])

# Veriyi eğitim ve test setlerine ayır
training_samples = 1500
validation_samples = 1000

x_train = data[:training_samples]
y_train = labels[:training_samples]
x_val = data[training_samples: training_samples + validation_samples]
y_val = labels[training_samples: training_samples + validation_samples]

# LSTM modeli oluştur
embedding_dim = 100
model = Sequential()
model.add(Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=maxlen))
model.add(LSTM(units=100))
model.add(Dense(units=1, activation='sigmoid'))

# Modeli derle
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Modeli eğit
model.fit(x_train, y_train, epochs=5, batch_size=32, validation_data=(x_val, y_val))

# Modeli değerlendir
loss, accuracy = model.evaluate(x_val, y_val)
print(f"Validation Accuracy: {accuracy * 100:.2f}%")
