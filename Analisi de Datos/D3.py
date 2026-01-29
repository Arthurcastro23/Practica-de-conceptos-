import numpy as np
import pandas as pd

# propiedades de un array
a=np.array([[1,2,3,4.5],[5,6,7,8]])
print("Forma",a.shape)
print("Dimension",a.ndim)
print("tamaño",a.size)
print("tipo dato",a.dtype)
#------------------------------------
## Indexacion y slicing
a1=np.array([10,19,23,10,1])
print(" Elemento a1[0]",a1[0])
print(" Elemento a1[1]",a1[1])
print(" rebanada a1[1:4]",a1[1:4])

mat=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print("Elemento",mat[1,2])
print("Columna mat[:,1]",mat[:,1])
print("Columna mat[:,2]",mat[:,2])
print("Renglon mat[1,:]",mat[1,:])

dic1={"col1":pd.Series([7,2,3,4],index=['a','b','c','d']), "col2":pd.Series([5,6,7,4],index=['a','b','c','d'])}
df4=pd.DataFrame(dic1)
df4
#------------------------------------
#Otra forma de de formar arreglos
#arange linspace
rango=np.arange(0,10,3)
print(rango)

#------------------------------------
#linspace
lin=np.linspace(0,1,7)
print(lin)
#------------------------------------
#Indexacion y slicing
matriz=np.random.randint(0,10,size=(5,5))
print(matriz)
#------------------------------------
#Modificar los valores mayores que 5 
matriz[matriz>5]=99
print(matriz)
#------------------------------------
#Obtener diagrama principal
diag=np.diag(matriz)
print(diag)
#------------------------------------
#Sumar elementos de la diagonal
print("Suma diagonal",np.sum(diag))
#------------------------------------
#Manipulacion y limpieza de datos con pandas
L=[10,11,12,13,41,15]
serie=pd.Series(L)
print(serie)
#------------------------------------
#Cambiamos un indice numerico por uno de letras
L=[10,11,12,13,41,15]
etiqueta=['a','b','c','d','e','f']
serie2=pd.Series(L,index=etiqueta)
print(serie2)
#Acceso a los datos
print(serie2['b'])
print(serie2.iloc[1])
#------------------------------------
#Operaciones de matrices
mat1=np.array([[1,2,3,4,5],[6,7,8,9,10]])
mat2=np.array([[10,20,30,40,50],[60,70,80,90,100]])
print("Suma")
print(mat1+mat2)
print("Multiplicacion elemento a elemento")
print(mat1*mat2)
print('Potencia')
print(mat1**2)
#------------------------------------
#Ejercicio
matriz=np.random.randint(0,10,size=(5,5))
print(matriz)
#------------------------------------
L=[10,11,12,13,14,15]
L=[1,2,12,3,4,5]

s1=pd.Series(L)
s2=pd.Series(L)

print("Suma Series")
print(s1+s2)
#------------------------------------
#Crear una serie apartir de un diccionario
D={'a':10,'b':20,'c':30,'d':40}
serie3=pd.Series(D)
print(serie3)
#------------------------------------
datos={'nombre':['Ana','Luis','Carlos','Marta'],
       'edad':[23,34,45,25],
        'ciudad':['CDMX','Jalapa','Monterrey','Campeche']
       }
dataFrame1=pd.DataFrame(datos)
dataFrame1

print(dataFrame1['nombre'])
print(dataFrame1[['nombre','ciudad']])
#Agregar un columna ak datafarme
scp=pd.Series([3024,3567,3567,5678])
dataFrame1['CP']=scp
dataFrame1
#Eliminar Co0lumna
del dataFrame1['CP']
dataFrame1
#------------------------------------
res1 = dataFrame1.iloc[0]
res1
#------------------------------------
#buscar que pos de la columna 1 tiene mayor o igual valor que la columna2
filtro=np.greater_equal(df4['col1'],df4['col2'])
print(filtro)
# ------------------------------------
dataFrame1
#-------------------------------------
dataFrame1[dataFrame1["edad"]>25]
#------------------------------------
dataFrame1[(dataFrame1["edad"]>30)& (dataFrame1["ciudad"]=="Jalapa")]
#------------------------------------
#Agregar una columna a partir de otra
dataFrame1["edadDS"]=dataFrame1["edad"]+5
dataFrame1
#------------------------------------
dataFrame1.sort_values(by="edad",ascending=False)