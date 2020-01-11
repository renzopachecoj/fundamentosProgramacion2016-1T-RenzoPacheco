#Proyecto.Tema4
#2012.Termino1.Evaluacion2.Tema3

import numpy
import random

n=int(input('Filas: '))
m=int(input('Columnas: '))
pixel=numpy.zeros(shape=(n,m),dtype=int)
negativo=numpy.zeros(shape=(n,m),dtype=int)
f=0

while not f>=n:
    c=0
    while not c>=m:
        pixel[f,c]=int(input('valor: '))
        #pixel[f,c]=int(random.random()*255) *reemplazar en la linea anterior para usar cualquier matriz aleatoria
        c=c+1
    f=f+1
print ('----------Foto----------')
print (pixel)

totaltinta=0
f=0
while not f>=n:
    c=0
    while not c>=m:
       totaltinta=totaltinta+pixel[f,c]
       c=c+1
    f=f+1
print ('------------------------')
print ('Total de tinta: ',totaltinta)
print ('------------------------')

f=0
while not f>=n:
    c=0
    while not c>=m:
       negativo[f,c]=255-pixel[f,c]
       c=c+1
    f=f+1
print ('--------Negativo--------')
print (negativo)
