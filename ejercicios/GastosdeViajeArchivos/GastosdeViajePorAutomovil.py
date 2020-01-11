#2011.Termino2.Evaluacion3.Tema2
#Renzo Pacheco
import random as rnd
import numpy as np

print('Mapas disponibles: 1,2')
mapa=int(input('Ingrese el numero del mapa: '))
while not ((mapa==1)or(mapa==2)):
    print('Ingrese mapa valido')
    mapa=input('Ingrese el numero del mapa: ')
tabla=np.loadtxt('mapa'+str(mapa)+'.txt')
n,m=np.shape(tabla)

gjuan=0
lugarjuan=0
lugarpedro=0
proximaj=-2
estuvojuan=[]
while not (proximaj==-1):
    estuvojuan.append(lugarjuan+1)
    gjuan=gjuan+tabla[lugarjuan,1]
    moneda=int(rnd.random()*2) 
    if moneda==0:
        direccion=2
    if moneda==1:
        direccion=3
    proximaj=tabla[lugarjuan,direccion]-1
    lugarjuan=int(proximaj)

print('Gastos de Juan: ',gjuan)
print('Ciudades visitadas por Juan: ', estuvojuan)

gpedro=0
lugarpedro=0
proximap=-2
estuvopedro=[]
while not (proximap==-1):
    estuvopedro.append(lugarpedro+1)
    gpedro=gpedro+tabla[lugarpedro,1]
    moneda=int(rnd.random()*2) 
    if moneda==0:
        direccion=2
    if moneda==1:
        direccion=3
    proximap=tabla[lugarpedro,direccion]-1
    lugarpedro=int(proximap)

print('Gastos de Pedro: ',gpedro)
print('Ciudades visitadas por Pedro: ', estuvopedro)
if gpedro>gjuan:
    print('Pedro gasto mas')
if gpedro==gjuan:
    print('Gastaron lo mismo')
if gpedro<gjuan:
    print('Juan gasto mas')
if len(estuvopedro)>len(estuvojuan):
    print('Pedro visito mas ciudades')
if len(estuvopedro)==len(estuvojuan):
    print('Visitaron el mismo numero de ciudades')
if len(estuvopedro)<len(estuvojuan):
    print('Juan visito mas ciudades')

visitados=open('visitados.txt','w')
visitados.write('Juan visito las siguientes ciudades:\n')
visitados.write(str(estuvojuan)+'\n')
visitados.write('Juan gasto: $'+str(gpedro)+'\n')
visitados.write('Pedro visito las siguientes ciudades:\n')
visitados.write(str(estuvopedro)+'\n')
visitados.write('Pedro gasto: $'+str(gpedro)+'\n')
visitados.close()


