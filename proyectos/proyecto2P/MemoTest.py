#2007.Termino2.Evaluacion2.Tema2
import numpy
import random

print ('Juego Memotest')
tablero=numpy.zeros(shape=(4,4),dtype=int)
tope=16
nfichas=0
repetidas=[]
while not nfichas>=tope:
    numero=int(random.random()*8)+1
    f=int(random.random()*4)
    c=int(random.random()*4)
    if (tablero[f,c]==0) and (numero not in tablero):
        tablero[f,c]=numero
        nfichas=nfichas+1
    if (tablero[f,c]==0) and (numero not in repetidas):
        tablero[f,c]=numero
        nfichas=nfichas+1
        repetidas.append(numero)
print (tablero)

puntos=0
fallos=0
while not ((puntos>=8) or (fallos>=3)):     
    fila1=int(input('Fila de casilla 1: '))
    columna1=int(input('Columna de casilla 1: '))
    fila2=int(input('Fila de casilla 2: '))
    columna2=int(input('Columna de casilla 2: '))
    fila1=fila1-1
    fila2=fila2-1
    columna1=columna1-1
    columna2=columna2-1
    print('Casillas contienen ',tablero[fila1,columna1],' y ',tablero[fila2,columna2])
    if (tablero[fila1,columna1]==tablero[fila2,columna2]):
        print('Acertaste!')
        puntos=puntos+1
    else:
        print('Fallaste!')
        fallos=fallos+1
        
if puntos==8:
    print ('Ganaste')
if fallos==3:
    print ('Perdiste')
print('Puntos: ',puntos)
print('Fallos: ',fallos)
