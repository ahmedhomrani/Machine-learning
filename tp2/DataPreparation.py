# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 10:09:21 2018

@author: Asma
"""
#import csv
import pandas 
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler



Columns = ['NumTimesPrg', 'PlGlcConc', 'BloodP', 'SkinThick', 'TwoHourSerIns', 'BMI', 'DiPedFunc', 'age', 'HasDiabetes']
dataframe = pandas.read_csv('pima-indians-diabetes.data.csv')

dataframe.columns=Columns


# Calculate the median value for SkinThick
median_bmi = dataframe[dataframe['SkinThick']!=0].median()

# Substitute it in the SkinThick column of the
# dataset where values are 0
dataframe['SkinThick'] = dataframe['SkinThick'].replace(0,median_bmi['SkinThick'])


# Il est impossible de faire la même chose avec l'attribut "NumTimesPrg" car la valeur zero 
# est significative (ne correspond pas à une valeur nulle) 


#Uniformisation d'échelle
array = dataframe.head(5).values
X = array[:,0:7]
scaler = MinMaxScaler(feature_range=(0, 1))
rescaledX = scaler.fit_transform(X)
print(rescaledX)


#Normalisation
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)
print(rescaledX)






        