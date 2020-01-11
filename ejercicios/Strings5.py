#Renzo Pacheco, Jeniffer Urquiza
#TallerDeCadenasDeCaracteres.Tema5

import numpy

romanos = 'IVXLCDM'
equivale = numpy.array([1,5,10,50,100,500,1000])
w=1
x=0
y=0
z=1
cuenta=0
numero=0
encontre=0
n=input('Numero romano: ')
m=[]

while not w>=len(n):
    if n[w-1]==n[w]:
        cuenta=cuenta+1
    else:
        cuenta=cuenta-1
    w=w+1

if cuenta==3:
    n=input('Numero romano: ')

while not x>=len(n):
    while not y>=len(romanos):
        if n[x]==romanos[y]:
            encontre=y
            m.append(equivale[encontre])
        y=y+1
    x=x+1
    y=0

while not z>=len(m):
    if m[z-1]<m[z]:
        m[z-1]=m[z-1]*-1
    z=z+1
           
print (numpy.sum(m))

      
