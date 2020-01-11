#2007.Termino1.Evaluacion2.Tema1

import random
import numpy

n=int(input('Numero de letras: '))
m=int(input('Numero de palabras: '))
while not n>=2:
    n=int(input('Letras en la palabra: '))
letras=0
lista=[]
palabra=''
npalabras=0
consonante='bcdfghjklmnpqrstvwxyz'
vocal='aeiou'

while not npalabras>=m:
    #palabra=''
    while not letras>=n:
        c=int(random.random()*len(consonante))
        v=int(random.random()*len(vocal))
        palabra=palabra+consonante[c]+vocal[v]
        letras=letras+2
    lista.append(palabra)
    npalabras=npalabras+1
print (lista)
