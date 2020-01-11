#2015.Termino1.Evaluacion2.Tema3

import numpy
import random

n=int(input('Numero total de filas: '))
while not n>0:
    n=int(input('Numero total de filas: '))
m=int(input('Numero total de columnas: '))
while not m>0:
    m=int(input('Numero total de columnas: '))
q=int(input('Maximo de tortugas por casilla: '))
while not q>0:
    q=int(input('Maximo de tortugas por casilla: '))
total=int(input('Numero total de tortugas: '))
while not (total<=(n*m*q)) and total>0:
    total=int(input('Numero total de tortugas: '))

isla=numpy.zeros(shape=(n,m), dtype=int)

tortuga=1
while not tortuga>total:
    x=int(random.random()*n)
    y=int(random.random()*m)
    if isla[x,y]<q:
        isla[x,y]=1 + isla[x,y]
        tortuga=tortuga+1
    
print(isla)
