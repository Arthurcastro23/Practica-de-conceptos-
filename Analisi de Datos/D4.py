
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D as lineStyles

vx = np.array([1,2,3,4,5,6,7,8])
vy = np.array([1,4,6,8,25,36,49,64])

plt.plot(vx, vy, marker='o', linestyle='--', color='b')
plt.title("Graficas")
plt.xlabel("Eje x")
plt.ylabel("Eje y")
plt.grid(True)
plt.show()
#-----------------------------------------------------
#Histogramas
datos=np.random.randn(1000)
plt.hist(datos,bins=30,color='purple',edgecolor='black')
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
#----------------------------------------------------
datos=np.random.randn(1000)
plt.hist(datos,orientation='horizontal',bins=30,color='blue',edgecolor='black')
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.show()
#---------------------------------------------------
#Mapa de dencidad 
x=np.random.randn(1000)
y=np.random.randn(1000)

plt.hexbin(x,y,gridsize=30,cmap='Greys') #cmap
plt.colorbar(label="Frecuencua")

plt.title("Hexbin Plot Mapa de Densidad")
plt.xlabel("Valor x")
plt.ylabel("Valor y")
plt.show()
#------------------------------------------------
#Grafica de barras

categorias=['A','B','C','D']
valores=[23,17,25,29]
plt.bar(categorias,valores)
plt.title("Grafica de barras")
plt.xlabel("Valor x")
plt.ylabel("Valor y")
plt.show()
#------------------------------------------------

categorias=['A','B','C','D']
valores=[23,17,25,29]
valores2=[20,40,14,78]

x=np.arange(len(categorias))

plt.bar(categorias,valores,color='skyblue')
plt.title("Grafica de barras")
plt.xlabel("categorias")
plt.ylabel("Valores")
plt.show()
#----------------------------------------------
categorias=['A','B','C','D']
valores=[23,17,25,29]
valores2=[20,40,14,78]

x=np.arange(len(categorias))
ancho=0.35

#Crear graficas
plt.bar(x-ancho/2,valores,width=ancho,label='Grupo1',color='skyblue')
plt.bar(x+ancho/2,valores2,width=ancho,label='Grupo2',color='blue')
plt.legend()

plt.title("Grafica de barras")
plt.xlabel("categorias")
plt.ylabel("Valores")
plt.show()
#---------------------------------------------------
#Barras apiladas
plt.bar(categorias,valores,label='Grupo1',color="skyblue")
plt.bar(categorias,valores2,bottom=valores,label='Grupo 2',color='red')

plt.title("Grafica de barras apiladas")
plt.xlabel("categorias")
plt.ylabel("Valores")
plt.show()
#----------------------------------------------------
fig, axs = plt.subplots(1,2,figsize=(10,4))

axs[0].bar(categorias, valores)
axs[0].set_title("Grupo1")

axs[1].bar(categorias, valores2)
axs[1].set_title("Grupo2")

plt.suptitle("Comparacion")
plt.show()

#---------------------------------------------------
#Graficas circulares
import matplotlib.pyplot as plt #biblioteca externa 
valores=np.array([.5,.25,.25]) #El porcentaje que conforma a la grafica circular
plt.pie(valores)
plt.show()
#---------------------------------------------------
#import matplotlib.pyplot as plt
etiquetas=['Python','Java','C++','JavaScript']
porcentajes=[40,25,20,15]
colores=["#29c785","#00ffea","#ffe600","#a200ff"] #Los colores que va a tener cada dato diferente
valores=np.array([.5,.25,.20,.5]) #El porcentaje que conforma a la grafica circular
plt.pie(porcentajes,labels=etiquetas,colors=colores,autopct="%1.1f%%",startangle=140)
plt.show()
#--------------------------------------------------

# Plotly
from plotly.offline import iplot
import plotly.graph_objects as go
y=np.array([1,2,3,4,5])
data=[go.Scatter(y=y)]
iplot(data)
#-----------------------------------------------
vx=np.array([1,2,3,4,5])
vy=np.array([1,4,6,9,10])
data=[go.Scatter(x=vx,y=vy, mode="markers")]
print(data)
iplot(data)
#-----------------------------------------------
#Gráficas de barras Separadas
fig,axs=plt.subplots(1,2,figsize=(10,4))
#grafica1
axs[0].bar(categorias,valores,color='blue')
axs[0].set_title("Grupo1")
axs[0].set_ylabel("Valores 1")
#grafica2
axs[1].bar(categorias,valores2,color="orange")
axs[1].set_title("Grupo 2")
plt.suptitle("Comparacion ")
plt.show()