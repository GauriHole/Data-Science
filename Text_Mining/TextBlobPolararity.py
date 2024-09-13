# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 09:42:54 2024

@author: Lenovo
"""

import pandas as pd
from textblob import TextBlob
sent = "Thi is very excellent"
pol = TextBlob(sent).sentiment.polarity
pol

df = pd.read_csv("Godfather_review.csv")
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']
