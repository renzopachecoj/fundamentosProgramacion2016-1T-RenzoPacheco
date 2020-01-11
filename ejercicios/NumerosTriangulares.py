#2003.Termino3.Evaluacion1.Tema2

n=int(input('Ingrese el numero de pisos: '))
i=1
usados=0

while not i>n:
    bloques=i
    usados=usados+bloques
    i=i+1

print (usados)
