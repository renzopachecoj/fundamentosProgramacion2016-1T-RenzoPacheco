#Renzo Pacheco, Jeniffer Urquiza
#TallerDeCadenasDeCaracteres.Tema3

import numpy

romanos = 'IVXLCDM'
equivale = numpy.array([1,5,10,50,100,500,1000])
x=0
y=0
numero=0
encontre=0
n=input('Numero romano: ')
m=[]

while not x>=len(n):
    while not y>=len(romanos):
        if n[x]==romanos[y]:
            encontre=y
            m.append(equivale[encontre])
        y=y+1
    x=x+1
    y=0

print (numpy.sum(m))

      
