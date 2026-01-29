#Listas
L1=[1,[1,2,3,4,5], 6.7, True]
print(L1[0])        #Imprime el primer elemento de la lista
print(L1[1][1])     #Imprime el segundo elemento de la sublista
print(L1[-1])       #Imprime el último elemento de la lista
#Modificar un elemento de la lista
L1[-1]=2345
print('Lista modificada:',L1)
#Tuplas
tupla=(1,2,3,4,5) #Inmutables
tupla2=1,2,3,4,5 # Con o sin parentesis
print(tupla)
print(tupla2)
#Lista de duplas 
punto=[(0,0),(3,5)]
#Dicccionarios
Dic={"llave1":"Hola"}
print("Diccionario:",Dic)
#Def
def calucarProm(lista):
    if not lista:
        return 
    return sum(lista)/len(lista) #len es la longitud de la lista y sum la suma de los elementos
calif=[7.8,9,7.6,8.8,10]
cal=[]
print("Promedio",calucarProm(calif))
print("Promedio",calucarProm(cal))
#Argumentos por posicion
def imprimirNumeros(*args):
    for a in args: # args es una tupla
        print(a)

imprimirNumeros(1,2,3,4,5)
#Diccionario dinamico
def imprimirValores(**args):
    for argu in args:
        print(argu, args[argu])

imprimirValores(ag1="Hola", arg2=[1,2,3,4], arg3= 34.34)
#Expresiones anonimas 
def cuadrado(x):
    r=x**2
    return r
print(cuadrado(5)) #Imprime el cuadrado de 5
#Sintaxis lambda parametro1, parametro2 : expresion
print(lambda x: x**2)
res=lambda x: x**2
print(res(3)) #Imprime el cuadrado de 3
#Lista de nombres
nombres=["Andre", "Olga", "Paco", "Carlos", "Luis"]
def nombresIniVocal(nombre):
    vocales="AEIOUaeiou"
    if nombre[0] in vocales:
        return True
    else:
        return False

nombresIniVocal(nombres[2])
nombresFiltrados=filter(nombresIniVocal,nombres)
print(list(nombresFiltrados))
#Obtener numeros pares
#Lista de numeros
I=[1,2,3,4,5,6,7,8,9,10]
#Expresio lambda para obtener numeros pares
esPar=lambda num:num%2==0
#print(esPar(4)) #Prueba de la funcion
Res=list(filter(esPar,I)) #Aplica la funcion esPar a cada elemento de la lista I
print(Res)
#----------------------------------
lista=[1,2,3,4,5,6,7]
res2=lambda x:x*x
listaCuadrados = list(map(res2,lista))
print("Lista de cuadrados:",listaCuadrados)
#Sorted 
personas2=[
    {"nombre":"Ana", "edad":29},
    {"nombre":"Luis", "edad":26},
    {"nombre":"Oscar", "edad":35}
]
print(sorted(personas2, key=lambda x:x["edad"]))
#Sin compresion de listas 
#Secuencias de cubos de los primeros enteros
cubos=[]
for i in range(5):
    cubos.append(i**3)
print(cubos)
cubos2=[x**3 for x in range(5)]
print(cubos2)
#----------------------------------
nums=list(range(1,11))
print(nums)
cuadradoPares=[x**2 for x in nums if x%2==0]
print(cuadradoPares)