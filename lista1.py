#Questão 8
#gerar duas listas com geomspace, somar ambas listas e gráficar a primeira lista
#versus a soma e fazer um gráfico com nome nos eixos e com linha colorida.
import numpy as np
import matplotlib.pyplot as plt
x=np.geomspace(1,5, num=5) #1ª lista
y=np.geomspace(1,8, num=5) #2ª lista
c=x+y #soma
plt.plot(x,c,'m:') #1ª versus a soma
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.show
