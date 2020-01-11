#2005.Termino1.Evaluacion2.Tema4

import random

meta=int(input('Meta: '))
casillaA=0
casillaB=0

while (casillaA<=meta) or (casillaB<=meta):
    dadoA=int(random.random()*6)+1
    casillaA=casillaA+dadoA
    dadoB=int(random.random()*6)+1
    casillaB=casillaB+dadoB
    print (casillaA, casillaB)

if casillaA>casillaB:
    ganador=1
if casillaB>casillaA:
    ganador=2

print ('Gana el jugador: ' , ganador)
