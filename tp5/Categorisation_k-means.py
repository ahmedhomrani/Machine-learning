# -*- coding: utf-8 -*-
"""
Created on Sat Oct 26 06:08:58 2019

@author: Asma
"""


import pandas 
import imageio
from sklearn.preprocessing import StandardScaler
from matplotlib import pyplot as plt
from sklearn.preprocessing import MinMaxScaler
#from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import KMeans
import numpy as np




Columns = ['NumTimesPrg', 'PlGlcConc', 'BloodP', 'SkinThick', 'TwoHourSerIns', 'BMI', 'DiPedFunc', 'age', 'HasDiabetes']

dataframe = pandas.read_csv('pima-indians-diabetes.data.csv')

dataframe.columns=Columns

#construction de l'ensemble de données formé par 100 individus et 2 variables
array = dataframe.values
data = array[:100,1:3]

#normalisation 
scaler = MinMaxScaler(feature_range=(0, 1))
data = scaler.fit_transform(data)
scaler.transform(data)
 
# Affichage des points initiaux 
plt.scatter(data[:,0], data[:,1], c='r')
plt.show()

"""
#effectuer la catégorisation en 2 classes avec k-means
kmeans = KMeans(n_clusters=2)
kmeans.fit(data)
y_km = kmeans.fit_predict(data)
#Afficher les poitns aprés la la catégorisation pour 2 classes 
plt.scatter(data[y_km ==0,0], data[y_km == 0,1], s=20, c='r')
plt.scatter(data[y_km ==1,0], data[y_km == 1,1], s=20, c='m')
#Conclusion : points abérants ont été inclus dans l'une des deux classes 
"""
"""
#effectuer la catégorisation en 3 classes avec k-means
kmeans = KMeans(n_clusters=3)
kmeans.fit(data)
y_km = kmeans.fit_predict(data)
#Afficher les poitns aprés la la catégorisation pour 3 classes 
plt.scatter(data[y_km ==0,0], data[y_km == 0,1], s=20, c='r')
plt.scatter(data[y_km ==1,0], data[y_km == 1,1], s=20, c='m')
plt.scatter(data[y_km ==2,0], data[y_km == 2,1], s=20, c='y')
#Conclusion : la troisième classe ne contient que les points abérants 
"""

#effectuer la catégorisation en 4 classes avec k-means
kmeans = KMeans(n_clusters=4)
kmeans.fit(data)
y_km = kmeans.fit_predict(data)
#Afficher les poitns aprés la la catégorisation pour 4 classes 
plt.scatter(data[y_km ==0,0], data[y_km == 0,1], s=20, c='r')
plt.scatter(data[y_km ==1,0], data[y_km == 1,1], s=20, c='m')
plt.scatter(data[y_km ==2,0], data[y_km == 2,1], s=20, c='y')
plt.scatter(data[y_km ==3,0], data[y_km == 3,1], s=20, c='b')
#Conclusion : sensibilité de k-means au bruit: un groupe  qui a été divisé en deux 