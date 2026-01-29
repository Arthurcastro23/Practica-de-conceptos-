#Lista de nombres que viven en CDMX
LNombres=['ARTHUR','STEVE','ANGELICA','JENNYFER','EDWARD','ABIGAIL','CHARLES','ERIC']
#Personas mayores de 30 QUE VIVEN EN CDMX 
Ltuplas=[('SHELDON',45),('BERNARD',36),('CHARLES',15),('DAVID',40),('EDWARD',45)]    
#Order la lista por edad (usar sorted y lambda)
LtuplasOrdenadas=sorted(Ltuplas,key=lambda x: x[1])
print("Lista de nombres:",LNombres)
print("Lista de tuplas ordenadas por edad:",LtuplasOrdenadas)
#Imprimir los nombres de los menores de 35 años
print("Nombres de los menores de 35 años:")
for nombre,edad in LtuplasOrdenadas:
    if edad<35:
        print(nombre)