#Proyecto.Tema2
#2011.Termino1.Evaluacion1.Tema2

import random

vendedores=int(input('Cuantos vendedores: '))
listav=[]
listavm=[]
x=0
              
while x<vendedores:
    oferta=int(input('Valor de la oferta: '))
    listav.append(oferta)
    x=x+1

x=0
menor=listav[0]
while not x>=len(listav):
    if listav[x]<menor:
        menor=listav[x]
    x=x+1

x=0
cuentamenor=0
while not x>=len(listav):
    if listav[x]==menor:
        listavm.append(x+1)
        cuentamenor=cuentamenor+1
    x=x+1

seleccionado=int(random.random()*len(listavm))
    
print ('El menor valor es: ', menor)
print ('Cumplen mejor oferta: ', cuentamenor)
print ('El vendedor seleccionado es:', listavm[seleccionado])
    
            
