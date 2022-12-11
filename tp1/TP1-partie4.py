# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 05:06:37 2021

@author: i__t__s
"""

import pandas 

Columns = ['NumTimesPrg', 'PlGlcConc', 'BloodP', 'SkinThick', 'TwoHourSerIns', 'BMI', 'DiPedFunc', 'age', 'HasDiabetes']

dataframe = pandas.read_csv('pima-indians-diabetes.data.csv')

dataframe.columns=Columns

print(dataframe.shape) #taille de la matrice

print(dataframe.head(10)) #head(Nbre_ligne)

print(dataframe['BloodP'])

print(dataframe.describe())

array = dataframe.values
X = array[:,0:7]
print(X)