from tensorflow import keras
from keras.preprocessing import text
from keras.utils import pad_sequences
import numpy as np
import pandas as pd

def main(test):
    print("======Filtering Information...======")

    model = keras.models.load_model('models/LSTM_model.h5')
    df = pd.read_csv("tokenize.csv")
    df = list(df.text.values)

    test.reset_index(drop=True, inplace=True)

    token = text.Tokenizer(num_words=None)
    max_len = 100

    xtest = test.text.values
    token.fit_on_texts(list(df))

    xtest_seq = token.texts_to_sequences(xtest)
    xtest_pad = pad_sequences(xtest_seq, maxlen=max_len)

    scores = model.predict(xtest_pad)
    scores = np.where(scores > 0.5, 1, 0)

    test['label'] = scores
    test = test.loc[test['label']==1]

    return test
