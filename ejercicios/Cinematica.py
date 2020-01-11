#Cinematica

import numpy
import matplotlib.pyplot as plt

vx=float(input('Velocidad en x: '))
x0=float(input('Posicion inicial x: '))
vy=float(input('Velocidad en y: '))
y0=float(input('Posicion inicial y: '))
tfinal=float(input('Tiempo de observacion: '))
tiempo=numpy.zeros(tfinal,dtype=float)
posicionx=numpy.zeros(tfinal,dtype=float)
posiciony=numpy.zeros(tfinal,dtype=float)
i=0

while not i>=tfinal:
    tiempo[i]=i
    posicionx[i]=x0+(vx*tiempo[i])
    posiciony[i]=y0+(vy*tiempo[i])+(0.5*-9.8*(tiempo[i]**2))
    i=i+1

print(tiempo)
print(posicionx)
plt.plot(posicionx,posiciony,'ro')
plt.title('Tiro Parabolico')
plt.xlabel('desplazamiento x')
plt.ylabel('desplazamiento y')
plt.show()
