#Proyecto.Tema5
#2005.Termino1.Evaluacion2.Tema4

import numpy

p=int(input('Numero de actividades: '))
n=int(input('Numero de estudiantes: '))
ponderaciones=numpy.zeros(p,dtype=int)
nombres=[]
calificaciones=numpy.zeros(shape=(n,p),dtype=int)
final=numpy.zeros(n,dtype=int)
sumap=0
x=0
while not sumap==100:
    if sumap!=100:
        x=0
        sumap=0
        while not x>=len(ponderaciones):
            print('Ponderacion',x+1,':')
            ponderaciones[x]=int(input('Valor: '))
            sumap=sumap+ponderaciones[x]
            x=x+1

x=0
nombre=''
while not x>=n:
    nombre=input('Nombre del estudiante: ')
    nombres.append(nombre)
    x=x+1

x=0
y=0
while not x>=n:
    while not y>=p:
        calificaciones[x,y]=int(input('Notas del estudiante: '))
        y=y+1
    x=x+1
    y=0

x=0
y=0
nota=0
while not x>=n:
    while not y>=p:
        nota=nota+((calificaciones[x,y]/100)*ponderaciones[y])
        final[x]=nota
        y=y+1
    x=x+1
    y=0
    nota=0

x=0
maximo=final[0]
nombremax=''
while not x>=len(final):
    if final[x]>maximo:
        maximo=final[x]
        nombremax=nombres[x]
    x=x+1

x=0
nombremin=''
minimo=final[0]
while not x>=len(final):
    if final[x]<minimo:
        minimo=final[x]
        nombremin=nombres[x]
    x=x+1 
    

print ('Ponderaciones(Leccion, Proyecto, Examen): ')
print (ponderaciones)
print ('Estudiantes: ')
print (nombres)
print ('Calificaciones:')
print (calificaciones)
print ('Notas (sobre 100): ')
print (final)
print ('Nota maxima: ',nombremax,maximo)
print ('Nota minima: ',nombremin,minimo)
