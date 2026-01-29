
def sum4(a=0,b=0,c=0,d=0,e=0):
    return (a+b+c+d)*e

#Llamdo de la funcion
def main():

    print("Sitema Unitario de Mayor Accion")
    print('S.U.M.A')
    n1= int(input("Ingrese 1er valor: "))
    n2= int(input("Ingrese 2do valor: "))
    n3= int(input("Ingrese 3er valor: "))
    n4= int(input("Ingrese 4to valor: "))
    X= int(input("Ingrese una valor que multiplicara a los anteriores: "))
    suma4=(n1,n2,n3,n4,'x',X)

    print(suma4)
    print("Resulatdo de la suma de 4 numeros, multiplicados por x = ",sum4(n1,n2,n3,n4,X))

    
main()