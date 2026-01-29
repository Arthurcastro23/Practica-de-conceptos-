# funciones

def sum4(a=0,b=0,c=0,d=0,e=0):
    return (a+b+c+d)*e

#Llamdo de la funcion
def main():
    n1=1
    n2=2
    n3=3
    n4=4
    X=3
    suma4=(n1,n2,n3,n4,'x',X)

    print(suma4)
    print("Resulatdo de la suma de 4 numeros, multiplicados por x = ",sum4(n1,n2,n3,n4,X))

    
main()