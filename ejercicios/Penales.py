#2005.Termino1.Evaluacion1.Tema4

import random

n=int(input('Ingrese el numero de penales: '))
gol=0
lanza=0
golderecha=0
golizquierda=0
golcentro=0

while not (lanza>=n):
    jugador=int(input('Ingrese el area donde pateara (1,2,3,4,5,6): '))
    arquero=int(random.random()*6)+1
    if not(jugador==arquero):
        gol=gol+1
        if (jugador==1 or jugador==6):
            golderecha=golderecha+1
        if (jugador==2 or jugador==5):
            golcentro=golcentro+1
        if (jugador==3 or jugador==4):
            golizquierda=golizquierda+1
    lanza=lanza+1

goleada='izquierda'
if golcentro>golizquierda and golcentro>golderecha:
    goleada='centro'
if golderecha>golizquierda and golderecha>golcentro:
    goleada='derecha'

tapada='izquierda'
if golcentro<golizquierda and golcentro<golderecha:
    tapada='centro'
if golderecha<golizquierda and golderecha<golcentro:
    tapada='derecha'

falla=n-gol
    
print ('Goles totales: ', gol)
print ('Goles derecha: ', golderecha)
print ('Goles centro: ', golcentro)
print ('Goles izquierda: ', golizquierda)
print ('Metieron mas goles en: ', goleada)
print ('Numero de fallas: ', falla)
print ('Fallaron mas goles en: ' , tapada)



