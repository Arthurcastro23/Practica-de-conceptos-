#Definimos sum4 que suma 4 numeros y los multiplica por un 5to
def sum4(a=0,b=0,c=0,d=0,e=0): # Inicializa la funcion sum4 con el valor de 0 para cada variable
    return (a+b+c+d)*e # Retorne la suma de los 4 numeros multiplicados por el 5to

#Llamdo de la funcion
def main():

    print("Sitema Unitario de Mayor Accion") # Titulo del programa 
    print('S.U.M.A') # Acronimo del programa
    L1=[1,2,3,4,5] # L1 es la variable en la que se gurdara la lista de numeros 
    n1=(L1[0])
    n2=(L1[1])
    n3=(L1[2])
    n4=(L1[3])
    X=(L1[4]) # X es la variable que multiplicara a las variables n1,n2,n3,n4
    suma4=(n1,n2,n3,n4,X) # Valor de la definicion sum4 que contiene las variables anteriores

    print(suma4) 
    print("Resulatdo de la suma de 4 numeros, multiplicados por x = ",sum4(n1,n2,n3,n4,X))

    
main()