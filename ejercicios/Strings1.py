#Renzo Pacheco, Jeniffer Urquiza
#TallerDeCadenasDeCaracteres.Tema1

import numpy

romanos = 'IVXLCDM'
equivale = numpy.array([1,5,10,50,100,500,1000])
x=0
y=0
z=0
numero=0
encontre=0
n=input('Numero romano: ')

while not y>=len(romanos):
    if n==romanos[y]:
        z=z+1
    y=y+1

if z==1:
    while not x>=len(romanos):
        if n==romanos[x]:
            encontre=x
        x=x+1

    numero=equivale[encontre]
    print (numero)

else:
    print ('-1')


