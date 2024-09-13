# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 08:46:41 2024

@author: Lenovo
"""
#1.
import pandas as pd

file = 'diamonds_messy.csv'
df = pd.read_csv(file)
df.head(), df.info(), df.describe(include='all')
df = df.drop(columns=['Unnamed: 0'])
df['y'] = pd.to_numeric(df['y'], errors='coerce')

df = df.dropna()
df = df.drop_duplicates()

df['cut'] = df['cut'].str.strip().str.lower()
df.info(), df.head()

#2