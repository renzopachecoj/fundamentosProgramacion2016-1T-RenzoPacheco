#2011.Termino1.Evaluacion1.Tema1

depositoJ=float(input('DepositoJ: '))
depositoP=float(input('DepositoP: '))
interesJ=float(input('InteresJ: '))
interesP=float(input('InteresP: '))

a=1
saldoJ=depositoJ
saldoP=depositoP

while not (saldoJ>saldoP):
    saldoJ=saldoJ+(saldoJ*interesJ)
    saldoP=saldoP+(saldoP*interesP)
    a=a+1
n=a-1
print ('Año buscado: ', n)
print ('Saldo Juan: ', saldoJ)
print ('Saldo Pedro: ', saldoP)
