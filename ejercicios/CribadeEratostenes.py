#2008.Termino1.Evaluacion1.Tema2

import numpy

n=int(input('Analizar hasta n: '))
i=1
queda=numpy.zeros(n+1,dtype=int)

while not i>n:
    queda[i]=1
    i=i+1

analizar=2
i=analizar+analizar
while not analizar>n:
    i=analizar+analizar
    while not i>n:
        queda[i]=0
        i=i+analizar
    analizar=analizar+1

i=2
while not i>n:
    if queda[i]==1:
        print(i)
    i=i+1
