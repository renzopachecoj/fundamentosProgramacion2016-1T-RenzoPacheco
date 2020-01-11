#Buscaminas

import numpy
matriz = numpy.random.choice([0,-1],(8,8))

print('Matriz inicial\n',matriz)
for i in range(8):
   for j in range(8):
      if(matriz[i,j]==0):
         contar = 0
         #Esquina superior izquierda
         if(i > 0 and j > 0 and matriz[i-1,j-1]==-1):
            contar += 1
         #Esquina superior derecha
         if(i > 0 and j < 7 and matriz[i-1,j+1]==-1):
            contar += 1
         #Superior
         if(i > 0 and matriz[i-1,j]==-1):
            contar += 1
         #esquina inferior izquierda
         if(i < 7 and j > 0 and matriz[i+1,j-1]==-1):
            contar += 1
         #esquina inferior derecha
         if(i < 7 and j < 7 and matriz[i+1,j+1]==-1):
            contar += 1
         #Inferior
         if(i < 7 and matriz[i+1,j]==-1):
            contar += 1
         #Derecha
         if(j < 7 and matriz[i,j+1]==-1):
            contar +=1
         #Izquierda
         if(j > 0 and matriz[i,j-1]==-1):
            contar += 1
         matriz[i,j] = contar
nminas=0
for x in range(8):
   for y in range(8):
      if(matriz[x,y]==-1):
         nminas=nminas+1

print('\nMatriz final\n',matriz)
print (nminas)
