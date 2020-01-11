#Tarea1.Ejercicio12

import math
  
a=float(input('Ingresa a: ')) #largo del bloque
b=float(input('Ingresa b: ')) #ancho del bloque
c=float(input('Ingresa c: ')) #altura del bloque
d=float(input('Ingresa d: ')) #diametro del agujero

#Calculo de las distancias
d1=math.sqrt((a*a)+(b*b))
d2=math.sqrt((b*b)+(c*c))
d3=math.sqrt((a*a)+(c*c))
pasa=False #variable para determinar le valor de verdad

#comprobacion de las distancias
if d1<d:
    pasa=True

if d2<d:
    pasa=True

if d3<d:
    pasa=True

print ('Pasara el bloque:' , pasa)




