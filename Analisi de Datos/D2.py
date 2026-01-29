import time

import numpy as np

lista1=range(1000000)
lista2=range(1000000)

arreglo1=np.array(lista1)
arreglo2=np.array(lista2)


tini=time.time()
result=[x-y for x,y in zip(lista1,lista2)]
tfin=time.time()

print("Tiempo", tfin-tini)

tini=time.time()
res2=arreglo1-arreglo2

tfin=time.time()
print("Tiempo", tfin-tini)

#------------------------------

ceros=np.zeros((2,3))
print(ceros)

unos=np.ones(4)
print(unos)

unos2=np.ones((4,5))
print(unos2)

unos342=np.ones((3,4,2))

print(unos342)


a1=np.array([1,2,2,3,4,5,6,8])
a2=np.array([11,22,22,32,42,52,62,82])

print("resta",np.subtract(a2,a1))
print("suma", np.add(a1,a2))
print("potencial", np.power(a1,a2))
print("multiply",np.multiply(a1,a2))
print("raiz cuadrada", np.sqrt(a2))
print("e", np.exp(a1))

#-----------------------------
personas2=[
    {"nombre":"Juan","edad":23,"ciudad":"CDMX"},
    {"nombre":"Ana","edad":30,"ciudad":"GDL"},
    {"nombre":"Luis","edad":28,"ciudad":"CDMX"},
    {"nombre":"Marta","edad":35,"ciudad":"MTY"},
]
nomVivCDMX=[P["nombre"].upper() for P in personas2 if P["ciudad"]=="CDMX"]
print(nomVivCDMX)

mayor30=[(P["nombre"], P["edad"])for P in personas2 if P["edad"]>30]
print(mayor30)

datosOrdenados=sorted(personas2, key=lambda p:p["edad"])
print(datosOrdenados)

menores35NoCDMX=[P["nombre"]for P in personas2 if P["edad"]<35 and P["ciudad"]!="CDMX"]
print(menores35NoCDMX)

#CSV = Valores separados por comas
#import csv
#with open("alumnos.csv", newline='', encoding='utf-8') as a:
 #   lectura=csv.reader(a)
  #  for renglon in lectura:
   #     print(renglon)

#--------------------------------
#datos=[["nombre","edad","promedio"],["Ana",19,8.9],["Luis",17,9.1],]
#with open("alumnos2.csv", "w", newline='', encoding='utf-8') as a:
 #   esc=csv.writer(a)
  #  esc.writerows(datos)

#--------------------------------

vacio=np.empty((3,3))
print(vacio)

#--------------------------------
#Matrices identidades

print(np.eye(7))

#--------------------------------

a1=np.array([4,89,15])
a2=np.array([6,39,15])

#mayor 
print(np.greater(a1,a2))
#mayor o igual
print(np.greater_equal(a1,a2))

#elem1 < elem2
print(np.greater_equal(a1,a2))

print(np.less(a1,a2))

print(np.less_equal(a1,a2))

print(np.equal(a1,a2))

print(np.not_equal(a1,a2))

#--------------------------------
#Funciones booleanas
a1=np.array([True,False,True])
a2=np.array([False,False,False])
print(np.logical_and(a1,a2))

#--------------------------------
#Funciones estadisticas 
datos=np.array([23,45,67,89,12,34,56,78,90])

print("Media:", np.mean(datos))
print("Mediana:", np.median(datos))
print("Desviacion estandar:", np.std(datos))
print("Varianza:", np.var(datos))
print("Maximo:", np.max(datos))
print("Minimo:", np.min(datos))

#--------------------------------

valores, frecs = np.unique(datos, return_counts=True)
print("Valores:", valores)
print("Frecuencias:", frecs)
moda=valores[np.argmax(frecs)]
print("Moda:", moda)