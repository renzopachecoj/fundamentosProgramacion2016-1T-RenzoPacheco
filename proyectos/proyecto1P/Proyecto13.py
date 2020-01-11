#Proyecto.Tema3
#2013.Termino2.Evaluacion2.Tema2

import numpy
cadena=input('Ingrese ADN: ')
cadena=cadena.upper()
tamano=len(cadena)
bandera=numpy.zeros(tamano, dtype=int)
referencia='ACGT'

i=0
while not i>=tamano:
    encontre=0
    j=0
    while not (j>=4):
        if (cadena[i]==referencia[j]):
            encontre=1
        j=j+1
    if encontre==1:
        bandera[i]=1
    i=i+1
suma=bandera.sum()
while suma<len(cadena):
    cadena=input('Ingrese ADN: ')
    cadena=cadena.upper()
    i=0
    while not i>=tamano:
        encontre=0
        j=0
        while not (j>=4):
            if (cadena[i]==referencia[j]):
                encontre=1
            j=j+1
        if encontre==1:
            bandera[i]=1
        i=i+1
    suma=bandera.sum()   
print(cadena)

y=1
cuentaordenados=0
while not y>=tamano:
    if cadena[y-1]<=cadena[y]:
        cuentaordenados=cuentaordenados+1
    y=y+1
print ('Pares ordenados: ',cuentaordenados)
