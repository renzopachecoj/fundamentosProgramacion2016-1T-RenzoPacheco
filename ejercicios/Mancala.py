#Mancala

import numpy
tablero=numpy.zeros(shape=(2,8),dtype=int)
f=0
c=1
while not f>=2:
    while not c>=7:
        tablero[f,c]=4
        c=c+1
    f=f+1
    c=1
print(tablero)
#----------------------------------------------------------------------
def modtablero (tablero,jugador,c):
    semillas=tablero[jugador-1,c]
    i=1
    if jugador==1:
        while not (semillas<=0):
            while not c+i>=8:
                tablero[0,c]=tablero[0,c]-1
                tablero[0,c+i]=tablero[0,c+i]+1
                semillas=semillas-1
                i=i+1
            if c+i==8:
                while not i>=5:
                    a=7
                    b=0
                    tablero[0,c]=tablero[0,c]-1
                    tablero[1,a-b]=tablero[1,a-b]+1
                    semillas=semillas-1
                    i=i+1
                    b=b-1
        return(tablero)
    if jugador==2:
        while not (semillas<=0):
            while not ((c-i)<=-1):
                tablero[1,c]=tablero[1,c]-1
                tablero[1,c-i]=tablero[1,c-i]+1
                semillas=semillas-1
                i=i+1
            if c-i==-1:
                while not i>=5:
                    a=0
                    b=0
                    tablero[1,c]=tablero[1,c]-1
                    tablero[0,a+b]=tablero[0,a+b]+1
                    semillas=semillas-1
                    i=i+1
                    b=b+1
        return(tablero)
#------------------------------------------------------------------------------

while not ((tablero[0,7]+tablero[1,7])>=24 or (tablero[0,0]+tablero[1,0])>=24):
    jugador=int(input('Jugador: '))
    while not (jugador==1) or (jugador==2):
        jugador=int(input('Jugador: '))
    c=int(input('Casilla: '))
    while not ((c>1) and (c<8)):
        c=int(input('Casilla: '))
    c=c-1 
    tablero=modtablero(tablero,jugador,c)
    print (tablero)

if (tablero[0,7]+tablero[1,7])>=24:
    print('Gana jugador 2')

if (tablero[0,0]+tablero[1,0])>=24:
    print('Gana jugador 1')
