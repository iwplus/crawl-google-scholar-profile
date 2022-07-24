# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:36:30 2021

@author: LENOVO
"""
import pandas as pd

df = pd.read_json('dining.json', lines = True)
export_csv = df.to_csv('diningalaa.csv', index = None, header = True)
