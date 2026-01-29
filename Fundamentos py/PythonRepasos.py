def mayor2(n1,n2):
    if n1 > n2:
        return n1
    else:
        return n2

def principal():
    num1=int(input("Dame n1"))
    num2=int(input("Dame n2"))
    print(f"El mayor de {num1} y {num2} es {mayor2(num1,num2)}" )

principal()

import sys

l3=[[2,3,4,5],[1,2,3,4],[6,7,8,9]]
print(l3[1][2])

#defincion
def imprime(cadena):
    c2=cadena+"hola"
    cadena="prueba"
    print(c2)

def pasoParRef(lista):
    print(lista)
    lista[0]="Nuevo" 

#llamado
c="mundo"
imprime(c)
print(c)

L=[1,2,3,4,5]
pasoParRef(L)
print(L)

# ejemplo con funciones

def cuadrado(x):
    return x*x

def variasOp(x):
    return x**2, x**3 , x**4

def cuadradoDef(x=3):
    return x*x
def sumaTresNumeros(a=0,b=0,c=0):
    return a+b+c
    
    

def main():
    n=2
    r=cuadrado(n)
    r1,r2,r3=variasOp(n)
    rr1,_,rr3=variasOp(n)
    
    print(r)
    print(r1,r2,r3)
    print(rr1,rr3)
    print(cuadradoDef())
    print(cuadradoDef(5))
    print("Resulatdo de la suma de 3 num",sumaTresNumeros(2,3,5))
    print("Resulatdo de la suma de 3 num",sumaTresNumeros())

    
main()

nombre = input("Nombre de usuario:" ) 
#Nos sirve para que los usuarios puedan escribir un dato usando input, ademas input nos permite guardar datos no numericos
edad = int(input("Edad:")) 
#Para que el usuario pueda escribir valores numericos
clave = input("Introdusca una clave de seguridad usando unicamente numeros:")
print("Su nombre es {}, su edad {}, clave {}" .format(nombre, edad, clave))
#Aqui usamos .format para registrar ciertos datos con un orden
print("La informacion mostrada es correcta?")
#Para que nosotros podamos visualizar el texto, lo tenemos que escribir entre comillas
respuesta = input("SI/NO \n")

if respuesta == "SI":
    print("Usuario registrado")
#-----------------------
nombre2 = input("Nombre del usuario:")
if nombre != nombre2:
#Bueno ya sabes como funciona if
    print("Acceso denegado")
    sys.exit(0)
#sys.exit(0) sirve para que el programa se detenga en caso de que la condicion no se cumpla
if nombre == nombre2:
    print("Acceso permitido")
#-----------------------
edad2 = int(input("Edad:"))
if edad != edad2:
    print("Acceso denegado")
    sys.exit(0)

if edad == edad2:
    print("Acceso permitido")
#-----------------------
clave2 = input("Clave de seguridad:")
if clave != clave2:
    print("Acceso denegado")
    sys.exit(0)
if clave == clave2:
    print("Acceso permitido")



print(edad>18)
#Se usa la logica booleana para que al momento de compilar el resultado sea verdadero o falso
print(nombre[0:])
#Para que nosotros podamos visualizar los arreglos 

