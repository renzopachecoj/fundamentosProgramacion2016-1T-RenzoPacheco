#2011.Termino1.Evaluacion1.Tema1

deposito=float(input('Deposito: '))
interes=float(input('Interes: '))
n=int(input('Año: '))
a=1
saldo=deposito

while not (a>n):
    saldo=saldo+(saldo*interes)
    a=a+1

print (saldo)
