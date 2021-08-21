#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from text_processing import *

model = joblib.load('svm_model.pkl')
tfidf = joblib.load('tfidf.pkl')
token = joblib.load('tokenizer.pkl')
stopwords = joblib.load('stopwords.pkl')
lemmatizer = joblib.load('lemmatizer.pkl')

def prediction(text):
    text_pro0 = text_processing(text,token,lemmatizer,stopwords)
    vectorized = tfidf.transform([text_pro0])
    text_pro = vectorized.toarray().reshape(1,-1)
    pred = model.predict(text_pro)
    return pred

