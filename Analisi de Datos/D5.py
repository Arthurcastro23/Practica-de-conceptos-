import pandas as pd
import numpy as np

#Cargar los datos
train_data = pd.read_csv('train.csv')
#Tipos de datos y valores faltantes
train_data.info()
#Estadisticas describe
train_data.describe()
#Columnas
train_data.columns

#Index(['PassengerId','Survived','Pclass', 'Name', 'Sex','Age','SibSp',
#       'Parch','Ticket','Fare','Cabin','Embarked'],dtype='object')
#Analizar la variable objetivo
#----------------------------------------------------------------------
import matplotlib.pyplot as plt
train_data["Survived"].value_counts().plot(kind="bar")
plt.title("Distribucion de Supervivencia")
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad")
plt.show()
#Verificamos su hay alguna relacion entre los sobrevivientes y su sexo
train_data.groupby("Sex")["Survived"].mean().plot(kind='bar')
plt.title("Distribucion de Supervivencia")
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad")
plt.show()
#Relacion entre clase social y supervivencia
train_data.groupby("Pclass")["Survived"].mean().plot(kind="bar")
plt.title("Distribucion de Supervivencia")
plt.xlabel("Sobrevivio")
plt.ylabel("Cantidad")
plt.show()
#Analisis de edad
train_data["Age"].plot(kind="hist",bins=20)
plt.title("Distribucion de las edades")
plt.xlabel("Edad")
plt.show()
#-------------------------------------------------------------------
train_data.boxplot(column="Age",by="Survived")
plt.suptitle("")
plt.show()
#------------------------------------------------------------------
train_data["Age"].fillna(train_data["Age"].median(),inplace=True)
train_data.isnull().sum()
#------------------------------------------------------------------
train_data.info()
#Decodificar varibles categoricas
train_data = pd.get_dummies(train_data,columns=["Sex","Embarked"],drop_first=True)
train_data.head()
#------------------------------------------------------------------
columna_drop = ["Name","PassengerId","Cabin"]
train_data.drop(columns=columna_drop,inplace=True)
#------------------------------------------------------------------
#Cargar los datos
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
#-----------------------------------------------------------------
train["Embarked"].fillna(train["Embarked"].mode()[0],inplace=True)
test["Embarked"].fillna(test["Embarked"].mode()[0],inplace=True)
test["Fare"].fillna(test["Fare"].mode()[0],inplace=True)
train["Fare"].fillna(test["Fare"].mode()[0],inplace=True)
#-----------------------------------------------------------------
train=pd.get_dummies(train,columns=["Sex","Embarked"],drop_first=True)
test=pd.get_dummies(test,columns=["Sex","Embarked"],drop_first=True)

test_id=test['PassengerId']
columna_drop=['Name','Ticket','Cabin','PassengerId']
train.drop(columns=columna_drop,inplace=True)
#----------------------------------------------------------------
from sklearn.linear_model import LogisticRegression 
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

x =train.drop("Survived",axis=1)
y =train["Survived"]
print(x)
print(y)
#-----------------------------------------------------------------
x_trai,x_val,y_train, yval=train_test_split(x,y,test_size=0.2,random_state=42)
#Modelo
model=LogisticRegression(max_iter=200)
model.fit(x_trai, y_train)
#----------------------------------------------------------------
#prediccion
ypred=model.predict(x_val)
print("Prediccion en validacion",x_val)