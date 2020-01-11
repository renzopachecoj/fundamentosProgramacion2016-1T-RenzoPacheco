#Proyecto.Tema1
#2013.TerminoI.Evaluacion2.Tema1

import numpy
import random

tabla=numpy.zeros(shape=(5,5),dtype=int)
f=0
c=0
i=1
x=0

while c<len(tabla):
    while f<len(tabla):
        tabla[f,c]=int(random.random()*15)+i
        while (tabla[f,c]==tabla[f-1,c])or(tabla[f,c]==tabla[f-2,c])or(tabla[f,c]==tabla[f-3,c])or(tabla[f,c]==tabla[f-4,c]):
            tabla[f,c]=int(random.random()*15)+i
        f=f+1
    f=0
    c=c+1
    i=i+15

while x<len(tabla):
    tabla[:,x].sort()
    x=x+1

tabla[2,2]=0

print (tabla)

