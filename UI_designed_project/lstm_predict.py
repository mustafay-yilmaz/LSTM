from keras.preprocessing.text import Tokenizer
from keras.utils import pad_sequences
import numpy as np
from keras.models import load_model
import config as c

loaded_model = load_model("model9021.h5",compile=False)
loaded_model.summary()

max_sequence_len=46

def generate_text(seed_text, next_words, model, max_sequence_len):
    for _ in range(next_words):
        token_list = c.tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
        predicted_probs = model.predict(token_list, verbose=0)
        predicted = np.argmax(predicted_probs)

        output_word = ""
        for word, index in c.tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        seed_text=str.capitalize(seed_text)
        seed_text += " " + output_word

    seed_text+="."
    return seed_text

def load(kelime,kelime_sayi=7):
    genereted_text = generate_text(kelime,kelime_sayi,loaded_model,max_sequence_len)
    return genereted_text