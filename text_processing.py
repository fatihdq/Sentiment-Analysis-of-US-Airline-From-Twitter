#!/usr/bin/env python
# coding: utf-8

# In[8]:


import joblib
import emot as e
import re

# Convert Emoji
def convert_emoji(text):
    new_text = ''
    for emoji in e.UNICODE_EMOJI:
        if emoji in text:
            text = re.sub(r'[:]',"",
                        re.sub(r'[::]'," ",
                               re.sub(r'['+emoji+']',e.UNICODE_EMOJI_ALIAS[emoji],text)))
    new_text = text
    
    return new_text

# Cleaning Text
def cleaning_text(text):
    pattern1 = r'@[^ ]+'
    pattern2 = r'https?://[^ ]+'
    pattern3 = r'#[^ ]+'
    combined_pattern = r'|'.join((pattern1,pattern2,pattern3))
    www_patt = r'www.[^ ]+'
    text_cleaned = re.sub(www_patt,'',re.sub(combined_pattern,'',text)).lower()

    return text_cleaned

def cleaning_text2(text):
    pattern4 = r'0-9[^ ]+'
    text_cleaned = re.sub("[^a-zA-Z]"," ", re.sub(pattern4,'',text)).lower()
    
    return text_cleaned

def text_processing(text,tokenizer,lemmatizer,stopwords):
    emoji_converted = convert_emoji(text)
    cleaned = cleaning_text(emoji_converted)
    # Tokenizing
    tokenized = tokenizer.tokenize(cleaned)
    # Remove stopwords
    word_stopwords = [w for w in tokenized if w not in stopwords]
    # Normalizing words
    word_lemmatized = [lemmatizer.lemmatize(w) for w in word_stopwords]
    # Untokenizing words
    untokenized = " ".join(w for w in word_lemmatized)
    text_processed = cleaning_text2(untokenized)
    
    return text_processed

