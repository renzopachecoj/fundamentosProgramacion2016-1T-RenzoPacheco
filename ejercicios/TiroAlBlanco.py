#2007.Termino1.Evaluacion1.Tema1

import random
import math

n=int(input('numero de dardos: '))
premio=0
i=0 #contador para lanzamientos

while not(i>=n):
    x=(random.random()*160)-80
    y=(random.random()*160)-80
    d=math.sqrt(x**2+y**2)
    if (d<=10):
        premio=premio+50
    if (d>10 and d<=40):
        premio=premio+40
    if (d>40 and d<=80):
        premio=premio+30
    i=i+1

print(' El total ganado es: $' ,  premio)
