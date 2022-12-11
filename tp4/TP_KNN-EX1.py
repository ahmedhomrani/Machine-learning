# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 10:30:43 2019

@author: Asma
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris
from sklearn.metrics import confusion_matrix,classification_report


#Q1-a Importer les données
X= load_iris().data

#Q1-b : Importer les labels des classes
y= load_iris().target

#Q2: Afficher les noms des variables
print("Les variables : ", load_iris().feature_names) # 4 variables 

#Q3: Afficher les classes
print("Les classes : ",load_iris().target_names) #3 classes  ==> classification multiclasses

#Q4: Normaliation des données 
scaler = StandardScaler().fit(X)
rescaledX = scaler.transform(X)

#Q5: Fonction KNN
def K_NN(X_train, X_test, y_train, y_test ,k):
    knn = KNeighborsClassifier(n_neighbors=k)
    #Pas d'apprentissage d'un modèle pour le KNN ==>
    #la fonction fit ne fait pas de l'apprentissage mais elle sert seulement 
    #à la structuration des données)
    Res_KNN=knn.fit(X_train, y_train)
    
    #Prédiction sur les données de test
    y_pred=knn.predict(X_test)
    taux_erreur_test=(1-Res_KNN.score(X_test,y_test))
    print('Taux d\'erreur sur l\'ensemble de test',taux_erreur_test)
    
    return y_pred

#Q6: Construire les ensembles d'apprentissage(60%) et de test(40%)
X_train, X_test, y_train, y_test = train_test_split(rescaledX, y, test_size=0.4)

#Q7: appliquer KNN avec k=7
K_NN(X_train, X_test, y_train, y_test ,2)

#Q8: établir une validation croisée pour déterminer la meilleure valeur de k 
param=[{"n_neighbors":list(range(1,15))}]
knn= GridSearchCV(KNeighborsClassifier(),param,cv=5,scoring='accuracy')
Res_KNN=knn.fit(X_train, y_train)
best_k=Res_KNN.best_params_["n_neighbors"]
print("Meilleure valeur de k : ",best_k)

#---Classification par KNN en utilisant la meilleure valeur de k 
y_pred=K_NN(X_train, X_test, y_train, y_test ,best_k)

#Q9: Matrice de Confusion
CM=confusion_matrix(y_test, y_pred)
print('Matrice de Confusion',CM)

#Q10 : Rappel et précision 
# Ref: https://ai.plainenglish.io/understanding-confusion-matrix-and-applying-it-on-knn-classifier-on-iris-dataset-b57f85d05cd8
print(classification_report(y_test, y_pred))